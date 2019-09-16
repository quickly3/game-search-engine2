<?php

namespace App\Models;

use ScoutElastic\Searchable;
use Illuminate\Database\Eloquent\Model;
use App\EsConfigurator\EscnConfigurator;

class EscnModel extends Model
{
    use Searchable;

    /**
     * @var string
     */


    protected $indexConfigurator = EscnConfigurator::class;
    protected $table = 'EsDailyItem';
    /**
     * @var array
     */
    protected $searchRules = [
        //
    ];

    public function searchableAs()
    {
        return 'escn';
    }

    /**
     * @var array
     */
    protected $mapping = [
        "properties" => [
            "id" => [
                "type" => "long"
            ],
            "link" => [
                "type" => "keyword"
            ],
            "pid" => [
                "type" => "long"
            ],
            "state" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ]
            ],
            "title" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word",
                "fielddata" => true
            ]
        ]
    ];

    public function toSearchableArray()
    {
        $data = $this->attributes;
        return $data;
    }
}
