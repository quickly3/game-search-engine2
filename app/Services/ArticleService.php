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

    public static function getWordsCloud($query_string = "*:*", $size = 1000)
    {
        $es = new ElasticModel("article", "article");

        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => $query_string
                    ]
                ],
                "aggs" => [
                    "title_words_cloud" => [
                        "terms" => [
                            "field" => "title.text_smart",
                            "size" => $size
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;
        $cloud_words = $resp->aggregations['title_words_cloud']['buckets'];

        $cloud_words = array_map(function ($item) {
            return (object) $item;
        }, $cloud_words);


        $stop_words = file(app_path().'/Services/stopwords.txt');
        $stop_words = array_map(function($word){
            return trim($word);
        },$stop_words);

        $cloud_words = array_filter($cloud_words, function ($item) use ($stop_words) {

            $matched = true;

            if (mb_strlen($item->key) == 1) {
                $matched = false;
            }

            if (in_array($item->key, $stop_words)) {
                $matched = false;
            }

            return $matched;
        });

        $cloud_words = array_merge($cloud_words, []);
        return $cloud_words;
    }


}
