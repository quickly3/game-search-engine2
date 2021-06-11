<?php

namespace App\Services;

use App\Model\Elastic\ElasticModel;

class GraphService
{
    public function getDailyGraph(){
        $es = new ElasticModel("article");

        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => "*:*"
                    ]
                ],
                "aggs" => [
                    "count_over_time" => [
                        "terms" => [
                            "field" => "source"
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $resp = $es->client->search($params);
        $buckets = $resp['aggregations']['count_over_time']['buckets'];

        $items = [];

        foreach ($buckets as $key => $item) {
            $items[$item['key']] = $item['doc_count'];
        }

        return $items;
    }
}