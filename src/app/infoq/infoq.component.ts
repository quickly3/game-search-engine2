import {
    Component,
    ViewEncapsulation,
    HostListener,
    ViewChild,
} from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, of, Subject, fromEvent } from 'rxjs';
import { Router, ActivatedRoute } from '@angular/router';

import {
    debounceTime,
    distinctUntilChanged,
    map,
    switchMap,
    tap,
    catchError,
} from 'rxjs/operators';
import { InfoqService } from '../api/infoq.service';
import {
    NgbDate,
    NgbDateStruct,
    NgbTypeahead,
} from '@ng-bootstrap/ng-bootstrap';
import * as moment from 'moment-timezone';
import { faCalendarAlt, faSearch } from '@fortawesome/free-solid-svg-icons';
import constList from './constList';

@Component({
    selector: "infoq",
    templateUrl: './infoq.component.html',
    styleUrls: ['./infoq.component.scss'],
    encapsulation: ViewEncapsulation.None,
})
export class InfoqComponent {
    faCalendarAlt = faCalendarAlt;
    faSearch = faSearch;
    articleList: any[] = [];
    totalNumber = 0;
    totalPage = 0;
    took = 0;
    showMore = false;
    searchFailed = false;
    wordsCloud: any;
    InfoqService;
    startDateIsInvalid = false;
    modelChanged = new Subject<string>();
    authorChangedDebounce = new Subject<string>();
    @ViewChild('instance', { static: true }) instance: NgbTypeahead | undefined;
    tags: any[] = [];
    updateSta = true;
    tagsI18n;
    sortItems;
    sourceList;
    displayModelItems;
    queryParams;
    displayModel;

    // tslint:disable-next-line: no-shadowed-variable
    constructor(
        private http: HttpClient,
        InfoqService: InfoqService,
        private route: ActivatedRoute,
        private router: Router

        ) {
        this.InfoqService = InfoqService;

        this.authorChangedDebounce.pipe(debounceTime(300)).subscribe(() => {
            this.search();
        });

        this.tagsI18n = constList.tagsI18n;
        this.sortItems = constList.sortItems;
        this.sourceList = constList.sourceList;
        this.displayModelItems = constList.displayModelItems;
        this.displayModel = this.displayModelItems[0];
    }

    @HostListener('window:keydown', ['$event'])
    // tslint:disable-next-line: typedef
    handleKeyboardEvent(event: KeyboardEvent) {
        if (event.key === 'ArrowLeft') {
            if (this.queryParams.page !== 1) {
                this.queryParams.page--;
                this.pageChange();
            }
        }

        if (event.key === 'ArrowRight') {
            if (this.queryParams.page < this.totalNumber) {
                this.queryParams.page++;
                this.pageChange();
            }
        }
    }

    // tslint:disable-next-line: use-lifecycle-interface
    ngOnInit(): void {
        // console.log('ngOnInit');
        this.updateQueryParamsByUrl();
    }

    updateQueryParamsByUrl(): void{
        const initQueryParams = this.getInitQueryParams();
        const urlParams = this.route.snapshot.queryParams;
        const urlParamsCopy = {...urlParams};

        if (urlParamsCopy.page){
            // tslint:disable-next-line: radix
            urlParamsCopy.page = parseInt( urlParamsCopy.page);
        }

        if (urlParamsCopy.row){
            // tslint:disable-next-line: radix
            urlParamsCopy.row = parseInt( urlParamsCopy.row);
        }

        if (urlParamsCopy.startDate){
            urlParamsCopy.startDate = this.strToNgbDate(urlParamsCopy.startDate);
        }

        if (urlParamsCopy.endDate){
            urlParamsCopy.endDate = this.strToNgbDate(urlParamsCopy.endDate);
        }

        if (urlParamsCopy.source){
            urlParamsCopy.source = this.sourceList.find(i => i.title === urlParamsCopy.source);
        }

        if (urlParamsCopy.sortBy){
            urlParamsCopy.sortBy = this.sortItems.find(i => i.value === urlParamsCopy.sortBy);
        }

        console.log('urlParamsCopy', urlParamsCopy);
        this.queryParams = {...initQueryParams, ...urlParamsCopy};
        console.log('queryParams', this.queryParams);
        this.search();

    }

    getInitQueryParams() {
        return {
            page: 1,
            row: 20,
            keywords: '',
            tag: 'all',
            source: this.sourceList[0],
            startDate: '',
            endDate: '',
            author: '',
            sortBy: this.sortItems[0]
        };
    }

    // tslint:disable-next-line: typedef
    searchOnKeydown(e: { key: string }) {
        if (e.key === 'Enter') {
            if (this.instance) {
                this.instance.dismissPopup();
                this.search();
            }
        }
    }

    getWordsCloud = () => {
        this.InfoqService.getWordsCloud({
            tag: this.queryParams.tag,
            source: this.queryParams.source.title,
        }).subscribe((wordsCloud: any) => {
            this.wordsCloud = wordsCloud;
        });
    }

    getTags = () => {
        this.InfoqService.getTags({
            source: this.queryParams.source.title,
        }).subscribe((tags: any) => {
            let total = 0;
            const _tags: any[] = tags.map(
                (i: { key: any; doc_count: number }) => {
                    const matchedItem = this.tagsI18n.find(
                        (item: { text: any }) => {
                            return item.text == i.key;
                        }
                    );
                    total += i.doc_count;
                    return {
                        text: i.key,
                        count: i.doc_count,
                        i18n: matchedItem ? matchedItem.i18n : i.key,
                    };
                }
            );

            this.tags = _tags;
            this.tags.unshift({ text: 'all', i18n: '全部', count: total });
            this.queryParams.tag = this.tags[0].text;
        });
    }

    searchKeyDown = ($event: any) => {
        this.search();
    }

    initSearch = () => {
        this.queryParams = this.getInitQueryParams();
        this.search();
    }

    // search_debounce = (ky: any): void => {
    //     this.queryParams.page = 1;
    //     this.modelChanged.next();
    // }

    ngbDateToStr = (ngbDate): string => {
        if (!ngbDate){
            return '';
        }
        const jsDate = new Date(ngbDate.year, ngbDate.month - 1, ngbDate.day);
        return jsDate.toISOString();
    }

    strToNgbDate = (str) => {
        const date = new Date(str);
        const ngbDateStruct = { day: date.getDate(), month: date.getMonth() + 1, year: date.getFullYear()};
        return ngbDateStruct;
    }

    getQueryParams = () => {
        return {
            ...this.queryParams,
            source: this.queryParams.source.title,
            sortBy: this.queryParams.sortBy.value,
            startDate: this.ngbDateToStr(this.queryParams.startDate),
            endDate: this.ngbDateToStr(this.queryParams.endDate),
            updateSta: this.updateSta
        };
    }

    setQueryParamsToUrl(queryStringParams): void{
        const nativeParams: any  = {};
        for (const param in queryStringParams){
            if (typeof queryStringParams[param] !== 'string' || queryStringParams[param].trim() !== ''){
                if (param === 'updateSta'){
                    continue;
                }
                nativeParams[param] = queryStringParams[param];
            }
        }

        this.router.navigate([], {
            relativeTo: this.route,
            queryParams: nativeParams,
            queryParamsHandling: 'merge',
        });

    }

    search = () => {
        const queryStringParams = this.getQueryParams();
        this.setQueryParamsToUrl(queryStringParams);

        this.InfoqService.getDailyList(queryStringParams).subscribe(
            (data: { [x: string]: any }) => {
                this.articleList = data.data;
                this.articleList.map(
                    (item: {
                        stars: number;
                        source: any;
                        badge_class: any;
                        tag: any[];
                    }) => {
                        if (!item.stars) {
                            item.stars = 0;

                            for (const i of this.sourceList) {
                                if (item.source === i.title) {
                                    item.badge_class = i.source_class;
                                }
                            }
                        }
                        if (!Array.isArray(item.tag)) {
                            item.tag = [item.tag];
                        }
                    }
                );
                this.totalNumber = data.total;
                this.took = data.took;
                this.totalPage = Math.floor(this.totalNumber / this.queryParams.row);
                if (this.instance) {
                    this.instance.dismissPopup();
                }

                if (this.updateSta){
                    if (data.tags){
                        this.handleTags(data.tags);
                    }

                    if (data.wordsCloud){
                        this.wordsCloud = data.wordsCloud;
                    }
                }
            }
        );
    }

    handleTags = (tags) => {
        let total = 0;
        const _tags: any[] = tags.map(
            (i: { key: any; doc_count: number }) => {
                const matchedItem = this.tagsI18n.find(
                    (item: { text: any }) => {
                        return item.text === i.key;
                    }
                );
                total += i.doc_count;
                return {
                    text: i.key,
                    count: i.doc_count,
                    i18n: matchedItem ? matchedItem.i18n : i.key,
                };
            }
        );

        this.tags = _tags;
        this.tags.unshift({ text: 'all', i18n: '全部', count: total });

        // this.queryParams.tag = this.tags[0].text;
    }

    pageChange = () => {
        this.updateSta = false;
        this.search();
    }

    wordsCloudToKeyWords = (word: { key: any }) => {
        this.queryParams.page = 1;
        this.queryParams.keywords = word.key;
        this.search();
    }

    searchByAuthorName = (author) => {
        this.queryParams.page = 1;
        this.queryParams.author = author;
        this.search();
    }

    selectTag = (tag: any) => {
        this.queryParams.tag = tag;
        this.queryParams.page = 1;
        this.search();
    }

    selectSource = (source: any) => {
        this.queryParams.source = source;
        this.queryParams.tag = 'all';
        this.queryParams.page = 1;
        this.search();
    }

    keywordSearch() {
        this.queryParams.page = 1;
        this.search();
    }

    searchDatasSimple = (term: any) => {
        const params = {
            page: '1',
            keywords: term,
            search_type: 'simple',
        };
        return this.InfoqService.searchDatasSimple(params).pipe(
            map((response: any) => {
                const titles = response.data.map(
                    (item: { title: any }) => item.title
                );
                return titles;
            })
        );
    }

    autoComplete = (text$) =>
        text$.pipe(
            debounceTime(300),
            switchMap((term: any) =>
                this.InfoqService.autoComplete({
                    keywords: term,
                }).pipe(
                    map((resp: any) => resp),
                    tap(() => (this.searchFailed = false)),
                    catchError(() => {
                        this.searchFailed = true;
                        return of([]);
                    })
                )
            )
        )

    dateSelected = ($event: any) => {
        let startDate = null;
        let endDate = null;

        if (this.queryParams.startDate && this.queryParams.startDate.year) {
            startDate = new NgbDate(
                this.queryParams.startDate.year,
                this.queryParams.startDate.month,
                this.queryParams.startDate.day
            );
        }

        if (this.queryParams.endDate && this.queryParams.endDate.year) {
            endDate = new NgbDate(
                this.queryParams.endDate.year,
                this.queryParams.endDate.month,
                this.queryParams.endDate.day
            );
        }

        if (endDate && startDate) {
            if (startDate.after(endDate)) {
            }
        }
    }

    toDate = (date: string) => {
        const today = moment();
        const tomorrow = moment().add(1, 'days');
        const yesterday = moment().subtract(1, 'd');
        const ago7day = moment().subtract(7, 'd');

        if (date === 'today') {
            this.queryParams.startDate = {
                year: today.year(),
                month: today.month() + 1,
                day: today.date(),
            };
            this.queryParams.endDate = {
                year: tomorrow.year(),
                month: tomorrow.month() + 1,
                day: tomorrow.date(),
            };
        }

        if (date === 'yesterday') {
            this.queryParams.startDate = {
                year: yesterday.year(),
                month: yesterday.month() + 1,
                day: yesterday.date(),
            };
            this.queryParams.endDate = {
                year: today.year(),
                month: today.month() + 1,
                day: today.date(),
            };
        }

        if (date === 'week') {
            this.queryParams.startDate = {
                year: ago7day.year(),
                month: ago7day.month() + 1,
                day: ago7day.date(),
            };
            this.queryParams.endDate = {
                year: tomorrow.year(),
                month: tomorrow.month() + 1,
                day: tomorrow.date(),
            };
        }
    }

    authorChanged = ($event: any) => {
        // this.authorChangedDebounce.next($event)
    }

    selectSortBy = (sortBy: { value: string; label: string }) => {
        this.queryParams.sortBy = sortBy;
        this.search();
    }

    selectDisplayModel = (displayModel: { value: string; label: string }) => {
        this.displayModel = displayModel;
        this.search();
    }
}
