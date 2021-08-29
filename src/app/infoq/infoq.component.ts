import {
    Component,
    ViewEncapsulation,
    HostListener,
    ViewChild,
} from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, of, Subject, fromEvent } from 'rxjs';

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

@Component({
    selector: "infoq",
    templateUrl: './infoq.component.html',
    styleUrls: ['./infoq.component.scss'],
    encapsulation: ViewEncapsulation.None,
})
export class InfoqComponent {
    faCalendarAlt = faCalendarAlt;
    faSearch = faSearch;

    escn_list: any[] = [];
    total_number = 0;
    total_page = 0;
    current_page = 1;
    row = 20;
    took = 0;
    show_more = false;
    searchFailed = false;
    keywords = '';
    words_cloud: any;
    InfoqService;
    _tag = 'all';
    _source;
    startDate: NgbDateStruct | undefined;
    endDate: NgbDateStruct | undefined;
    startDateIsInvalid = false;
    author = '';

    searchByKeywords: any;
    modelChanged = new Subject<string>();
    authorChangedDebounce = new Subject<string>();
    @ViewChild('instance', { static: true }) instance: NgbTypeahead | undefined;

    tags: any[] = [];

    tagsI18n = [
        { text: 'All', i18n: '全部' },
        { text: 'Python', i18n: 'Python' },
        { text: 'PHP', i18n: 'PHP' },
        { text: 'Javascript', i18n: 'Javascript' },
        { text: 'Css', i18n: 'Css' },
        { text: 'Typescript', i18n: 'Typescript' },
        { text: 'Node', i18n: 'Node' },
        { text: 'Game', i18n: '游戏' },
        { text: 'Security', i18n: '安全' },
        { text: 'Linux', i18n: 'Linux' },
        { text: 'Postgresql', i18n: 'Postgres' },
        // {text: "blockchain", i18n: "区块链"},
        { text: 'blockchain', i18n: '区块链' },
        { text: 'dp', i18n: '设计模式' },
        { text: 'design', i18n: '设计' },
        { text: 'opensource', i18n: '开源' },
        { text: 'nosql', i18n: 'Nosql' },
        { text: 'game', i18n: '游戏' },
        { text: 'web', i18n: '网页开发' },
        { text: 'algorithm', i18n: '算法' },
        { text: 'translate', i18n: '翻译' },
    ];

    sortItems = [
        { value: 'multi', label: '综合' },
        { value: 'date', label: '日期' },
        { value: 'score', label: '搜索相关度' },
    ];

    sortBy = this.sortItems[0];

    displayModelItems = [
        { value: 'summary', label: '简介模式' },
        { value: 'title', label: '标题模式' },
    ];

    displayModel = this.displayModelItems[0];

    sourceList = [
        { title: 'all', source_class: 'icon-all', text: '全部' },
        { title: 'jianshu', source_class: 'icon-jianshu', text: '简书' },
        { title: 'infoq', source_class: 'icon-infoq', text: '极客帮' },
        { title: 'juejin', source_class: 'icon-juejin', text: '掘金' },
        { title: 'cnblogs', source_class: 'icon-cnblogs', text: '博客园' },
        { title: 'csdn', source_class: 'icon-csdn', text: 'CSDN' },
        { title: 'oschina', source_class: 'icon-oschina', text: '开源中国' },
        { title: 'sf', source_class: 'icon-sf', text: '思否' },
        { title: 'escn', source_class: 'icon-escn', text: 'Es中文社区' },
        { title: 'elastic', source_class: 'icon-elastic', text: 'Es官方' },
        { title: 'itpub', source_class: 'icon-itpub', text: 'itpub' },
        {
            title: 'data_whale',
            source_class: 'icon-datawhale',
            text: '和鲸数据',
        },
        {
            title: 'ali_dev',
            source_class: 'icon-alidev',
            text: '阿里开发者社区',
        },
    ];

    // tslint:disable-next-line: no-shadowed-variable
    constructor(private http: HttpClient, InfoqService: InfoqService) {
        this.InfoqService = InfoqService;

        this.modelChanged.pipe(debounceTime(300)).subscribe(() => {
            // this.autoComplete();
        });

        this.authorChangedDebounce.pipe(debounceTime(300)).subscribe(() => {
            this.search();
        });

        // this._tag = this.tags[0].text;
        this._source = this.sourceList[0];
    }

    @HostListener('window:keydown', ['$event'])
    // tslint:disable-next-line: typedef
    handleKeyboardEvent(event: KeyboardEvent) {
        if (event.key === 'ArrowLeft') {
            if (this.current_page !== 1) {
                this.current_page--;
                this.pageChange();
            }
        }

        if (event.key === 'ArrowRight') {
            if (this.current_page < this.total_number) {
                this.current_page++;
                this.pageChange();
            }
        }
    }

    ngOnInit(): void {
        this.getWordsCloud();
        this.getTags();
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
    showValue(item: any): void {}

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
            tag: this._tag,
            source: this._source.title,
        }).subscribe((wordsCloud: any) => {
            this.words_cloud = wordsCloud;
        });
    }

    getTags = () => {
        this.InfoqService.getTags({
            source: this._source.title,
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
            this._tag = this.tags[0].text;
        });
    }

    searchKeyDown = ($event: any) => {
        this.search();
    }

    authorChanged = ($event: any) => {
        // this.authorChangedDebounce.next($event)
    }

    search_debounce = (ky: any) => {
        this.current_page = 1;
        this.modelChanged.next();
    }

    search = () => {
        const params = {
            page: '' + this.current_page,
            keywords: this.keywords,
            tag: this._tag,
            source: this._source.title,
            startDate: this.startDate,
            endDate: this.endDate,
            sortBy: this.sortBy,
            author: this.author,
            displayModel: this.displayModel,
        };

        if (this.startDate && this.startDate.year) {
            // params.startDate = (new Date(this.startDate.year, this.startDate.month - 1, this.startDate.day)).toISOString();
        }

        if (this.endDate && this.endDate.year) {
            // params.endDate = (new Date(this.endDate.year, this.endDate.month - 1, this.endDate.day+1)).toISOString();
        }

        this.InfoqService.getDailyList(params).subscribe(
            (data: { [x: string]: any }) => {
                this.escn_list = data.data;
                this.escn_list.map(
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
                // this.escn_list.map(item=>{item.unfold = false});
                this.total_number = data.total;
                this.took = data.took;
                this.total_page = Math.floor(this.total_number / this.row);
                if (this.instance) {
                    this.instance.dismissPopup();
                }
            }
        );
    }

    pageChange = () => {
        this.search();
    }

    wordsCloudToKeyWords = (word: { key: any }) => {
        this.current_page = 1;
        this.keywords = word.key;
        this.search();
    }

    search_typeahead = (text$: Observable<string>) =>
        text$.pipe(
            debounceTime(300),
            tap(),
            switchMap((term) =>
                this.searchDatasSimple(term).pipe(
                    tap(),
                    catchError(() => {
                        return of([]);
                    })
                )
            )
        )

    selectTag = (tag: any) => {
        this._tag = tag;
        // this.keywords = "";
        this.current_page = 1;
        this.search();
        this.getWordsCloud();
    }

    selectSource = (source: any) => {
        this._source = source;
        this._tag = 'all';
        // this.keywords = "";
        this.current_page = 1;
        this.search();
        this.getWordsCloud();
        this.getTags();
    }

    keywordSearch() {
        this.current_page = 1;
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

        if (this.startDate && this.startDate.year) {
            startDate = new NgbDate(
                this.startDate.year,
                this.startDate.month,
                this.startDate.day
            );
        }

        if (this.endDate && this.endDate.year) {
            endDate = new NgbDate(
                this.endDate.year,
                this.endDate.month,
                this.endDate.day
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
            this.startDate = {
                year: today.year(),
                month: today.month() + 1,
                day: today.date(),
            };
            this.endDate = {
                year: tomorrow.year(),
                month: tomorrow.month() + 1,
                day: tomorrow.date(),
            };
        }

        if (date === 'yesterday') {
            this.startDate = {
                year: yesterday.year(),
                month: yesterday.month() + 1,
                day: yesterday.date(),
            };
            this.endDate = {
                year: today.year(),
                month: today.month() + 1,
                day: today.date(),
            };
        }

        if (date === 'week') {
            this.startDate = {
                year: ago7day.year(),
                month: ago7day.month() + 1,
                day: ago7day.date(),
            };
            this.endDate = {
                year: tomorrow.year(),
                month: tomorrow.month() + 1,
                day: tomorrow.date(),
            };
        }
    }

    selectSortBy = (sortBy: { value: string; label: string }) => {
        this.sortBy = sortBy;
        this.search();
    }

    selectDisplayModel = (displayModel: { value: string; label: string }) => {
        this.displayModel = displayModel;
        this.search();
    }
}
