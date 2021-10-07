<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Model\Elastic\ElasticModel;
use App\Services\AuthorService;
use Illuminate\Http\Request;
use Carbon\Carbon;

class AuthorController extends Controller
{
    public function getAuthors(Request $request){
        $keywords = $request->input("keywords", "");
        $sortBy = $request->input("sortBy", "");
        $size = $request->input("size", 20);


        $es = new ElasticModel("author", "author");

        if ($keywords != '') {
            $query_string = "user_name:\"{$keywords}\" || user_name:*$keywords* ";
        }else{
            $query_string = "*:*";
        }

        $data = $es;

        $highlight = [
            "fields" => [
                "user_name" => (object) [],
            ],
        ];
        $data->size($size)->highlight($highlight);

        if($sortBy !== ""){
            $sortBy = $sortBy['value'];
        }

        switch($sortBy){
            case "power":
                $orders = [
                    "power" => "desc",
                    "_score" => "desc",
                ];
                break;
            case "post_article_count":
                $orders = [
                    "post_article_count" => "desc",
                    "_score" => "desc",
                ];
                break;
            case "level":
                $orders = [
                    "level" => "desc",
                    "_score" => "desc",
                ];
                break;

            default:
                $orders = [
                    "post_article_count" => "desc",
                    "_score" => "desc",
                ];
        }
        $data->orderBy($orders);

        // $data->orderBy($orders);

        try {
            $data = $data->query_string($query_string, "*")->paginate(20);
        } catch (\Throwable $th) {
            $data = ["data"=>[]];
        }
        

        $data['query_string'] = $query_string;
        $data['orderBy'] = $orders;


        return response()->json($data);
    }
}