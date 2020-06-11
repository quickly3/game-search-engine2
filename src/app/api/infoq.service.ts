import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn: "root"
})
export class InfoqService {
    constructor(private http: HttpClient) {}

    getWordsCloud = params => {
        return this.http.get("/infoq/getWordsCloud", { params });
    };

    searchDatasSimple = params => {
        return this.http.post("/infoq/getDailyList", params);
    };

    getDailyList = params => {
        return this.http.post("/infoq/getDailyList", params);
    };

    starsChange = params => {
        return this.http.post("/infoq/starsChange", { params });
    };

    autoComplete = params => {
        return this.http.get("/infoq/autoComplete", { params });
    };

}
