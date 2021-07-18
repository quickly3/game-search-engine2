import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({
    providedIn: 'root'
})
export class GraphService {
    constructor(private http: HttpClient) {}

    getDailyGraph = () => {
        return this.http.get('/graph/getDailyGraph');
    }

    getTotalGraph = () => {
        return this.http.get('/graph/getTotalGraph');
    }

}
