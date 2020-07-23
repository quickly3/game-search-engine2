<?php

namespace App\Console\Commands\spider;

use Illuminate\Console\Command;
use App\Model\Elastic\ElasticModel;


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
        $shells = [
            "scrapy crawl escn_new"
        ];

        // 获取当前目录
        print(getcwd());
        // 改变目录
        chdir("scrapy");
        // 获得当前目录
        print(getcwd());

        foreach($shells as $s){
            system($s, $status);
            dump($status);
        }
    }
}
