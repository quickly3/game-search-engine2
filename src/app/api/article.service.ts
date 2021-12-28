import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class ArticleService {
    constructor(private http: HttpClient) {}

    getHistogram = (params) => {
        return this.http.post('/article/getHistogram',params);
    }


    getAuthorTermsAgg = (params) => {
        return this.http.post('/article/getAuthorTermsAgg',params);
    }

}
