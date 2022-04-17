<?php

namespace App\Services;

use App\Model\Elastic\ElasticModel;
use Illuminate\Http\Request;

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

    public static function genWordsCloud($tag, $source ,$size = 100)
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
                        "field" => "title",
                        "size" => $size
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

    public static function genWordsCloudByQuery($query_string)
    {
        $cloud_words = [];

        $es = new ElasticModel("article", "article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "$query_string"
                ]
            ],
            "aggs" => [
                "title_words_cloud" => [
                    "terms" => [
                        "field" => "title",
                        "size" => 100
                    ]
                ]
            ],
            "size" => 0
        ];

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
            "基于", "文章", "处理", "什么", "一个", "如何", "问题", "利用", "2021","2020","2019","2019", "2018","10",
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


    public static function getTagsByQuery($query_string)
    {
        $cloud_words = [];

        $es = new ElasticModel("article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "$query_string"
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

        $params = [
            "index" => "article",
            "body" =>  $data
        ];

        $data = $es->client->search($params);
        $resp = (object) $data;
        $tags = $resp->aggregations['tags']['buckets'];

        return $tags;
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

    public static function getCategories($source)
    {
        $es = new ElasticModel("article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "*:*"
                ]
            ],
            "aggs" => [
                "categories" => [
                    "terms" => [
                        "field" => "category",
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
        $tags = $resp->aggregations['categories']['buckets'];

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

    public static function getLastDayArticleByQuery($query)
    {

        $lastDay = date('Y-m-d',strtotime("-1 day"));
        // $lastDay = date('Y-m-d');

        // $today = "2020-12-09";
        $es = new ElasticModel("article");
        $data = [
            "query" => [
                "query_string" => [
                    "query" => "{$query} && created_at:{$lastDay}"
                ]
            ],
            "size"=>20,
            "sort" => [
                [
                    "created_at"=> [
                        "order"=> "desc"
                    ]
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

    public static function getArticles(Request $request){

        $search_type = trim($request->input("search_type", ""));
        $sortBy = $request->input("sortBy", "");
        $updateSta = $request->input("updateSta", true);
        $keywords = $request->input("keywords", "");

        if (trim($keywords) == "") {
            $keywords = "*";
        }

        $es = new ElasticModel("article", "article");

        if ($search_type == "simple") {
            $data = $es->source(["title"]);
        } else {
            $data = $es;
            $highlight = [
                "fields" => [
                    "summary" => (object) [],
                    "title" => (object) [],
                ],
            ];
            $data->highlight($highlight);
        }

        switch($sortBy){
            case "date":
                $orders = [
                    "created_at" => "desc",
                    "_score" => "desc",
                    "created_year" => "desc",
                    "title" => "asc",
                ];

                break;
            case "score":
                $orders = [
                    "_score" => "desc",
                    "created_year" => "desc",
                    "created_at" => "desc",
                    "title" => "asc",
                ];
                break;
            case "multi":
                $orders = [
                    "_score" => "desc",
                    "created_year" => "desc",
                    "created_at" => "desc",
                    "title" => "asc",
                ];
                break;
            case "viewed":
                $orders = [
                    "view_count" => "desc",
                    "created_year" => "desc",
                    "created_at" => "desc",
                    "title" => "asc",
                ];
                break;
            case "like":
                $orders = [
                    "digg_count" => "desc",
                    "created_year" => "desc",
                    "created_at" => "desc",
                    "title" => "asc",
                ];
                break;
            case "comments":
                $orders = [
                    "comment_count" => "desc",
                    "created_year" => "desc",
                    "created_at" => "desc",
                    "title" => "asc",
                ];
                break;
            case "collected":
                $orders = [
                    "collect_count" => "desc",
                    "created_year" => "desc",
                    "created_at" => "desc",
                    "title" => "asc",
                ];
                break;
            default:
                $orders = [
                    "created_at" => "desc",
                    "_score" => "desc",
                    "created_year" => "desc",
                    "title" => "asc",
                ];
        }

        $data->orderBy($orders);

        $query = SELF::articlesQueryBuilder($request);
        $query_string = $query['query_string'];

        try {
            $data = $data->query($query, "*")->paginate(20);
        } catch (\Throwable $th) {
            $data = ["data"=>[]];
        }
        $data['query_string'] = $query_string;

        if (!empty($data['data'])) {
            $data['data'] = array_map(function ($item) {
                if (isset($item['highlight']) && isset($item['highlight']['summary']) && isset($item['highlight']['summary'][0])) {
                    $item['summary'] = $item['highlight']['summary'][0];
                }

                if (isset($item['highlight']) && isset($item['highlight']['title']) && isset($item['highlight']['title'][0])) {
                    $item['title'] = $item['highlight']['title'][0];
                }

                return $item;
            }, $data['data']);
        }

        return $data;
    }

    public static function getArticleHistogram(Request $request){

        $query = SELF::articlesQueryBuilder($request);
        $query_string = $query['query_string'];

        $resp = ArticleService::getHistogram($query,'day');

        $data = [
            'query_string' => $query_string,
            'data' => $resp,
        ];

        return $data;
    }

    public static function getWordsCloudByQueryBuilder(Request $request, $size=1000){

        $query = SELF::articlesQueryBuilder($request);
        $query_string = $query['query_string'];

        $resp = ArticleService::getWordsCloud($query, $size=1000);

        $data = [
            'query_string' => $query_string,
            'data' => $resp,
        ];

        return $data;
    }

    public static function getAuthorTermsAggByQueryBuilder(Request $request, $size=1000){

        $query = SELF::articlesQueryBuilder($request);
        $query_string = $query['query_string'];
        
        $article  = new ArticleService();
        return [
            'data' => $article->getAuthorTermsAgg($query),
            'query_string' => $query_string
        ];
    }
    


    public static function escapeElasticReservedChars($string) {
        $regex = "/[\\+\\-\\=\\&\\|\\!\\(\\)\\{\\}\\[\\]\\^\\\"\\~\\*\\<\\>\\?\\:\\\\\\/]/";
        return preg_replace($regex, addslashes('\\$0'), $string);
    }

    public static function articlesQueryBuilder(Request $request){

        $keywords = $request->input("keywords", "*");
        $tag = $request->input("tag", "all");
        $source = strtolower($request->input("source", "all"));
        $startDate = $request->input("startDate", "");
        $endDate = $request->input("endDate", "");
        $author = $request->input("author", '');
        $selectTags = $request->input("selectTags", []);
        $selectCategories = $request->input("selectCategories", []);
        $collect_count = $request->input("collect_count", null);
        $comment_count = $request->input("comment_count", null);
        $digg_count = $request->input("digg_count", null);
        $view_count = $request->input("view_count", null);
        $and_operator = $request->input("and_operator", false);

        $keywords = SELF::escapeElasticReservedChars($keywords);

        if ($keywords == '*' || !$keywords) {
            $query_string = "*:*";
        }else{
            $query_string = "(title:({$keywords}) OR title:\"{$keywords}\" OR summary:({$keywords}) OR summary:\"{$keywords}\") ";
        }

        if(count($selectTags)){
            $selectTags = array_map(function($tag){ return "\"$tag\""; }, $selectTags);
            $selectTagsStr = join(' || ',$selectTags);
            $query_string = $query_string . " && tag:({$selectTagsStr})";
        }

        if(count($selectCategories)){
            $selectCategories = array_map(function($tag){ return "\"$tag\""; }, $selectCategories);
            $selectCategoriesStr = join(' || ',$selectCategories);
            $query_string = $query_string . " && category:({$selectCategoriesStr})";
        }

        if ($tag != "all") {
            $query_string = $query_string . " && tag:{$tag}";
        }

        if ($source != "all") {
            $query_string = $query_string . " && source:{$source}";
        }

        if ($author != "") {
            $query_string = $query_string . " && (author:{$author} OR author:*{$author}*)";
        }

        if(trim($startDate) !== ''){
            $query_string = $query_string . " && created_at:[{$startDate} TO *]";
        }

        if(trim($endDate) !== ''){
            $query_string = $query_string . " && created_at:[* TO {$endDate}}";
        }

        if(!is_null($collect_count)){
            $query_string = $query_string . " && collect_count:[{$collect_count} TO *}";
        }

        if(!is_null($comment_count)){
            $query_string = $query_string . " && comment_count:[{$comment_count} TO *}";
        }

        if(!is_null($digg_count)){
            $query_string = $query_string . " && digg_count:[{$digg_count} TO *}";
        }

        if(!is_null($view_count)){
            $query_string = $query_string . " && view_count:[{$view_count} TO *}";
        }

        $query = [
            "query_string" => [
                "query" => "{$query_string}"
            ]
        ];

        if($and_operator){
            $query['query_string']['default_operator'] = "AND";
        }

        return $query;
    }
}
