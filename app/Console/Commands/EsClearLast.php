<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Model\Elastic\ElasticModel;



class EsClearLast extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     * @translator laravelacademy.org
     */
    protected $signature = 'EsClearLast';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Send drip e-mails to a user';

    /**
     * The drip e-mail service.
     *
     */
    protected $drip;

    /**
     * Create a new command instance.
     *
     */
    public function __construct()
    {
        parent::__construct();
    }

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
        $this->del_ids = [];
        $lastDay = date("Y-m-d",strtotime("-1 day"));

        $es = new ElasticModel("article", "article");
        $client = $es->client;
        $params = [
            "index" => "article",
            "scroll" => "30s",          // how long between scroll requests. should be small!
            "size" => 100,
            "body" => [
                "query" => [
                    "query_string" => [
                        "query" => "source:* && -source:github && created_at:[{$lastDay} TO *]"
                    ]
                ]
            ],
            "_source" => ["url"]
        ];

        $response = $client->search($params);

        while (isset($response['hits']['hits']) && count($response['hits']['hits']) > 0) {

            foreach ($response['hits']['hits'] as $key => $value) {
                $url = $value['_source']['url'];
                $tags = isset($value['_source']['tag'])?$value['_source']['tag']:[];
                if (!isset($this->del_ids[$url])) {
                    $this->del_ids[$url] = [$value['_id']];
                } else {
                    if(in_array("news",$tags)){
                        array_unshift($this->del_ids[$url],$value['_id']);
                    }else{
                        $this->del_ids[$url][] = $value['_id'];
                    }
                }
            }
            $scroll_id = $response['_scroll_id'];
            $response = $client->scroll(
                [
                    "scroll_id" => $scroll_id,  //...using our previously obtained _scroll_id
                    "scroll" => "30s"           // and the same timeout window
                ]
            );
        }
        $count = count($this->del_ids);
        $current = 0;
        foreach ($this->del_ids as $url => $ids) {
            $current++;
            if (count($ids) > 1) {
                $_id = $ids[0];
                $params = [
                    "index" => "article",
                    "body" => [
                        "query" => [
                            "query_string" => [
                                "query" => "url:\"{$url}\" && -_id:\"{$_id}\""
                            ]
                        ]
                    ],
                ];

                $res = $client->deleteByQuery($params);
            }
            $this->info("{$current}/{$count}");
        }
    }
}
