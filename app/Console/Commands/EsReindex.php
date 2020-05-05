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
        $this->index = "movie";

        $es = new ElasticModel($this->index);
        $client = $es->client;
        $params = [
            "index" => $this->index,
            "scroll" => "30s",          // how long between scroll requests. should be small!
            "size" => 100,
            "body" => [
                "query" => [
                    "query_string" => [
                        "query" => "*:*"
                    ]
                ],
                "_source"=> "type"
            ]
        ];

        $response = $client->search($params);

        while (isset($response['hits']['hits']) && count($response['hits']['hits']) > 0) {

            foreach ($response['hits']['hits'] as $key => $value) {


                $types = [
                    "series"=> ["欧美","国产","日本","香港","韩国","海外","台湾","泰国"],
                    "comic"=> ["动漫"],
                    "movie"=> ["剧情片","喜剧片","动作片","恐怖片","爱情片","科幻片","战争片"]
                ];

                foreach($types as $key => $type){
                    if(in_array($value['_source']['type'], $type)){
                        $new_type = $key;
                        break;
                    }
                }

                $params = [
                    'index' => $this->index,
                    'id' => $value['_id'],
                    'body' => [
                        'doc' => [
                            'type' => $new_type
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
