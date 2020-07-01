import { Component, ViewEncapsulation, HostListener, ViewChild } from "@angular/core";
import { HttpClient } from "@angular/common/http";

import { Observable, of, Subject, fromEvent } from "rxjs";
import { scan } from "rxjs/operators";

import {
    debounceTime,
    distinctUntilChanged,
    map,
    switchMap,
    tap,
    catchError
} from "rxjs/operators";
import { InfoqService } from "app/api/infoq.service";
import { NgbTypeahead } from '@ng-bootstrap/ng-bootstrap';

@Component({
    selector: "infoq",
    templateUrl: "./infoq.component.html",
    styleUrls: ["./infoq.component.scss"],
    encapsulation: ViewEncapsulation.None
})
export class InfoqComponent {
    escn_list = [];
    total_number = 0;
    total_page = 0;
    current_page = 1;
    row = 20;
    took = 0;

    keywords = "";
    words_cloud;
    InfoqService;
    _tag;
    _source;
    ngbTypeahead;

    search_by_keywords;
    modelChanged = new Subject<string>();
    @ViewChild("instance", {static: true})instance: NgbTypeahead;

    tags = [
        {text: "All", i18n: "全部"},
        {text: "Python", i18n: "Python"},
        {text: "PHP", i18n: "PHP"},
        {text: "Javascript", i18n: "Javascript"},
        {text: "Css", i18n: "Css"},
        {text: "Typescript", i18n: "Typescript"},
        {text: "Node", i18n: "Node"},
        {text: "Game", i18n: "游戏"},
        {text: "Security", i18n: "安全"},
        {text: "Linux", i18n: "Linux"},
        {text: "Postgresql", i18n: "Postgres"},
        // {text: "blockchain", i18n: "区块链"},
        {text: "blockchain", i18n: "区块链"},
        {text: "dp", i18n: "设计模式"},
        {text: "design", i18n: "设计"},
        {text: "opensource", i18n: "开源"},
        {text: "nosql", i18n: "Nosql"},
        {text: "game", i18n: "游戏"},
        {text: "web", i18n: "全部"},
        {text: "algorithm", i18n: "算法"},
        {text: "translate", i18n: "翻译"}
    ];

    source_list = [
        { title: "all", source_class: "icon-all", text: "全部" },
        { title: "jianshu", source_class: "icon-jianshu", text: "简书" },
        { title: "infoq", source_class: "icon-infoq", text: "极客帮" },
        { title: "juejin", source_class: "icon-juejin", text: "掘金" },
        { title: "cnblogs", source_class: "icon-cnblogs", text: "博客园" },
        { title: "csdn", source_class: "icon-csdn", text: "CSDN" },
        { title: "oschina", source_class: "icon-oschina", text: "开源中国" },
        { title: "sf", source_class: "icon-sf", text: "思否" },
        { title: "escn", source_class: "icon-escn", text: "Es中文社区" },
        { title: "elastic", source_class: "icon-elastic", text: "Es官方" }
    ];

    constructor(private http: HttpClient, InfoqService: InfoqService) {
        this.InfoqService = InfoqService;

        this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
            // this.autoComplete();
        });

        this._tag = this.tags[0].text;
        this._source = this.source_list[0];
    }

    @HostListener("window:keydown", ["$event"])
    handleKeyboardEvent(event: KeyboardEvent) { 
        if(event.key === "ArrowLeft"){
            if(this.current_page !== 1){
                this.current_page--;
                this.pageChange();
            }
        }

        if(event.key === "ArrowRight"){
            if(this.current_page < this.total_number){
                this.current_page++;
                this.pageChange();
            }
        }
    }

    ngOnInit(): void {
        this.getWordsCloud();
        this.search();

        // const observable = new Observable(subscriber => {
        //     subscriber.next(1);
        //     subscriber.next(2);
        //     subscriber.next(3);
        //     setTimeout(() => {
        //         subscriber.next(4);
        //         subscriber.complete();
        //     }, 1000);
        // });

        // observable.subscribe({
        //     next(x) {
        //         console.log("got value " + x);
        //     },
        //     error(err) {
        //         console.error("something wrong occurred: " + err);
        //     },
        //     complete() {
        //         console.log("done");
        //     }
        // });
        // console.log("just after subscribe");
    }
    showValue(item): void {}

    searchOnKeydown(e) {
        if (e.key === "Enter") {
            this.instance.dismissPopup();
            this.search();
        }
    }

    getWordsCloud = function() {
        this.InfoqService.getWordsCloud({
            tag: this._tag,
            source: this._source.title
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
            source: this._source.title
        };

        this.InfoqService.getDailyList(params).subscribe(data => {
            this.escn_list = data["data"];
            this.escn_list.map(item => {
                if (!item.stars) {
                    item.stars = 0;

                    for (const i of this.source_list) {
                        if (item.source === i.title) {
                            item.badge_class = i.source_class;
                        }
                    }
                }
            });
            // this.escn_list.map(item=>{item.unfold = false});
            this.total_number = data["total"];
            this.took = data["took"];
            this.total_page = Math.floor(this.total_number / this.row);
            this.instance.dismissPopup();
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
        this.current_page = 1;
        this.search();
        this.getWordsCloud();
    };

    selectSource = function(source) {
        this._source = source;
        this.keywords = "";
        this.current_page = 1;
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

    autoComplete = (text$: Observable<string>) => text$.pipe(
        debounceTime(300),
        switchMap(term =>
            this.InfoqService.autoComplete({
                keywords: term,
            })
        )
    );
}
