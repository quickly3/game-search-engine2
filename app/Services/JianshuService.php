<?php

namespace App\Services;

use App\Model\Elastic\ElasticModel;

class JianshuService
{
    public static function genWordsCloud()
    {
        $cloud_words = [];

        $es = new ElasticModel("escn", "escn");
        $data = [
            "aggs" => [
                "title_words_cloud" => [
                    "terms" => [
                        "field" => "title_text",
                        "size" => 100
                    ]
                ]
            ],
            "size" => 0
        ];

        $params = [
            "index" => "jianshu",
            "type" => "jianshu",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;
        $cloud_words = $resp->aggregations['title_words_cloud']['buckets'];

        $cloud_words = array_map(function ($item) {
            return (object) $item;
        }, $cloud_words);


        $stop_words = ["基于", "文章", "处理", "什么", "一个", "如何", "问题"];

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
