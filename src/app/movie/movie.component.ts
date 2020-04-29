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

@Component({
    selector: "movie",
    templateUrl: "./movie.component.html",
    styleUrls: ["./movie.component.scss"]
})
export class MovieComponent {
    public list = []; 

    public total_number = 0;
    public current_page = 1;
    public row = 10;
    public keywords = "";

    modelChanged = new Subject<string>();

    constructor(
        private readonly http: HttpClient, 
        private readonly movieService: MovieService) {  

    }

    ngOnInit(): void {
        this.search()

        this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
            this.search();
        });
    }

    search = function() {
        let params = {
            page: "" + this.current_page,
            keywords: this.keywords,
            tag: this._tag,
            source: this._source
        };

        console.log(params);
        this.movieService.getList(params).subscribe(data=>{
            this.list = data['data'];
            this.total_number = data["total"];
            
        })
    };


    search_debounce = function(ky) {
        this.current_page = 1;
        this.modelChanged.next();
    };

    pageChange = () => {
        this.search();
    };

}
    