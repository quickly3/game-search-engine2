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
}
