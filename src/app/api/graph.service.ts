import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';


@Injectable({
    providedIn: 'root'
})
export class GraphService {
    constructor(private http: HttpClient) {}

    getTotalGraph = () => {
        return this.http.get('/graph/getTotalGraph');
    }

    getLastDayData = () => {
        return this.http.get('/graph/getLastDayData');
    }
}
