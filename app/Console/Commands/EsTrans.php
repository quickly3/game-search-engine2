<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Model\Elastic\ElasticModel;



class EsTrans extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     * @translator laravelacademy.org
     */
    protected $signature = 'EsTrans';

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
        $this->index = "juejin";
        $this->type = "juejin";

        $es = new ElasticModel($this->index, $this->type);
        $client = $es->client;
        $params = [
            "index" => $this->index,
            "type" => $this->type,
            "scroll" => "30s",          // how long between scroll requests. should be small!
            "size" => 100,
            "body" => [
                "query" => [
                    "match_all" => (object) []
                ]
            ]
        ];

        $response = $client->search($params);
        $count = $response['hits']['total'];
        $current = 0;

        while (isset($response['hits']['hits']) && count($response['hits']['hits']) > 0) {

            $params = [];
            foreach ($response['hits']['hits'] as $key => $value) {
                $current++;
                $created_year = isset($value['_source']['createdAt']) ? date("Y", strtotime($value['_source']['createdAt'])) : "";
                $item = $value['_source'];

                if (!isset($item['title'])) {
                    continue;
                }

                $doc = [
                    'title' => $item['title'],
                    'author' => '',
                    'tag' => ucfirst($item['tag']),
                    'source' => 'juejin',
                    'source_id' => $item['jid'],
                    'source_score' => 0,
                    'stars' => 0,
                    'url' => $item['href'],
                    'summary' => $item['summaryInfo'],
                    'created_year' => $created_year,
                    'created_at' => $value['_source']['createdAt']
                ];

                $params['body'][] = [
                    'index' => [
                        '_index' => "article",
                        '_type' => "article"
                    ]
                ];

                $params['body'][] = $doc;
                $this->info("{$current}/{$count}");
            }

            $es->client->bulk($params);


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
