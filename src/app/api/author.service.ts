import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { map } from 'rxjs/operators';


@Injectable({
    providedIn: 'root'
})
export class AuthorService {
    constructor(private http: HttpClient) {}

    getAuthors = (params) => {
        return this.http.post('/author/getAuthors', params);
    }
}
