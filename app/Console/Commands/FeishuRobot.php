<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Services\FSRobotService;

class FeishuRobot extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     * @translator laravelacademy.org
     */
    protected $signature = 'FeishuRobot';

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

        $fs_robot = new FSRobotService();
        $fs_robot->set_app_access_token();
        // $fs_robot->show_group_info("oc_59384feeb3ab194bdc0f9f385da7354f");

        $fs_robot->sendUserHtml("ou_7ba56fd9ecc84f4115ba863607f3d898");

    }
}