<?php

namespace App\Services;

use App\Model\Elastic\ElasticModel;

class InfoqService
{
    public static function updateStarsById($id, $stars)
    {
        $index = new ElasticModel("article", "article");
        $body = [
            'doc' => [
                'stars' => $stars
            ]
        ];

        return $index->updateById($id, $body);
    }

    public static function genWordsCloud($tag, $source)
    {
        $cloud_words = [];

        $es = new ElasticModel("article", "article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "*:*"
                ]
            ],
            "aggs" => [
                "title_words_cloud" => [
                    "terms" => [
                        "field" => "title.text_cn",
                        "size" => 100
                    ]
                ]
            ],
            "size" => 0
        ];

        if ($tag != "all") {
            $data['query']['query_string']['query'] .= " && tag:{$tag}";
        }

        if ($source != "all") {
            $data['query']['query_string']['query'] .= " && source:{$source}";
        }

        $params = [
            "index" => "article",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;
        $cloud_words = $resp->aggregations['title_words_cloud']['buckets'];

        $cloud_words = array_map(function ($item) {
            return (object) $item;
        }, $cloud_words);

        $stop_words = [
            "基于", "文章", "处理", "什么", "一个", "如何", "问题", "利用", "2019", "2018","10",
            "php", "python", "javascript", "js", "css", "linux", "node","postgresql", "typescript",
            "java", "vue", "web","react"
        ];

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

    public static function getTags($source)
    {
        $cloud_words = [];

        $es = new ElasticModel("article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "*:*"
                ]
            ],
            "aggs" => [
                "tags" => [
                    "terms" => [
                        "field" => "tag",
                        "size" => 200
                    ]
                ]
            ],
            "size" => 0
        ];

        if ($source != "all") {
            $data['query']['query_string']['query'] .= " && source:{$source}";
        }

        $params = [
            "index" => "article",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;
        $tags = $resp->aggregations['tags']['buckets'];

        return $tags;
    }

    public static function getLastDayArticle()
    {

        $today = date('Y-m-d',strtotime("-1 day"));
        // $today = "2020-12-09";
        $es = new ElasticModel("article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "source:escn && created_at:{$today}"
                ]
            ]
        ];

        $params = [
            "index" => "article",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;

        $data = array_map(function($item){
            return $item['_source'];
        },$resp->hits['hits']);
        return $data;
    }

    public static function getLastDayInfoqArticle()
    {

        $lastDay = date('Y-m-d',strtotime("-1 day"));
        // $today = "2020-12-09";
        $es = new ElasticModel("article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "source:escn && created_at:{$lastDay}"
                ]
            ]
        ];

        $params = [
            "index" => "article",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;

        $data = array_map(function($item){
            return $item['_source'];
        },$resp->hits['hits']);
        return $data;
    }

}
