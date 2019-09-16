<?php

namespace App\Models;

use ScoutElastic\Searchable;
use Illuminate\Database\Eloquent\Model;
use App\EsConfigurator\GameConfigurator;

class GameModel extends Model
{
    use Searchable;

    /**
     * @var string
     */
    protected $indexConfigurator = GameConfigurator::class;
    protected $table = 'Game';

    /**
     * @var array
     */
    protected $searchRules = [
        //
    ];

    /**
     * @var array
     */
    protected $mapping = [
        'properties' => [
            "name" => [
                "type" => "keyword"
            ]
        ]
    ];

    public function searchableAs()
    {
        return "game";
    }

    public function toSearchableArray()
    {
        $data = [];
        dump($this);
        die();
        return $data;
    }
}
