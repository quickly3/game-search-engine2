<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
 */

// Route::get('/', function () {
//     $index = File::get(public_path() . '/dist/index.html');
//     // $index = str_replace('href="styles','href="/dist/styles',$index);
//     $index = str_replace('href="styles', 'href="/dist/styles', $index);
//     $index = str_replace('src="', 'src="/dist/', $index);

//     return $index;
// });

Route::get('game/list', 'GameController@getList');
Route::get('game/test', 'GameController@test');
Route::get('game/index', 'GameController@index');

Route::get('game/getGameDataById', 'GameController@getGameDataById');

Route::get('escn/getDailyList', 'EscnController@getDailyList');
Route::get('escn/getWordsCloud', 'EscnController@getWordsCloud');

Route::get('js/getDailyList', 'JianshuController@getDailyList');
Route::get('js/getWordsCloud', 'JianshuController@getWordsCloud');

Route::get('jj/getDailyList', 'JuejinController@getDailyList');
Route::get('jj/getWordsCloud', 'JuejinController@getWordsCloud');
Route::post('jj/starsChange', 'JuejinController@starsChange');

Route::any('infoq/getDailyList', 'InfoqController@getDailyList');
Route::any('infoq/getArticleHistogram', 'InfoqController@getArticleHistogram');
Route::any('infoq/getWordsCloudByQueryBuilder', 'InfoqController@getWordsCloudByQueryBuilder');
Route::any('infoq/getAuthorTermsAgg', 'InfoqController@getAuthorTermsAgg');

Route::get('infoq/getWordsCloud', 'InfoqController@getWordsCloud');
Route::post('infoq/starsChange', 'InfoqController@starsChange');
Route::get('infoq/autoComplete', 'InfoqController@autoComplete');
Route::get('infoq/getTags', 'InfoqController@getTags');
Route::get('infoq/getCategories', 'InfoqController@getCategories');

Route::get('article/index', 'ArticleController@index');
Route::post('article/getHistogram', 'ArticleController@getHistogram');

Route::get('fanju/list', 'FanjuController@getList');
Route::post('movie/getList', 'MovieController@getList');

Route::get('movie/getDetail', 'MovieController@getDetail');
Route::get('movie/autoComplete', 'MovieController@autoComplete');


Route::get('graph/index', 'GraphController@getDailyGraph');
Route::get('graph/getTotalGraph', 'GraphController@getTotalGraph');
Route::get('graph/getLastDayData', 'GraphController@getLastDayData');


Route::get('graph/dailyMd', 'GraphController@dailyMd');
Route::post('graph/getTagsAgg', 'GraphController@getTagsAgg');


Route::post('author/getAuthors', 'AuthorController@getAuthors');



// Route::get('game/test', 'GameController@test');

Auth::routes();
