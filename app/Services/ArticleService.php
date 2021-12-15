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
        $items = [];

        foreach ($buckets as $key => $item) {
            $items[$item['key']] = $item['doc_count'];
        }

        return $items;
    }

    public static function getHistogram($query_string = "*:*",$calendar_interval = "month")
    {
        $es = new ElasticModel("article", "article");
        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => "{$query_string}"
                    ]
                ],
                "aggs" => [
                    "source_date_histogram" => [
                        "date_histogram" => [
                            "field" => "created_at",
                            "calendar_interval" => $calendar_interval,
                            "format"=> "yyyy-MM-dd"
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $resp = $es->client->search($params);

        $buckets = $resp['aggregations']['source_date_histogram']['buckets'];
        $items = [];

        foreach ($buckets as $key => $item) {
            $items[] = [
                "date" => $item["key_as_string"],
                "count" => $item["doc_count"]
            ];
        }
        return $items;
    }
}
