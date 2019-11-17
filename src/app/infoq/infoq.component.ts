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
import { InfoqService } from "app/api/infoq.service";

@Component({
    selector: "infoq",
    templateUrl: "./infoq.component.html",
    styleUrls: ["./infoq.component.scss"],
    encapsulation: ViewEncapsulation.None
})
export class InfoqComponent {
    escn_list = [];
    total_number = 0;
    current_page = 1;
    row = 10;

    keywords = "";
    words_cloud;
    InfoqService;
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
        "Node",
        "Game",
        "Security",
        "Linux",
        "Postgresql",
        "Block_chain"
    ];

    constructor(private http: HttpClient, InfoqService: InfoqService) {
        this.InfoqService = InfoqService;

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
        this.InfoqService.getWordsCloud({ tag: this._tag }).subscribe(
            words_cloud => {
                this.words_cloud = words_cloud;
            }
        );
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

        this.InfoqService.getDailyList(params).subscribe(data => {
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
            this.InfoqService.starsChange({ item: item }).subscribe(resp => {});
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
        return this.InfoqService.searchDatasSimple(params).pipe(
            map(response => {
                const titles = response["data"].map(item => item.title);
                return titles;
            })
        );
    };
}