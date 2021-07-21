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

        $resp = [
            "escn" => $escn,
            "juejin" => $juejin,
            "infoq" => $infoq
        ];
        return $resp;
    }
}
