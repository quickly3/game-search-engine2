<?php

namespace App\EsConfigurator;

use ScoutElastic\IndexConfigurator;
use ScoutElastic\Migratable;

class GameConfigurator extends IndexConfigurator
{
    use Migratable;

    protected $name = 'games';
    /**
     * @var array
     */
    protected $settings = [
        //
    ];
}
