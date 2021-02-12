<?php

namespace App\Services;

use App\Model\Elastic\ElasticModel;

class ArticleService
{
    public static function getCountBySource()
    {
        $es = new ElasticModel("article", "article");

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

    public static function getMonthHistogramBySource($source)
    {
        $es = new ElasticModel("article", "article");
        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => "source:{$source} && created_at:[2006-01-01 TO *]"
                    ]
                ],
                "aggs" => [
                    "source_date_histogram" => [
                        "date_histogram" => [
                            "field" => "created_at",
                            "calendar_interval" => "month"
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $resp = $es->client->search($params);
        $buckets = $resp['aggregations']['date_histogram']['buckets'];
        dump($buckets);
        $items = [];

        foreach ($buckets as $key => $item) {
            $items[$item['key']] = $item['doc_count'];
        }

        return $items;
    }


}
