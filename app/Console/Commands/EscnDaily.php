<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Model\Elastic\ElasticModel;
use Illuminate\Support\Facades\Log;


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
            "python3 -m scrapy crawl escn_new"
        ];
        chdir("/home/ubuntu/www/ng-blog/scrapy");
        foreach($shells as $s){
            system($s, $status);
            Log::info($status);
        }
    }
}
