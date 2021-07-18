<?php

namespace App\Http\Controllers;


use App\Services\GraphService;

class GraphController extends Controller
{
    function getDailyGraph(){
        $graph  = new GraphService();
        return $graph->getDailyGraph();
    }

    function getTotalGraph(){
        $graph  = new GraphService();
        return $graph->getTotalGraph();
    }    
}