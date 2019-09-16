<?php

namespace App\EsConfigurator;

use ScoutElastic\IndexConfigurator;
use ScoutElastic\Migratable;

class GameConfigurator extends IndexConfigurator
{
    use Migratable;

    protected $name = 'game';
    /**
     * @var array
     */
    protected $settings = [
        //
    ];
}
