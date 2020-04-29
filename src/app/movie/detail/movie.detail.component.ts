import { Component, ViewEncapsulation } from "@angular/core";
import { HttpClient } from "@angular/common/http";

import { Observable, of, Subject } from "rxjs";
import {
    debounceTime,
    distinctUntilChanged,
    map,
    switchMap,
    tap,
    catchError
} from "rxjs/operators";
import { MovieService } from 'app/api/movie.service';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: "movie",
    templateUrl: "./movie.detail.component.html",
    styleUrls: ["./movie.detail.component.scss"]
})
export class MovieDetailComponent {
    public list = []; 

    public total_number = 0;
    public current_page = 1;
    public row = 18;
    public keywords = "";
    public id:string;
    public movie:any;

    constructor(
        private http: HttpClient, 
        private movieService: MovieService,
        private route: ActivatedRoute,
        ) {  
            this.id = this.route.snapshot.paramMap.get("id");

    }

    ngOnInit(): void {
        this.getDetailById()
    }

    getDetailById = function(){
        this.movieService.getDetail({id:this.id}).subscribe( data=>{
            this.movie = data;
        })
    }

}
    