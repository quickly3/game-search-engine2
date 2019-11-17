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

    public static function genWordsCloud($tag)
    {
        $cloud_words = [];

        $es = new ElasticModel("article", "article");
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

        if ($tag != "all") {
            $data['query'] = ["query_string" => ["query" => "tag:{$tag}"]];
        }

        $params = [
            "index" => "article",
            "type" => "article",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;
        $cloud_words = $resp->aggregations['title_words_cloud']['buckets'];

        $cloud_words = array_map(function ($item) {
            return (object) $item;
        }, $cloud_words);

        $stop_words = ["基于", "文章", "处理", "什么", "一个", "如何", "问题", "利用", "2019", "2018"];
        switch (strtolower($tag)) {
            case 'php':
                $ext_stop_words = ["php"];
                break;
            case 'python':
                $ext_stop_words = ["python"];
                break;
            case 'javascript':
                $ext_stop_words = ["javascript", "js"];
                break;
            case 'css':
                $ext_stop_words = ["css"];
                break;
            case 'linux':
                $ext_stop_words = ["linux"];
                break;
            case 'node':
                $ext_stop_words = ["node"];
                break;
            case 'postgresql':
                $ext_stop_words = ["postgresql"];
                break;
            case 'typescript':
                $ext_stop_words = ["typescript", "2.5", "3.0"];
                break;
            default:
                $ext_stop_words = [];
                break;
        }

        $stop_words = array_merge($stop_words, $ext_stop_words);


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
