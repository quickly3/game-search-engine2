import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { map } from 'rxjs/operators';


@Injectable({
    providedIn: 'root'
})
export class InfoqService {
    constructor(private http: HttpClient) {}

    getWordsCloud = (params: { tag: string; source: string; }) => {
        return this.http.get('/infoq/getWordsCloud', { params });
    }

    searchDatasSimple = (params: { page: string; keywords: any; search_type: string; }) => {
        return this.http.post('/infoq/getDailyList', params);
    }

    getTags = (params: { source: string; }) => {
        return this.http.get('/infoq/getTags', {params});
    }

    getCategories = (params: { source: string; }) => {
        return this.http.get('/infoq/getCategories', {params});
    }

    // tslint:disable-next-line: max-line-length
    getDailyList = (params: { page: string; keywords: string; tag: string; source: string; startDate: NgbDateStruct | undefined; endDate: NgbDateStruct | undefined; sortBy: { value: string; label: string; }; }) => {
        return this.http.post('/infoq/getDailyList', params);
    }

    getArticleHistogram = (params: { page: string; keywords: string; tag: string; source: string; startDate: NgbDateStruct | undefined; endDate: NgbDateStruct | undefined; sortBy: { value: string; label: string; }; }) => {
        return this.http.post('/infoq/getArticleHistogram', params);
    }

    starsChange = (params: any) => {
        return this.http.post('/infoq/starsChange', { params });
    }

    autoComplete = (params: { keywords: string; }) => {
        return this.http.get('/infoq/autoComplete', { params });
    }

}
