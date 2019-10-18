import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn: "root"
})
export class JianshuService {
    constructor(private http: HttpClient) {}

    getWordsCloud = params => {
        return this.http.get("/js/getWordsCloud", { params });
    };

    searchDatasSimple = params => {
        return this.http.get("/js/getDailyList", { params });
    };

    getDailyList = params => {
        return this.http.get("/js/getDailyList", { params });
    };
}
