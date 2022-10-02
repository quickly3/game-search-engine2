<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Services\FSRobotService;
use App\Services\InfoqService;


class KrDaily extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     * @translator laravelacademy.org
     */
    protected $signature = 'KrDaily {test?}';

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

        $this->sendDailyKr($test);

        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();
        $fs_robot->sendGroupToFeishu($this->project, $this->test);

    }
    
    public function sendDailyKr($test){
        $info = new InfoqService();
        $articles = $info::getLastDayArticleByQuery('source:36kr',50);

        $yesterday = date('Y-m-d',strtotime("-1 day"));
        $title = "36Kr新闻";
        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();

        $this->project[$title] = $articles;
    }
}
