<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Model\Elastic\ElasticModel;
use App\Services\JianshuService;
use Illuminate\Http\Request;

class JianshuController extends Controller
{
    public function getDailyList(Request $request)
    {
        $keywords = $request->input("keywords", "");
        $search_type = trim($request->input("search_type", ""));

        $es = new ElasticModel("jianshu", "jianshu");

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

        $orders = [
            "title" => "desc",
        ];

        $data->orderBy($orders);
        $data = $data->query_string($query_string, "*")->paginate(10);

        return response()->json($data);
    }

    public function getWordsCloud(Request $request)
    {

        $words_cloud = JianshuService::genWordsCloud();
        return response()->json($words_cloud);
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
