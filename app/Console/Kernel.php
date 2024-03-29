<?php

namespace App\Console;

use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;

class Kernel extends ConsoleKernel
{
    /**
     * The Artisan commands provided by your application.
     *
     * @var array
     */
    protected $commands = [
        Commands\MysqlToEs::class,
        Commands\EscnToEs::class,
        Commands\EscnWordCloud::class,
        Commands\EsClear::class,
        Commands\EsClearLast::class,
        Commands\EsReindex::class,
        Commands\EsTrans::class,
        Commands\EscnDaily::class,
    ];

    /**
     * Define the application's command schedule.
     *
     * @param  \Illuminate\Console\Scheduling\Schedule  $schedule
     * @return void
     */
    protected function schedule(Schedule $schedule)
    {
        $schedule->command('EscnDaily')->dailyAt('07:00');
        $schedule->command('KrDaily')->dailyAt('07:05');
    }

    /**
     * Register the commands for the application.
     *
     * @return void
     */
    protected function commands()
    {
        $this->load(__DIR__ . '/Commands');

        require base_path('routes/console.php');
    }
}
