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
        $resp = InfoqService::getArticles($request);
        return response()->json($resp);
    }

    public function getArticleHistogram(Request $request)
    {
        $resp = InfoqService::getArticleHistogram($request);
        return response()->json($resp);
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
