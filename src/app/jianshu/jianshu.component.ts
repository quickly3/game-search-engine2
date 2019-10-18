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
import { JianshuService } from "app/api/jianshu.service";

@Component({
    selector: "jianshu",
    templateUrl: "./jianshu.component.html",
    styleUrls: ["./jianshu.component.scss"]
})
export class JianshuComponent {
    escn_list = [];
    total_number = 0;
    current_page = 1;
    row = 10;

    keywords = "";

    words_cloud;
    jianshuService;

    search_by_keywords;
    modelChanged = new Subject<string>();

    constructor(private http: HttpClient, jianshuService: JianshuService) {
        this.jianshuService = jianshuService;

        this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
            this.search();
        });
    }

    ngOnInit(): void {
        this.jianshuService.getWordsCloud().subscribe(words_cloud => {
            this.words_cloud = words_cloud;
        });
        this.search();
    }

    searchKeyDown = function($event) {
        this.search();
    };

    search_debounce = function(ky) {
        this.current_page = 1;
        this.modelChanged.next();
    };

    search = function() {
        let params = {
            page: "" + this.current_page,
            keywords: this.keywords
        };

        this.jianshuService.getDailyList(params).subscribe(data => {
            this.escn_list = data["data"];
            // this.escn_list.map(item=>{item.unfold = false});
            this.total_number = data["total"];
        });
    };

    pageChange = () => {
        this.search();
    };

    wordsCloudToKeyWords = function(word) {
        this.current_page = 1;
        this.keywords = word.key;
        this.search();
    };

    search_typeahead = (text$: Observable<string>) =>
        text$.pipe(
            debounceTime(300),
            tap(),
            switchMap(term =>
                this.searchDatasSimple(term).pipe(
                    tap(),
                    catchError(() => {
                        return of([]);
                    })
                )
            )
        );

    searchDatasSimple = (term: any) => {
        const params = {
            page: "1",
            keywords: term,
            search_type: "simple"
        };
        return this.jianshuService.searchDatasSimple(params).pipe(
            map(response => {
                const titles = response["data"].map(item => item.title);
                return titles;
            })
        );
    };
}
