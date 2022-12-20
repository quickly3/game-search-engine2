<?php

namespace App\Services;

use App\Model\Elastic\ElasticModel;
use Illuminate\Http\Request;

class AuthorService
{
    public static function getAuthorTags($author, $size = 100, $source="")
    {
        $es = new ElasticModel("article", "article");
        $query = "*:*";

        if(trim($source) !== ""){
            $query.=" && source:{$source}";
        }

        if(trim($author) !== ""){
            $query.=" && author:{$author}";
        }

        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => $query
                    ]
                ],
                "aggs" => [
                    "tag_agg" => [
                        "terms" => [
                            "field" => "tag",
                            "size" => $size
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $resp = $es->client->search($params);
        $buckets = $resp['aggregations']['tag_agg']['buckets'];

        $items = [];

        foreach ($buckets as $key => $item) {
            $items[] = [
                "name" => $item['key'],
                "value" => $item['doc_count']
            ];
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

    public static function getAuthorTagsAggs($author, $size = 100, $source="")
    {
        $es = new ElasticModel("article", "article");
        $query = "*:*";

        if(trim($source) !== ""){
            $query.=" && source:{$source}";
        }

        if(trim($author) !== ""){
            $query.=" && author:{$author}";
        }

        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => $query
                    ]
                ],
                "aggs" => [
                    "author_terms" => [
                        "terms" => [
                            "field" => "author",
                            "size" => $size
                        ], 
                        "aggs" => [
                            "tag_terms" => [
                              "terms" => [
                                "field" => "tag",
                                "size" => 100
                                ]
                            ]
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $resp = $es->client->search($params);
        $buckets = $resp['aggregations']['author_terms']['buckets'];

        $items = [];

        foreach ($buckets as $item) {
            $items[$item['key']] = $item['tag_terms']["buckets"];
        }
        return $items;
    } 

    public static function getAuthorTagsCates($author, $size = 100, $source="")
    {
        $es = new ElasticModel("article", "article");
        $query = "*:*";

        if(trim($source) !== ""){
            $query.=" && source:{$source}";
        }

        if(trim($author) !== ""){
            $query.=" && author:{$author}";
        }

        $params = [
            "index" => "article",
            "body" =>  [
                "query" => [
                    "query_string" => [
                        "query" => $query
                    ]
                ],
                "aggs" => [
                    "author_terms" => [
                        "terms" => [
                            "field" => "author",
                            "size" => $size
                        ], 
                        "aggs" => [
                            "cate_terms" => [
                              "terms" => [
                                "field" => "category",
                                "size" => 100
                                ]
                            ]
                        ]
                    ]
                ],
                "size" => 0
            ]
        ];

        $resp = $es->client->search($params);
        $buckets = $resp['aggregations']['author_terms']['buckets'];

        $items = [];

        foreach ($buckets as $item) {
            $items[$item['key']] = $item['cate_terms']["buckets"];
        }
        return $items;
    } 



    public static function getAuthors(Request $request){
        $keywords = $request->input("keywords", "");
        $sortBy = $request->input("sortBy", "");
        $size = $request->input("size", 20);
        $source = strtolower($request->input("source", "all"));

        $es = new ElasticModel("author", "author");

        if ($keywords != '') {
            $query_string = "user_name:\"{$keywords}\" || user_name:*$keywords* ";
        }else{
            $query_string = "*:*";
        }

        if ($source != "all") {
            $query_string .= " && source:{$source}";
        }

        $data = $es;

        $highlight = [
            "fields" => [
                "user_name" => (object) [],
            ],
        ];
        $data->size($size)->highlight($highlight);

        if($sortBy !== ""){
            $sortBy = $sortBy['value'];
        }

        switch($sortBy){
            case "power":
                $orders = [
                    "power" => "desc",
                    "_score" => "desc",
                ];
                break;
            case "post_article_count":
                $orders = [
                    "post_article_count" => "desc",
                    "_score" => "desc",
                ];
                break;
            case "level":
                $orders = [
                    "level" => "desc",
                    "_score" => "desc",
                ];
                break;

            default:
                $orders = [
                    "post_article_count" => "desc",
                    "_score" => "desc",
                ];
        }
        $data->orderBy($orders);

        // $data->orderBy($orders);

        try {
            $data = $data->query_string($query_string, "*")->paginate(20);
        } catch (\Throwable $th) {
            $data = ["data"=>[]];
        }

        $data['query_string'] = $query_string;
        $data['orderBy'] = $orders;

        $authors = array_map(function($author){
            return '"'.$author['user_name'].'"';
        },$data['data']);

        if(count($authors) > 0){
            $authors_str = "(" . join(" || ",$authors) . ")";
            $author_tags = SELF::getAuthorTagsAggs($authors_str);
            $author_cates = SELF::getAuthorTagsCates($authors_str);
            
            foreach($data['data'] as &$author){
                $match_tags = array_filter($author_tags,function($at ,$user_name) use ($author){
                    return $user_name == $author['user_name'];
                },1);

                $match_cates = array_filter($author_cates,function($at ,$user_name) use ($author){
                    return $user_name == $author['user_name'];
                },1);


                if($match_tags[$author['user_name']]){
                    $author['article_tags'] = $match_tags[$author['user_name']];
                }

                if($author_cates[$author['user_name']]){
                    $author['article_cates'] = $author_cates[$author['user_name']];
                }
            }

        }
        return $data;
    }

}
