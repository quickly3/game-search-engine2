import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { NgbModal } from "@ng-bootstrap/ng-bootstrap";

@Component({
    selector: "app-nav",
    templateUrl: "./nav.component.html",
    styleUrls: ["./nav.component.scss"]
})
export class NavComponent implements OnInit {
    navShow = false;
    constructor(public router: Router, private _modalService: NgbModal) {
        this.router = router;
    }

    ngOnInit() {
    }

    toggleNav() {
        this.navShow = !this.navShow;
    }
}
