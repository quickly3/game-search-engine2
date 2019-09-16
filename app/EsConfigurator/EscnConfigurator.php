<?php

namespace App\EsConfigurator;

use ScoutElastic\IndexConfigurator;
use ScoutElastic\Migratable;

class EscnConfigurator extends IndexConfigurator
{
    use Migratable;


    protected $name = 'escn';
    /**
     * @var array
     */
    protected $settings = [
        //
    ];
}
