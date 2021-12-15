<?php

namespace App\Http\Controllers;


use App\Services\ArticleService;
use Illuminate\Http\Request;
use App\Article;

class ArticleController extends Controller
{
    function index(){
        $article  = new ArticleService();
        return $article->getMonthHistogramBySource("infoq");
    }

    function getHistogram(Request $request){
        $query = $request->input("query", "*:*");
        $calendar_interval = $request->input("calendar_interval", "month");

        $article  = new ArticleService();
        return $article->getHistogram($query, $calendar_interval);
    }

}
