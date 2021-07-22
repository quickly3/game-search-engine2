<?php

namespace App\Http\Controllers;

use App\Services\GraphService;
use App\Services\InfoqService;

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

        $yesterday = date('Y-m-d',strtotime("-1 day"));

        $resp = [
            [
                "title" => isset($escn[0])?$escn[0]['summary']:'',
                "data" => $escn
            ],
            [
                "title" => "掘金资讯（{$yesterday}）",
                "data" => $juejin
            ],
            [
                "title" => "InfoQ 热门话题（{$yesterday}）",
                "data" => $infoq
            ],
            [
                "title" => "开源资讯（{$yesterday}）",
                "data" => $oschina
            ]
        ];
        return [
            "title" => "IT资讯（{$yesterday}）",
            "data" => $resp
        ];
    }
}
