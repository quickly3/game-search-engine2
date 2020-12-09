<?php

namespace App\Services;

class FSRobotService 
{
    public function __construct()
    {
        $this->app_id = getenv("FS_APP_ID");
        $this->app_secret = getenv("FS_APP_SECRET");
        $this->app_access_token = getenv("FS_APP_SECRET");

    }

    function set_app_access_token(){
        $body = [
            "app_id"=>$this->app_id,
            "app_secret"=>$this->app_secret
        ];

        $method = 'POST';
        $url = 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/';
        $options = [
            'json'=>$body,
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);

        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            $this->app_access_token = $resp->app_access_token;
        }
    }

    function show_chart_list(){
        $method = 'GET';
        $url = 'https://open.feishu.cn/open-apis/chat/v4/list';
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);

        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            foreach ($resp->data->groups as $k => $v) {
                dump($v->name);
                dump($v->chat_id);
                $this->show_group_info($v->chat_id);
            }
        }
    }


    function show_group_memeber($chat_id){
        $method = 'GET';
        $url = "https://open.feishu.cn/open-apis/chat/v4/members?chat_id={$chat_id}&page_token=0&page_size=10";
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);
        dump($url);
        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            dump($resp);
        }
    }

    function show_group_info($chat_id){
        $method = 'GET';
        $url = "https://open.feishu.cn/open-apis/chat/v4/info?chat_id={$chat_id}";
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);
        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            $open_ids = array_map(function($item){ return $item->open_id; },$resp->data->members);
            $this->get_user_info($open_ids);
        }
    }

    // ou_7ba56fd9ecc84f4115ba863607f3d898
    function get_user_info($open_ids){
        $ids_string =  join(array_map(function($item){ return "open_ids={$item}";},$open_ids),"&");

        $method = 'GET';
        $url = "https://open.feishu.cn/open-apis/contact/v1/user/batch_get?{$ids_string}";
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);
        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            dump($resp);
        }        
    }

    function sendUserHtml($open_id){

        $title = "Elastic日报 第1131期 (2020-12-07)";
        $contents = [
            [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> "1. es对比TiDB"
                ]
            ],
            [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> "http://www.machengyu.net/elasticsearch/2020/03/08/es-tidb.html"
                ],
            ]
        ];

        $body = [
            "open_id"=>$open_id,
            "msg_type"=>"post",
            "content"=>[
                "post"=>[
                    "zh_cn"=>[
                        "title"=>$title,
                        "content"=> $contents
                    ]
                ]
            ]
        ];

        $method = 'POST';
        $url = 'https://open.feishu.cn/open-apis/message/v4/send/';
        $options = [
            'json'=>$body,
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);

        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            dump($resp);
        }  
    }
}