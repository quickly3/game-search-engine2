<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Model\Elastic\ElasticModel;

use Carbon\Carbon;



class EsReindex extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     * @translator laravelacademy.org
     */
    protected $signature = 'EsReindex';

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
        $this->index = "article";
        $this->type = "article";


        $es = new ElasticModel($this->index, $this->type);
        $client = $es->client;
        $params = [
            "index" => $this->index,
            "type" => $this->type,
            "scroll" => "30s",          // how long between scroll requests. should be small!
            "size" => 100,
            "body" => [
                "query" => [
                    "query_string" => [
                        "query" => "source:cnblogs"
                    ]
                ]
            ]
        ];

        $response = $client->search($params);

        while (isset($response['hits']['hits']) && count($response['hits']['hits']) > 0) {

            foreach ($response['hits']['hits'] as $key => $value) {

                $created_year = date("Y", strtotime($value['_source']['createdAt']));
                $params = [
                    'index' => $this->index,
                    'type' => $this->type,
                    'id' => $value['_id'],
                    'body' => [
                        'doc' => [
                            'created_year' => $created_year,
                            'created_at' => date('c', strtotime($value['_source']['createdAt'])),
                            'summary' => $value['_source']['summary']
                        ]
                    ]
                ];

                $es->client->update($params);
            }

            $scroll_id = $response['_scroll_id'];
            $response = $client->scroll(
                [
                    "scroll_id" => $scroll_id,  //...using our previously obtained _scroll_id
                    "scroll" => "30s"           // and the same timeout window
                ]
            );
        }
    }
}
