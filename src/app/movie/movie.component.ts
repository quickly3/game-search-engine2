import { Component, ViewEncapsulation } from "@angular/core";
import { HttpClient } from "@angular/common/http";

import { Observable, of, Subject, from } from "rxjs";
import {
    debounceTime,
    distinctUntilChanged,
    map,
    scan,
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
    public keywords:any;
    public searching = false;
    public searchFailed = false;
    public curType;
    public types = ["movie","series","comic"]

    // modelChanged = new Subject<string>();

    constructor(
        private readonly http: HttpClient, 
        private readonly movieService: MovieService) {  

        this.curType = this.types[0];
    }

    ngOnInit(): void {
        this.search()

        // this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
        //     this.autoComplete();
        // });
    }

    selecType = (cate) => {
        this.curType = cate;
        this.search();
    }

    autoComplete = (text$: Observable<string>) => 
        text$.pipe(
            debounceTime(300),
            distinctUntilChanged(),
            switchMap(term =>
                this.movieService.autoComplete({
                    keywords: this.keywords,
                })
                .pipe(
                    catchError(() => {
                      return of([]);
                    }))
            ),
          )

    search = function() {
        let params = {
            page: "" + this.current_page,
            keywords: this.keywords,
            tag: this._tag,
            source: this._source,
            type: this.curType,
        };

        if(this.searching){
            return false;
        }

        this.searching = true;
        this.movieService.getList(params).subscribe(data=>{
            this.searching = false;

            this.list = data['data'];
            this.total_number = data["total"];
            
        })
    };

    selectItem = function($e){

    }

    search_debounce = function() {
        this.current_page = 1;
        this.modelChanged.next();
    };

    pageChange = () => {
        this.search();
    };

}
    