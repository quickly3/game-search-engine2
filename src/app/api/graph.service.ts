import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({
    providedIn: 'root'
})
export class GraphService {
    constructor(private http: HttpClient) {}

    getWordsCloud = () => {
        return this.http.get('/graph/index');
    }
}
