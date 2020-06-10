<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Model\Elastic\ElasticModel;
use App\Services\InfoqService;
use Illuminate\Http\Request;

class InfoqController extends Controller
{
    public function getDailyList(Request $request)
    {
        $keywords = $request->input("keywords", "");
        $tag = strtolower($request->input("tag", "all"));
        $source = strtolower($request->input("source", "all"));
        $search_type = trim($request->input("search_type", ""));

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
                    // "title" => (object) [],
                    "title_text" => (object) [],
                ],
            ];
            $data->highlight($highlight);
        }

        if ($keywords != '*') {
            $keywords = "'" . $keywords . "'";
        }

        $query_string = "(title_text:{$keywords} OR summary:{$keywords})  ";

        if ($tag != "all") {
            $query_string = $query_string . " && tag:{$tag}";
        }

        if ($source != "all") {
            $query_string = $query_string . " && source:{$source}";
        }

        $orders = [
            "created_year" => "desc",
            "created_at" => "desc",
            "_score" => "desc",
            "title" => "asc",
            "_id" => "desc",
        ];

        $data->orderBy($orders);

        $data = $data->query_string($query_string, "*")->paginate(20);

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


}
