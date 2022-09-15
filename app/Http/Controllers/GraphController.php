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
        $krs = $info::getLastDayArticleByQuery('source:36kr', 50);



        // $yesterday = date('Y-m-d',strtotime("-1 day"));

        $yesterday = date('Y-m-d',strtotime("now"));


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
            [
                "title" => "36氪新闻",
                "data" => $krs
            ],

        ];
        return [
            "title" => "互联网摸鱼日报（{$yesterday}）",
            "data" => $resp
        ];
    }

    function dailyKr()
    {
        $info = new InfoqService();
        $kr = $info::getLastDayArticleByQuery('source:36kr', 50);

        $yesterday = date('Y-m-d',strtotime("-1 day"));

        $resp = [
            [
                "title" => "36Kr 新闻",
                "data" => $kr
            ],
        ];
        return [
            "title" => "36Kr新闻 ({$yesterday}）",
            "data" => $resp
        ];
    }

    function dailyGitHub(Request $request)
    {
        $info = new InfoqService();
        $tags = [];

        $since = $request->input("since", null);
        $lan = $request->input("lan", null);
        $spl = $request->input("spl", null);

        if($since){
            $tags[] = $since;
        }

        if($lan){
            $tags[] = $lan;
        }

        if($spl){
            $tags[] = $spl;
        }

        $query_str = 'source:github';

        if(count($tags) > 0){
            $tags_str = join(' && ', $tags);
            $query_str.=" && tag:({$tags_str})";
        }

        $github = $info::getLastDayArticleByQuery($query_str, 25);

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
