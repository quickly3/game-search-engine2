<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Article;

class ArticleController extends Controller
{
    function index(){
    	$articles = Article::get();
    	return view("articles",["articles"=>$articles]);
    }
}
