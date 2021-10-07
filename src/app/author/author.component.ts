import {
    Component,
    ViewEncapsulation,
    ViewChild,
    HostListener
} from '@angular/core';
import { AuthorService } from '../api/author.service';
import constList from '../infoq/constList';
import { NgbTypeahead } from '@ng-bootstrap/ng-bootstrap';
import { faSearch, faRssSquare, faBuilding, faUser } from '@fortawesome/free-solid-svg-icons';
import { of } from 'rxjs';

@Component({
    selector: "author",
    templateUrl: './author.component.html',
    styleUrls: ['./author.component.scss', '../infoq/infoq.component.scss'],
    encapsulation: ViewEncapsulation.None,
})
export class AuthorComponent {
    queryParams: any = {};
    authorList = [];
    sourceList = [];
    sortItems = [];
    faSearch = faSearch;
    faRssSquare = faRssSquare;
    faBuilding = faBuilding;
    faUser = faUser;

    totalNumber: number;
    took: number;
    totalPage: number;

    defaultTouch = { x: 0, y: 0, time: 0 };

    @ViewChild('authorTypehead', { static: true }) authorTypehead: NgbTypeahead | undefined;

    constructor(
        private authorService: AuthorService
    ){
        this.sourceList = constList.sourceList;
        this.sortItems = constList.authorSortItems;
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

    ngOnInit(){
        this.getAuhtors();
        this.queryParams = this.getInitQueryParams();
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
            sortBy: this.sortItems[0],
            selectTags: [],
            selectCategories: []
        };
    }

    autoComplete = (text$) => of([]);

    authorSearch = () => {
        this.getAuhtors();
    }

    getAuhtors = () => {
        this.authorService.getAuthors(this.queryParams).subscribe(
            (data: { [x: string]: any }) => {
                this.authorList = data.data.map((user) => {
                    if (user.source === 'juejin'){
                        user.user_url = `https://juejin.cn/user/${user.user_id}`;
                        user.inner_url = `/#/infoq?page=1&row=20&tag=all&source=all&author=${user.user_name}&sortBy=multi`;
                    }
                    return user;
                });
                this.totalNumber = data.total;
                this.took = data.took;
                this.totalPage = Math.ceil(this.totalNumber / this.queryParams.row);
            }
        );
    }

    selectSortBy = (sortBy: { value: string; label: string }) => {
        this.queryParams.sortBy = sortBy;
        this.getAuhtors();
    }

    searchOnKeydown(e: { key: string }) {
        if (e.key === 'Enter') {
            if (this.authorTypehead) {
                this.authorTypehead.dismissPopup();
                this.getAuhtors();
            }
        }
    }

    pageChange = () => {
        this.getAuhtors();
    }

}
