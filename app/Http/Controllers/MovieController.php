<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Model\Elastic\ElasticModel;
use App\Services\JianshuService;
use Illuminate\Http\Request;

class MovieController extends Controller
{
    public function getList(Request $request)
    {
        $keywords = $request->input("keywords", "");
        $search_type = trim($request->input("search_type", ""));
        $type = trim($request->input("type", ""));


        $es = new ElasticModel("movie");

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
                    "title" => (object) [],
                ],
            ];
            $data->highlight($highlight);
        }
        
        $query_string = "title.text_cn:{$keywords}";

        if($type!=""){
            $query_string = "type:{$type} && ".$query_string;
        }

        $orders = [
            "title" => "desc",
        ];

        $data->source(["title","image","type"])->orderBy($orders);
        $data = $data->query_string($query_string, "*")->paginate(18);
        $data['query_string'] = $query_string;

        return response()->json($data);
    }

    public function getWordsCloud(Request $request)
    {

        $words_cloud = JianshuService::genWordsCloud();
        return response()->json($words_cloud);
    }

    public function getDetail(Request $request){
        $id = $request->input("id");

        $es = new ElasticModel("movie","movie");
        $data = $es->source(["name", "version"])->getById($id, "*");

        return response()->json($data);

    }

    public function autoComplete(Request $request){
        $text = $request->input("keywords");

        $es = new ElasticModel("movie");

        $field = "title.search";

        if(trim($text) == ""){
            $resp = [];
        }else{
            $resp = $es->source(["title"])->autoComplete($text,$field);
        }

        return response()->json($resp);
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
