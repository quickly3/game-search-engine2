<?php

namespace App\Models;

use ScoutElastic\Searchable;
use Illuminate\Database\Eloquent\Model;
use App\EsConfigurator\GameConfigurator;
use DateTime;

class GameModel extends Model
{
    use Searchable;

    /**
     * @var string
     */
    protected $indexConfigurator = GameConfigurator::class;
    protected $table = 'games';

    public function searchableAs()
    {
        return 'games';
    }

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
            "appid" => [
                "type" => "long"
            ],
            "conid" => [
                "type" => "long"
            ],
            "description" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ],
            "soft_requirements" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ],
            "detail_page" => [
                "type" => "keyword"
            ],
            "download_page" => [
                "type" => "keyword"
            ],
            "game_images_mini_string" => [
                "type" => "keyword"
            ],
            "game_images_string" => [
                "type" => "keyword"
            ],
            "game_tags_string" => [
                "type" => "keyword"
            ],
            "game_type" => [
                "type" => "keyword"
            ],
            "id" => [
                "type" => "long"
            ],
            "image_alt" => [
                "type" => "keyword"
            ],
            "image_url" => [
                "type" => "keyword"
            ],
            "inLanguage" => [
                "type" => "keyword"
            ],
            "install_info" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ],
            "license" => [
                "type" => "keyword"
            ],
            "mysql_id" => [
                "type" => "long"
            ],
            "name" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ],
            "name_chs" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ],
            "name_en" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ]
            ],
            "publish_date_by_ali" => [
                "type" => "date"
            ],
            "publisher" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ],
            "size" => [
                "type" => "float"
            ],
            "state" => [
                "type" => "long"
            ],
            "sys_requirements" => [
                "properties" => [
                    "key" => [
                        "type" => "keyword"
                    ],
                    "v1" => [
                        "type" => "text",
                        "fields" => [
                            "keyword" => [
                                "type" => "keyword",
                                "ignore_above" => 256
                            ]
                        ],
                        "analyzer" => "ik_max_word"
                    ],
                    "v2" => [
                        "type" => "text",
                        "fields" => [
                            "keyword" => [
                                "type" => "keyword",
                                "ignore_above" => 256
                            ]
                        ],
                        "analyzer" => "ik_max_word"
                    ]
                ]
            ],
            "try_name" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ]
            ],
            "version" => [
                "type" => "text",
                "fields" => [
                    "keyword" => [
                        "type" => "keyword",
                        "ignore_above" => 256
                    ]
                ],
                "analyzer" => "ik_max_word"
            ]
        ]
    ];

    public function toSearchableArray()
    {
        $data = $this->attributes;

        $data['description'] = trim($data['description']);
        $data['soft_requirements'] = trim($data['soft_requirements']);


        $data['game_tags_string'] = explode(",", $data['game_tags_string']);
        $data['game_images_string'] = explode(",", $data['game_images_string']);
        $data['game_images_mini_string'] = explode(",", $data['game_images_mini_string']);

        $data['sys_requirements'] = json_decode($data['sys_requirements'], true);

        $size_valid = false;

        if (strpos($data['size'], "M") > -1) {
            $data['size'] = str_replace("MB", "", $data['size']);
            $data['size'] = (float) str_replace("M", "", $data['size']);
            $size_valid = true;
        }
        if (strpos($data['size'], "G") > -1) {
            $data['size'] = str_replace("GB", "", $data['size']);
            $data['size'] = (float) str_replace("G", "", $data['size']) * 1000;
            $size_valid = true;
        }

        if (!$size_valid) {
            $data['size'] = 0;
        }

        $data['publish_date_by_ali'] = date(DateTime::ISO8601, strtotime($data['publish_date_by_ali']));

        return $data;
    }
}
