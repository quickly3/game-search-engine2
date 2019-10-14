<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Model\Elastic\ElasticModel;
use Illuminate\Http\Request;
use App\Models\GameModel;

use App\User;

class GameController extends Controller
{

    public function index(Request $request)
    {
        // $index = File::get(public_path() . '/dist/index.html');
        // // $index = str_replace('href="styles','href="/dist/styles',$index);
        // $index = str_replace('href="styles', 'href="/dist/styles', $index);
        // $index = str_replace('src="', 'src="/dist/', $index);

        $user = User::create(["name" => "bean", "email" => "quickly3@sohu.com", "password" => password_hash(123456)]);
        dump($user);
        die();
        return $index;
    }

    public function getList(Request $request)
    {

        $keywords = $request->input("keywords", "");
        $search_type = trim($request->input("search_type", ""));

        $es = new ElasticModel("games", "games");

        if ($search_type == "simple") {
            $data = $es->source(["name", "version"]);

            if (trim($keywords) == "") {
                $keywords = "''";
            }
        } else {
            $data = $es;

            if (trim($keywords) == "") {
                $keywords = "*";
            }
        }

        $orders = [
            "_score" => "desc",
            "publish_date_by_ali" => "desc",
        ];

        $query_string = "name:{$keywords}";

        $data->orderBy($orders);

        $data = $data->query_string($query_string, "*")->paginate(10);

        return response()->json($data);
    }

    public function test(Request $request)
    {
        // $es = new ElasticModel("game", "games");
        $games = GameModel::search('phone')
            // specify columns to select
            ->select(['name'])
            ->from(0)
            ->take(10)
            ->get();

        return response()->json($games);
    }

    public function getGameDataById(Request $request)
    {
        $id = $request->input("id", "");

        $es = new ElasticModel("games", "games");
        $query = ["match_all" => (object) []];
        $query_string = "name:英雄";
        $data = $es->source(["name", "version"])->getById($id, "*");

        return response()->json($data);
    }
}
