import {
    Component,
    ViewEncapsulation,
    HostListener,
    ViewChild,
} from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, of, Subject, fromEvent, merge } from 'rxjs';
import { Router, ActivatedRoute } from '@angular/router';

import {
    debounceTime,
    distinctUntilChanged,
    map,
    filter,
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
import {
    faCalendarAlt, faSearch,
    faLink, faTags, faTimes,
    faThumbsUp, faEye,
    faComment, faStar,
    faWrench, faFileAlt,
    faChartBar
} from '@fortawesome/free-solid-svg-icons';

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
    faFileAlt = faFileAlt;
    faChartBar = faChartBar;
    faLink = faLink;
    faThumbsUp = faThumbsUp;
    faComment = faComment;
    faStar = faStar;
    faEye = faEye;
    faTimes = faTimes;
    faTags = faTags;
    faWrench = faWrench;
    articleList: any[] = [];
    totalNumber = 0;
    totalPage = 0;
    took = 0;
    showMore = false;
    searchFailed = false;
    wordsCloud: any;
    InfoqService;
    startDateIsInvalid = false;
    showTitleOnly = false;
    modelChanged = new Subject<string>();
    searchDebounce = new Subject<string>();
    @ViewChild('instance', { static: true }) instance: NgbTypeahead | undefined;
    @ViewChild('tagsTh', { static: true }) tagsTh: NgbTypeahead | undefined;
    @ViewChild('categoriesTh', { static: true }) categoriesTh: NgbTypeahead | undefined;

    tagsFocus$ = new Subject<string>();
    tagsClick$ = new Subject<string>();
    categoriesFocus$ = new Subject<string>();
    categoriesClick$ = new Subject<string>();

    tags: any[] = [];
    updateSta = true;
    tagsI18n;
    sortItems;
    sourceList;
    displayModelItems;
    queryParams;
    displayModel;
    allTags: any[] = [];
    allCategories: any[] = [];

    selectedTags: any[] = [];
    selectedCategories: any[] = [];
    tagInput = '';
    categoryInput = '';

    tagsModalOpened = false;
    categoriesModalOpened = false;

    showOldTags = false;
    hideSearchZone = false;

    defaultTouch = { x: 0, y: 0, time: 0 };

    subNavItems = [
        {
            name:"articles",
            text:"文章",
            icon:faFileAlt,
        },
        {
            name:"charts",
            text:"数据可视化",
            icon:faChartBar,
        }
    ]

    curSubNav = this.subNavItems[0];
    subNavModel = this.curSubNav.name;
    histogramData:any = [];

    public screenWidth: any;
    public screenHeight: any;
    public isMobile = false;

    // tslint:disable-next-line: no-shadowed-variable
    constructor(
        private http: HttpClient,
        InfoqService: InfoqService,
        private route: ActivatedRoute,
        private router: Router

        ) {
        this.InfoqService = InfoqService;

        this.searchDebounce.pipe(debounceTime(300)).subscribe(() => {
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
            this.lastPage();
        }

        if (event.key === 'ArrowRight') {
            this.nextPage();
        }
    }

    // tslint:disable-next-line: use-lifecycle-interface
    ngOnInit(): void {
        this.checkWindowSize();
        this.updateQueryParamsByUrl();
        this.getTags();
        this.getCategories();
    }
    @HostListener('touchstart', ['$event'])
    // @HostListener('touchmove', ['$event'])
    @HostListener('touchend', ['$event'])
    @HostListener('touchcancel', ['$event'])
    handleTouch(event) {
        const touch = event.touches[0] || event.changedTouches[0];

        // check the events
        if (event.type === 'touchstart') {
            this.defaultTouch.x = touch.pageX;
            this.defaultTouch.y = touch.pageY;
            this.defaultTouch.time = event.timeStamp;
        } else if (event.type === 'touchend') {
            const deltaX = touch.pageX - this.defaultTouch.x;
            const deltaY = touch.pageY - this.defaultTouch.y;
            const deltaTime = event.timeStamp - this.defaultTouch.time;

            // simulte a swipe -> less than 500 ms and more than 60 px
            if (deltaTime < 500) {
                // touch movement lasted less than 500 ms
                if (Math.abs(deltaX) > 60) {
                    // delta x is at least 60 pixels
                    if (deltaX > 0) {
                        this.lastPage();
                    } else {
                        this.nextPage();
                    }
                }
            }
        }
    }

    lastPage = () => {
        if (this.queryParams.page !== 1) {
            this.queryParams.page--;
            this.pageChange();
        }
    }

    nextPage = () => {
        if (this.queryParams.page < this.totalPage) {
            this.queryParams.page++;
            this.pageChange();
        }
    }


    checkWindowSize(): void {
        this.screenWidth = window.innerWidth;
        this.screenHeight = window.innerHeight;
        this.isMobile = this.screenWidth < 669;
        if (this.isMobile){
            this.hideSearchZone = true;
        }
    }

    toggleSearchZone(): void {
        this.hideSearchZone = !this.hideSearchZone;
    }

    // tags handle
    searchTags = (text$: Observable<string>) => {
        const debouncedText$ = text$.pipe(debounceTime(200), distinctUntilChanged());
        const clicksWithClosedPopup$ = this.tagsClick$.pipe(filter(() => {
            return !this.tagsTh.isPopupOpen();
        }));
        const inputFocus$ = this.tagsFocus$;

        return merge(debouncedText$, inputFocus$, clicksWithClosedPopup$).pipe(
            map(term => (term === '' ? this.allTags
            : this.allTags.filter(v => v.toLowerCase().indexOf(term.toLowerCase()) > -1)).slice(0, 10))
        );
    }

    selectTag2 = ($e) => {
        $e.preventDefault();
        if (this.queryParams.selectTags.indexOf($e.item) < 0){
            this.queryParams.selectTags.push($e.item);
            this.search();
        }
    }

    removeSelectTag = (tag) => {
        if (this.queryParams.selectTags.indexOf(tag) > -1){
            this.queryParams.selectTags = this.queryParams.selectTags.filter(item => (item !== tag) );
            this.search();
        }
    }

    selectTagsModal = () => {
        this.tagsModalOpened = true;
    }

    tagsModalClosed = ($e) => {
        this.tagsModalOpened = false;
        if ($e){
            this.queryParams.selectTags = $e;
            this.search();
        }
    }


    // categories handle

    searchCategories = (text$: Observable<string>) => {
        const debouncedText$ = text$.pipe(debounceTime(200), distinctUntilChanged());
        const clicksWithClosedPopup$ = this.categoriesClick$.pipe(filter(() => {
            return !this.categoriesTh.isPopupOpen();
        }));
        const inputFocus$ = this.categoriesFocus$;

        return merge(debouncedText$, inputFocus$, clicksWithClosedPopup$).pipe(
            map(term => (term === '' ? this.allCategories
            : this.allCategories.filter(v => v.toLowerCase().indexOf(term.toLowerCase()) > -1)).slice(0, 10))
        );
    }

    selectCategory = ($e) => {
        $e.preventDefault();
        if (this.queryParams.selectCategories.indexOf($e.item) < 0){
            this.queryParams.selectCategories.push($e.item);
            this.search();
        }
    }

    removeSelectCategory = (category) => {
        if (this.queryParams.selectCategories.indexOf(category) > -1){
            this.queryParams.selectCategories = this.queryParams.selectCategories.filter(item => (item !== category) );
            this.search();
        }
    }

    selectCategoriesModal = () => {
        this.categoriesModalOpened = true;
    }

    categoriesModalClosed = ($e) => {
        this.categoriesModalOpened = false;
        if ($e){
            this.queryParams.selectCategories = $e;
            this.search();
        }
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

        if (urlParamsCopy.selectTags){
            urlParamsCopy.selectTags = urlParamsCopy.selectTags.split(',');
        }

        if (urlParamsCopy.selectCategories){
            urlParamsCopy.selectCategories = urlParamsCopy.selectCategories.split(',');
        }

        if (urlParamsCopy.sortBy){
            urlParamsCopy.sortBy = this.sortItems.find(i => i.value === urlParamsCopy.sortBy);
        }

        if (urlParamsCopy.subNavModel){
            this.subNavModel = urlParamsCopy.subNavModel;
            this.curSubNav = this.subNavItems.find(i => i.name === urlParamsCopy.subNavModel);
        }

        this.queryParams = {...initQueryParams, ...urlParamsCopy};
        this.search();

    }

    // tslint:disable-next-line: typedef
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
            sortBy: this.sortItems[0],
            selectTags: [],
            selectCategories: []
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
            source: 'all',
        }).subscribe((tags: any) => {
            let total = 0;
            // tslint:disable-next-line: variable-name
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
            this.allTags = _tags.map(i => i.text);
        });
    }

    getCategories = () => {
        this.InfoqService.getCategories({
            source: 'all',
        }).subscribe((cates: any) => {
            let total = 0;
            // tslint:disable-next-line: variable-name
            const _cates: any[] = cates.map(
                (i: { key: any; doc_count: number }) => {
                    total += i.doc_count;
                    return {
                        text: i.key,
                        count: i.doc_count,
                    };
                }
            );
            this.allCategories = _cates.map(i => i.text);
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

    getQueryParams = (option) => {
        return {
            ...this.queryParams,
            source: this.queryParams.source.title,
            sortBy: this.queryParams.sortBy.value,
            startDate: this.ngbDateToStr(this.queryParams.startDate),
            endDate: this.ngbDateToStr(this.queryParams.endDate),
            updateSta: option.updateSta,
            subNavModel: this.subNavModel
        };
    }

    setQueryParamsToUrl(queryStringParams): void{
        const nativeParams: any  = {};
        for (const param in queryStringParams){
            if (typeof queryStringParams[param] !== 'string' || queryStringParams[param].trim() !== ''){
                switch (param) {
                    case 'updateSta':
                        break;
                    case 'selectTags':
                        if (queryStringParams[param].length > 0){
                            nativeParams[param] = queryStringParams[param].join(',');
                        }
                        break;
                    case 'selectCategories':
                        if (queryStringParams[param].length > 0){
                            nativeParams[param] = queryStringParams[param].join(',');
                        }
                        break;

                    default:
                        nativeParams[param] = queryStringParams[param];
                        break;
                }

            }
        }

        this.router.navigate([], {
            relativeTo: this.route,
            queryParams: nativeParams,
        });

    }

    search = (option = {updateSta: true}) => {

        if(this.curSubNav.name === 'articles' ){
            this.searchArticles(option);
        }

        if(this.curSubNav.name === 'charts' ){
            this.searchCharts(option);
        }

        this.getWordsCloud();
    }

    searchCharts = (option = {updateSta: true}) =>{

        const queryStringParams = this.getQueryParams(option);
        this.setQueryParamsToUrl(queryStringParams);
        this.InfoqService.getArticleHistogram(queryStringParams).subscribe(
            (resp: { [x: string]: any }) => {
                this.histogramData = resp.data;
            }
        );
    }

     searchArticles = (option = {updateSta: true}) =>{

        const queryStringParams = this.getQueryParams(option);
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
                this.totalPage = Math.ceil(this.totalNumber / this.queryParams.row);
                if (this.instance) {
                    this.instance.dismissPopup();
                }

                if (option.updateSta){
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
        // tslint:disable-next-line: variable-name
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
        this.search({updateSta: false});
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
        this.queryParams.author = '';
        this.queryParams.tag = 'all';
        this.queryParams.page = 1;
        this.search();
    }

    keywordSearch(): void {
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

    countModified = ($event, field) => {
        if ((field in this.queryParams) && this.queryParams[field] < 0){
            this.queryParams[field] = null;
        }
        this.searchDebounce.next($event);
    }

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
        // this.searchDebounce.next($event)
    }

    selectSortBy = (sortBy: { value: string; label: string }) => {
        this.queryParams.sortBy = sortBy;
        this.search();
    }

    selectDisplayModel = (displayModel: { value: string; label: string }) => {
        this.displayModel = displayModel;
        this.showTitleOnly = (displayModel.value === 'title');
        this.search();
    }

    subNavChange = (subNav) => {
        if(this.curSubNav.name !== subNav.name){
            this.curSubNav = subNav;
            this.subNavModel = this.curSubNav.name;
            this.search();
        }
    }
}
