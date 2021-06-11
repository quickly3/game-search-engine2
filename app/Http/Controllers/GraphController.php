<?php

namespace App\Http\Controllers;


use App\Services\GraphService;

class GraphController extends Controller
{
    function index(){
        $graph  = new GraphService();
        return $graph->getDailyGraph();
    }
}
