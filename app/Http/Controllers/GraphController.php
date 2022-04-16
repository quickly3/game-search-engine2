<?php

namespace App\Http\Controllers;

use App\Services\GraphService;
use App\Services\InfoqService;
use App\Services\AuthorService;
use Illuminate\Http\Request;
class GraphController extends Controller
{

    function getLastDayData()
    {
        $graph  = new GraphService();
        return $graph->getDailyGraph();
    }

    function getTotalGraph()
    {
        $graph  = new GraphService();
        return $graph->getTotalGraph();
    }

    function dailyMd()
    {
        $info = new InfoqService();
        $escn = $info::getLastDayArticleByQuery('source:escn');
        $juejin = $info::getLastDayArticleByQuery('source:juejin && tag:news');
        $infoq = $info::getLastDayArticleByQuery('source:infoq');
        $oschina = $info::getLastDayArticleByQuery('source:oschina && tag:news');
        $cnblogs = $info::getLastDayArticleByQuery('source:cnblogs && tag:news');


        $yesterday = date('Y-m-d',strtotime("-1 day"));

        $escn_title = isset($escn[0])?$escn[0]['summary']:'';
        $escn_title = str_replace("({$yesterday}）", '', $escn_title);

        $resp = [
            [
                "title" => "掘金资讯",
                "data" => $juejin
            ],
            [
                "title" => "InfoQ 热门话题",
                "data" => $infoq
            ],
            [
                "title" => "开源中国资讯",
                "data" => $oschina
            ],
            [
                "title" => $escn_title,
                "data" => $escn
            ],
            [
                "title" => "博客园新闻",
                "data" => $cnblogs
            ],
        ];
        return [
            "title" => "IT资讯精选（{$yesterday}）",
            "data" => $resp
        ];
    }

    function dailyGitHub()
    {
        $info = new InfoqService();
        $github = $info::getLastDayArticleByQuery('source:github');


        $yesterday = date('Y-m-d',strtotime("-1 day"));

        $resp = [
            [
                "title" => "GitHub Trending",
                "data" => $github
            ]
        ];
        return [
            "title" => "GitHub Trending{$yesterday}）",
            "data" => $resp
        ];
    }

    
    public function getTagsAgg(Request $request){
        $author = $request->input("author", "");
        $source = $request->input("source", "");
        $size = $request->input("size", 10);

        $resp = AuthorService::getAuthorTags($author, $size);
        return response()->json($resp);
    }

}
