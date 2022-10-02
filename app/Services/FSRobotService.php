<?php

namespace App\Services;

use PhpParser\Node\Stmt\TryCatch;

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
                // $this->show_group_info($v->chat_id);
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
            dump($resp);
            // $open_ids = array_map(function($item){ return $item->open_id; },$resp->data->members);
            // $this->get_user_info($open_ids);
        }
    }


    function get_users_info($open_ids){
        $ids_string =  join("&", array_map(function($item){ return "open_ids={$item}";},$open_ids));

        $users = [];
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
            return $resp->data->user_infos;
        }

        return $users;
    }

    function get_user_info($user_id){

        $method = 'GET';
        $url = "https://open.feishu.cn/open-apis/contact/v3/users/{$user_id}";
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);
        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            return $resp->data->user_infos;
        }

        return false;
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

    function sendToBean($title, $articles){
        $open_id = 'ou_7ba56fd9ecc84f4115ba863607f3d898';
        $contents = [];

        foreach ($articles as $i => $c) {
            $index = $i+1;
            $contents[] = [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> "{$index}. {$c['title']}"
                ]
            ];
            $contents[] = [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> "{$c['url']}"
                ]
            ];
            $contents[] = [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> ""
                ]
            ];
        }

        if(empty($contents)){
            return null;
        }

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

    function sendToGroup($title, $articles, $chat_id = 'oc_59384feeb3ab194bdc0f9f385da7354f'){
        if(!isset($this->chat_id)){
            $this->chat_id = $chat_id;
        }
        $contents = [];

        foreach ($articles as $i => $c) {
            $index = $i+1;
            $contents[] = [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> "{$index}. {$c['title']}"
                ]
            ];
            $contents[] = [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> "{$c['url']}"
                ]
            ];
            $contents[] = [
                [
                    "tag"=> "text",
                    "un_escape"=>true,
                    "text"=> ""
                ]
            ];
        }

        if(empty($contents)){
            return null;
        }

        $body = [
            "chat_id"=>$this->chat_id,
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

    function sendToGroup2($title, $articles, $chat_id = 'oc_59384feeb3ab194bdc0f9f385da7354f'){
        if(!isset($this->chat_id)){
            $this->chat_id = $chat_id;
        }
        $contents = [];

        foreach ($articles as $i => $c) {
            $index = $i+1;
            $contents[] = [
                [
                    "tag"=> "a",
                    "href"=>"{$c['url']}",
                    "text"=> "{$index}. {$c['title']}"
                ]
            ];
        }

        if(empty($contents)){
            return null;
        }

        $body = [
            "chat_id"=>$this->chat_id,
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

    function sendGroupToFeishu($groups, $test = false, $title = '互联网资讯'){
        $contents = [];
        foreach ($groups as $groupTitle => $articles) {
            if(empty($articles)){
                continue;
            }

            $contents[] = [
                [
                    "tag"=> "text",
                    "text"=> "{$groupTitle}."
                ]
            ];

            foreach ($articles as $i => $c) {
                $index = $i+1;
                $contents[] = [
                    [
                        "tag"=> "a",
                        "href"=>"{$c['url']}",
                        "text"=> "{$index}. {$c['title']}"
                    ]
                ];
            }
        }

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "{$title} （{$yesterday}）";
        $body = [
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

        if(!$test){
            $this->chat_id = 'oc_59384feeb3ab194bdc0f9f385da7354f';
            $body['chat_id'] = 'oc_59384feeb3ab194bdc0f9f385da7354f';
        }else{
            $this->open_id = 'ou_7ba56fd9ecc84f4115ba863607f3d898';
            $body['open_id'] = 'ou_7ba56fd9ecc84f4115ba863607f3d898';
        }


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

    function getMessages($chat_id){
        $method = 'GET';
        $beginWeek = mktime(0,0,0,date("m"),date("d")-date("w")+1,date("Y"));
        $url = "https://open.feishu.cn/open-apis/im/v1/messages?container_id_type=chat&container_id={$chat_id}&start_time=${beginWeek}";
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);

        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            return $resp->data->items;
        }
    }

    function fileUpload($file_name){
        $method = 'POST';
        $url = "https://open.feishu.cn/open-apis/im/v1/files";
        $body = [
            "file_type" => 'mp3',
            "file_name" => $file_name,
            // "file" => $file
        ];

        $options = [
            'json'=> $body,
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}",
                "Content-Type"=>"application/octet-stream"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        try {
            $response = $client->request($method,$url,$options);
        } catch (\Throwable $e) {
            dump( $e);
            //throw $th;
        }


        // if($response->getStatusCode() === 200){
        //     $resp = json_decode($response->getBody());
        //     dump($resp['msg']);
        // }
    }

    function getMessagesReadUsers($message_id = 'om_fb381b29d89ce6d27970319756cea36a'){
        $method = 'GET';
        $url = "https://open.feishu.cn/open-apis/im/v1/messages/{$message_id}/read_users?user_id_type=open_id";
        $options = [
            "headers"=>[
                "Authorization"=>"Bearer {$this->app_access_token}"
            ]
        ];

        $client = new \GuzzleHttp\Client();
        $response = $client->request($method,$url,$options);

        if($response->getStatusCode() === 200){
            $resp = json_decode($response->getBody());
            
            $ids = array_map(function($item){
                return $item->user_id;
            }, $resp->data->items);

            $users = $this->get_users_info($ids);
            return array_map(function($user){
                return $user->name;
            },$users);
        }

        return [];
    }
}
