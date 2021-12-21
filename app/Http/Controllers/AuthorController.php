<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Services\AuthorService;

class AuthorController extends Controller
{
    public function getAuthors(Request $request){
        $resp = AuthorService::getAuthors($request);
        return response()->json($resp);
    }
}