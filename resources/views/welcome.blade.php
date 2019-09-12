@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="card">
            <div class="card-header">
                Articles <small>({{ $articles->count() }})</small>
            </div>
            <div class="card-body">
                @forelse ($articles as $article)
                    <article class="mb-3">
                        <h2>{{ $article->title }}</h2>

                        <p class="m-0">{{ $article->body }}</body>

                        <div>
                            @foreach ($article->tags as $tag)
                                <span class="badge badge-light">{{ $tag}}</span>
                            @endforeach
                        </div>
                    </article>
                @empty
                    <p>No articles found</p>
                @endforelse
            </div>
        </div>
    </div>
@stop