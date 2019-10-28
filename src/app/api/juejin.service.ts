import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn: "root"
})
export class JuejinService {
    constructor(private http: HttpClient) {}

    getWordsCloud = params => {
        return this.http.get("/jj/getWordsCloud", { params });
    };

    searchDatasSimple = params => {
        return this.http.get("/jj/getDailyList", { params });
    };

    getDailyList = params => {
        return this.http.get("/jj/getDailyList", { params });
    };
}
