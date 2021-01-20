import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

@Injectable({
    providedIn: "root"
})
export class AuthService {
    constructor(private http: HttpClient) {}

    login = params => {
        return this.http.post("/login", params);
    };
}
