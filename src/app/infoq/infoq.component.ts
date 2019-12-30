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
    _source;

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
        "Block_chain",
        "blockchain",
        "dp",
        "design",
        "opensource",
        "nosql",
        "gamedev",
        "web",
        "algorithm",
        "translate"
    ];

    // source_badge = {
    //     jianshu: "badge-primary",
    //     infoq: "badge-success",
    //     juejin: "badge-info",
    //     cnblogs: "badge-danger",
    //     csdn: "badge-warning"
    // };

    source_list = [
        { title: "all", source_class: "icon-all" },
        { title: "jianshu", source_class: "icon-jianshu" },
        { title: "infoq", source_class: "icon-infoq" },
        { title: "juejin", source_class: "icon-juejin" },
        { title: "cnblogs", source_class: "icon-cnblogs" },
        { title: "csdn", source_class: "icon-csdn" },
        { title: "oschina", source_class: "icon-oschina" },
        { title: "sf", source_class: "icon-sf" },
        { title: "escn", source_class: "icon-escn" }
    ];

    constructor(private http: HttpClient, InfoqService: InfoqService) {
        this.InfoqService = InfoqService;

        this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
            this.search();
        });

        this._tag = this.tags[0];
        this._source = this.source_list[0].title;
    }

    ngOnInit(): void {
        this.getWordsCloud();
        this.search();
    }
    showValue(item): void {}

    getWordsCloud = function() {
        this.InfoqService.getWordsCloud({
            tag: this._tag,
            source: this._source
        }).subscribe(words_cloud => {
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
            tag: this._tag,
            source: this._source
        };

        this.InfoqService.getDailyList(params).subscribe(data => {
            this.escn_list = data["data"];
            this.escn_list.map(item => {
                if (!item.stars) {
                    item.stars = 0;

                    for (const i of this.source_list) {
                        if (item.source == i.title) {
                            item.badge_class = i.source_class;
                        }
                    }
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

    selectSource = function(source) {
        this._source = source.title;
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
