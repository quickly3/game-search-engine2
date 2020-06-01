<?php

namespace App\Model\Elastic;

use Elasticsearch\ClientBuilder;
use Request;

class ElasticModel
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function __construct($index_name)
    {

        $this->connect();
        $this->index = $this->index_maped($index_name);
        // $this->index_type = $type;
        $this->page = 1;
        $this->size = 10;
        $this->from = 0;
        $this->orders = [
            "_score" => "desc",
        ];
    }

    public function index_maped($index_name)
    {
        $map = [
            "games" => "games",
        ];

        return isset($map[$index_name]) ? $map[$index_name] : $index_name;
    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function connect()
    {
        $hosts = [];
        $main_host = getenv("ES_HOST") . ":" . getenv("ES_PORT");
        $hosts[] = $main_host;
        $clientBuilder = ClientBuilder::create(); // Instantiate a new ClientBuilder
        $clientBuilder->setHosts($hosts); // Set the hosts
        // $clientBuilder->setBasicAuthentication(getenv("ES_USER"), getenv("ES_PWD"));
        $this->client = $clientBuilder->build();
        $this->source = [];
    }

    public function search($params)
    {
        return $this->client->search($params);
    }

    public function autoComplete($text, $field){
        $params = [
            "index" => $this->index,
            "body" => [
                "suggest" => [
                    "_suggest" => [
                        "text" => $text,
                        "completion" => [
                            "field" => $field
                        ]
                    ]
                ],
                "_source" => false
            ]
        ];
        $resp = $this->client->search($params);

        $respFormated = array_map(function($data){
            return $data["text"];
        },$resp["suggest"]["_suggest"][0]["options"]);

        return $respFormated;
    }

    public function source($source)
    {
        $this->source = $source;
        return $this;
    }

    public function query_string($keyword, $fields)
    {
        $params = [
            "index" => $this->index,
            "body" => [
                "query" => [
                    "query_string" => [
                        // "default_field" => $fields,
                        "query" => $keyword,
                        "default_operator" => "AND"
                    ],
                ],
                "sort" => $this->orders,
            ],
        ];
        if (isset($this->highlight)) {
            $params["body"]["highlight"] = $this->highlight;
        }

        $this->request_body = $params;
        $this->setSource();

        return $this;
    }

    public function getById($id, $fields)
    {
        $params = [
            "index" => $this->index,
            "id" => $id,
        ];

        $this->get($params);

        $res = $this->reqRes;
        $source = false;

        if ($res['found'] == true) {
            $source = $res['_source'];
            $source['_id'] = $res['_id'];
        }
        return $source;
    }

    public function size($size)
    {
        $this->request_body["body"]["size"] = $size;
        return $this;
    }

    public function from($from)
    {
        $this->request_body["body"]["from"] = $from;
        return $this;
    }

    public function orderBy($orders)
    {
        $this->orders = $orders;
        return $this;
    }

    public function highlight($highlight)
    {
        $this->highlight = $highlight;
        return $this;
    }

    public function query($query)
    {

        $params = [
            "index" => $this->index,
            "type" => $this->index_type,
            "body" => [
                "query" => $query,
            ],
        ];
        $this->request_body = $params;
        $this->setSource();
        $this->setReqRes();

        return $this;
    }

    public function paginate($size)
    {
        $page = (int) Request::input("page", 1);
        $from = ($page - 1) * $size;

        $this->request_body["body"]["size"] = $size;
        $this->request_body["body"]["from"] = $from;

        $this->request_body["body"]["track_total_hits"] = true;

        $this->setReqRes();
        $res = [];

        $res['current_page'] = $page;
        $res['total'] = $this->reqRes['hits']['total']['value'];



        $res['last_page'] = ceil($res['total'] / $size);
        $res['from'] = $from;
        $res['to'] = $from + $size;
        $res['per_page'] = $size;

        $res['data'] = $this->getIdRes();
        return $res;
    }

    private function setSource()
    {
        if (!empty($this->source)) {
            $this->request_body["body"]["_source"] = $this->source;
        }
        return $this;
    }

    private function setReqRes()
    {
        $this->reqRes = $this->client->search($this->request_body);
    }

    private function get($params)
    {
        $this->reqRes = $this->client->get($params);
    }

    public function match_all()
    {
        $params = [
            "index" => $this->index,
            "type" => $this->index_type,
            "body" => [
                "query" => ["match_all" => (object) []],
            ],
        ];
        $this->setSource();
        $this->setReqRes($params);

        return $this;
    }

    public function getRes()
    {
        $hits = $this->reqRes["hits"]["hits"];
        return $hits;
    }

    public function getIdRes()
    {
        $res = [];
        $hits = $this->reqRes["hits"]["hits"];

        if (!empty($hits)) {
            foreach ($hits as $key => $item) {
                $source = $item['_source'];
                $source['_id'] = $item['_id'];

                if (isset($item['highlight'])) {
                    $source['highlight'] = $item['highlight'];
                }

                $res[] = $source;
            }
        }
        return $res;
    }

    public function updateById($id, $body)
    {
        $params = [
            "index" => $this->index,
            "type" => $this->index_type,
            'id' => $id,
            'body' => $body
        ];

        $response = $this->client->update($params);
        return $this;
    }

    public function updateByQueryString($query, $fields)
    {
    }


    // public function get
}
