<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Services\FSRobotService;
use App\Services\InfoqService;


class EscnDaily extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     * @translator laravelacademy.org
     */
    protected $signature = 'EscnDaily {test?}';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Send drip e-mails to a user';

    /**
     * The drip e-mail service.
     *
     */
    protected $drip;

    /**
     * Create a new command instance.
     *
     */
    public function __construct()
    {
        parent::__construct();
    }

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
        $this->test = $this->argument("test");

        if(!$this->test){
            $test = false;
        }else{
            $test = true;
        }

        $this->project = [];

        $this->sendDailyEscn($test);
        $this->sendDailyInofQ($test);
        $this->sendDailyJueJin($test);
        $this->sendDailyOschina($test);
        $this->sendDailyCnblogs($test);

        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();
        $fs_robot->sendGroupToFeishu($this->project, $this->test);

    }
    
    public function sendDailyEscn($test){
        $info =new InfoqService();
        $articles = $info::getLastDayArticle();
        $group = [];

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        foreach ($articles as $a) {
            if(!isset($group[$a['summary']])){
                $group[$a['summary']] = [$a];
            }else{
                $group[$a['summary']][] = $a;
            }
        }

        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();

        foreach ($group as $title => $articles) {
            $_title = str_replace("({$yesterday}）", '', $title);
            $this->project[$_title] = $articles;
        }
    }


    public function sendDailyJueJin($test){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:juejin && tag:news');

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "掘金资讯";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();

        $this->project[$title] = $articles;
    }

    public function sendDailyInofQ($test){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:infoq');

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "InfoQ 热门话题";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();

        $this->project[$title] = $articles;
    }

    public function sendDailyOschina($test){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:oschina && tag:news');

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "开源资讯";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();

        $this->project[$title] = $articles;
    }

    public function sendDailyCnblogs(){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:cnblogs && tag:news');

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "博客园新闻";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();

        $this->project[$title] = $articles;        
    }

}
