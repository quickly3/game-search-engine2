<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Model\Elastic\ElasticModel;
use App\Services\InfoqService;
use Illuminate\Http\Request;
use Carbon\Carbon;

class InfoqController extends Controller
{
    public function getDailyList(Request $request)
    {
        $keywords = $request->input("keywords", "");
        $tag = $request->input("tag", "all");
        $source = strtolower($request->input("source", "all"));
        $search_type = trim($request->input("search_type", ""));
        $startDate = $request->input("startDate", "");
        $endDate = $request->input("endDate", "");
        $sortBy = $request->input("sortBy", "");
        $author = $request->input("author", '');
        $updateSta = $request->input("updateSta", true);
        $selectTags = $request->input("selectTags", []);
        $selectCategories = $request->input("selectCategories", []);

        $collect_count = $request->input("collect_count", null);
        $comment_count = $request->input("comment_count", null);
        $digg_count = $request->input("digg_count", null);
        $view_count = $request->input("view_count", null);


        $es = new ElasticModel("article", "article");

        if ($search_type == "simple") {
            $data = $es->source(["title"]);
            if (trim($keywords) == "") {
                $keywords = "''";
            }
        } else {
            $data = $es;
            if (trim($keywords) == "") {
                $keywords = "*";
            }
            $highlight = [
                "fields" => [
                    "summary" => (object) [],
                    "title.text_cn" => (object) [],
                ],
            ];
            $data->highlight($highlight);
        }

        if ($keywords != '*') {
            $query_string = "(title.text_cn:'{$keywords}' OR title.text_cn:\"{$keywords}\" OR summary.text_cn:'{$keywords}' OR summary.text_cn:\"{$keywords}\") ";
        }else{
            $query_string = "*:*";
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

        try {
            $data = $data->query_string($query_string, "*")->paginate(20);
        } catch (\Throwable $th) {
            $data = ["data"=>[]];
        }
        

        $data['query_string'] = $query_string;

        if (!empty($data['data'])) {
            $data['data'] = array_map(function ($item) {
                if (isset($item['highlight']) && isset($item['highlight']['summary']) && isset($item['highlight']['summary'][0])) {
                    $item['summary'] = $item['highlight']['summary'][0];
                }

                if (isset($item['highlight']) && isset($item['highlight']['title.text_cn']) && isset($item['highlight']['title.text_cn'][0])) {
                    $item['title'] = $item['highlight']['title.text_cn'][0];
                }

                return $item;
            }, $data['data']);
        }
        // if($updateSta){
        //     $tags = InfoqService::getTagsByQuery($query_string);
        //     $wordsCloud = InfoqService::genWordsCloudByQuery($query_string);
        //     $data['tags'] = $tags;
        //     $data['wordsCloud'] = $wordsCloud;
        // }
        return response()->json($data);
    }

    public function getWordsCloud(Request $request)
    {

        $tag = strtolower($request->input("tag", "all"));
        $source = strtolower($request->input("source", "all"));

        $tag = $tag == "Postgresql" ? "PostgreSQL" : $tag;
        $words_cloud = InfoqService::genWordsCloud($tag, $source);

        return response()->json($words_cloud);
    }

    public function starsChange(Request $request)
    {
        $params = $request->input("params", null);
        $item = $params['item'];
        $resp = InfoqService::updateStarsById($item['_id'], $item["stars"]);

        return response()->json($resp);
    }

    public function autoComplete(Request $request){
        $text = $request->input("keywords");

        $es = new ElasticModel("article");

        $field = "title.auto_completion";

        if(trim($text) == ""){
            $resp = [];
        }else{
            $resp = $es->source(["title"])->autoComplete($text,$field);
        }

        return response()->json($resp);
    }

    public function getTags(Request $request)
    {
        $source = strtolower($request->input("source", "all"));
        $tags = InfoqService::getTags($source);
        return response()->json($tags);
    }

    public function getCategories(Request $request)
    {
        $source = strtolower($request->input("source", "all"));
        $tags = InfoqService::getCategories($source);
        return response()->json($tags);
    }
    

}
