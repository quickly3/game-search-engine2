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
import { JuejinService } from "app/api/juejin.service";

@Component({
    selector: "juejin",
    templateUrl: "./juejin.component.html",
    styleUrls: ["./juejin.component.scss"]
})
export class JuejinComponent {
    escn_list = [];
    total_number = 0;
    current_page = 1;
    row = 10;

    keywords = "";
    words_cloud;
    juejinService;
    _tag;

    search_by_keywords;
    modelChanged = new Subject<string>();

    tags = [
        "All",
        "Python",
        "PHP",
        "Javascript",
        "Css",
        "Typescript",
        "Block_chain",
        "Game",
        "Security",
        "Postgresql"
    ];

    constructor(private http: HttpClient, juejinService: JuejinService) {
        this.juejinService = juejinService;

        this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
            this.search();
        });

        this._tag = this.tags[0];
    }

    ngOnInit(): void {
        this.getWordsCloud();
        this.search();
    }
    showValue(item): void {}

    getWordsCloud = function() {
        this.juejinService
            .getWordsCloud({ tag: this._tag })
            .subscribe(words_cloud => {
                this.words_cloud = words_cloud;
            });
    };

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
            keywords: this.keywords,
            tag: this._tag
        };

        this.juejinService.getDailyList(params).subscribe(data => {
            this.escn_list = data["data"];
            this.escn_list.map(item => {
                if (!item.stars) {
                    item.stars = 0;
                }
            });
            // this.escn_list.map(item=>{item.unfold = false});
            this.total_number = data["total"];
        });
    };

    pageChange = () => {
        this.search();
    };

    starsChange = (stars, item) => {
        if (parseInt(item.stars, 10) !== stars) {
            item.stars = stars;
            this.juejinService
                .starsChange({ item: item })
                .subscribe(resp => {});
        }
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

    selectTag = function(tag) {
        this._tag = tag;
        this.keywords = "";
        this.search();
        this.getWordsCloud();
    };

    searchDatasSimple = (term: any) => {
        const params = {
            page: "1",
            keywords: term,
            search_type: "simple"
        };
        return this.juejinService.searchDatasSimple(params).pipe(
            map(response => {
                const titles = response["data"].map(item => item.title);
                return titles;
            })
        );
    };
}
