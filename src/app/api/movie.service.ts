import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn: "root"
})
export class MovieService {
    constructor(private http: HttpClient) {}

    getWordsCloud = params => {
        return this.http.get("/movie/getWordsCloud", { params });
    };

    searchDatasSimple = params => {
        return this.http.post("/movie/getDailyList", params);
    };

    getList = params => {
        return this.http.post("/movie/getList", params);
    };

    autoComplete = params => {
        return this.http.get("/movie/autoComplete", {params});
    };

    getDetail = params => {
        return this.http.get("/movie/getDetail", {params});
    };
    
    starsChange = params => {
        return this.http.post("/movie/starsChange", { params });
    };
}
