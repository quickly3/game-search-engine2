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
        $tag = ucfirst(strtolower($request->input("tag", "All")));

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
                    "title_text" => (object) [],
                ],
            ];
            $data->highlight($highlight);
        }

        $query_string = "title_text:{$keywords}";

        if ($tag != "All") {
            $query_string = $query_string . " && ((title_text:{$tag})^3 OR tag:{$tag} OR summary:{$tag} )";
        }

        $orders = [
            "_score" => "desc",
            "title" => "asc",
            "_id" => "desc"
        ];

        $data->orderBy($orders);
        $data = $data->query_string($query_string, "*")->paginate(10);

        $data['query_string'] = $query_string;
        return response()->json($data);
    }

    public function getWordsCloud(Request $request)
    {

        $tag = ucfirst(strtolower($request->input("tag", "All")));

        $tag = $tag == "Postgresql" ? "PostgreSQL" : $tag;
        $words_cloud = InfoqService::genWordsCloud($tag);


        return response()->json($words_cloud);
    }

    public function starsChange(Request $request)
    {
        $params = $request->input("params", null);
        $item = $params['item'];
        $resp = InfoqService::updateStarsById($item['_id'], $item["stars"]);

        return response()->json($resp);;
    }

    // public function getGameDataById(Request $request){
    //     $id = $request->input("id","");

    //     $es = new ElasticModel("games","games");
    //     $query = [  "match_all" => (object)[]];
    //     $query_string = "name:英雄";
    //     $data = $es->source(["name","version"])->getById($id,"*");

    //     return response()->json($data);
    // }

}
