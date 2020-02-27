<?php

return [
    'client' => [
        'hosts' => [
            [
                'host' => getenv("ES_HOST"),
                'port' => getenv("ES_PORT"),
                'user' => getenv("ES_USER"),
                'pass' => getenv("ES_PWD")
            ]
        ],
    ],
    'update_mapping' => env('SCOUT_ELASTIC_UPDATE_MAPPING', true),
    'indexer' => env('SCOUT_ELASTIC_INDEXER', 'single'),
    'document_refresh' => env('SCOUT_ELASTIC_DOCUMENT_REFRESH'),
];
