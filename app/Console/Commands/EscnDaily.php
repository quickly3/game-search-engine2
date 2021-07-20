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
    protected $signature = 'EscnDaily';

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
        $this->sendDailyInofQ();
        sleep(3);
        $this->sendDailyEscn();
        sleep(3);
        $this->sendDailyJueJin();
    }

    public function sendDailyEscn(){
        $info =new InfoqService();
        $articles = $info::getLastDayArticle();
        $group = [];
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
            $fs_robot->sendToGroup2($title, $articles);
            // $fs_robot->sendToBean($title, $articles);
        }
    }


    public function sendDailyJueJin(){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:juejin && tag:news');

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "掘金资讯（{$yesterday}）";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();
        // dump($articles);
        $fs_robot->sendToGroup2($title, $articles);
        // $fs_robot->sendToBean($title, $articles);
    }

    public function sendDailyInofQ(){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:infoq');

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "InfoQ 热门话题（{$yesterday}）";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();
        $fs_robot->sendToGroup2($title, $articles);
        // $fs_robot->sendToBean($title, $articles);
    }

}
