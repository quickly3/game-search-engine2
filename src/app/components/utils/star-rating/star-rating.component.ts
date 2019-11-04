import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";

const MODALS = {};

@Component({
    selector: "app-star-rating",
    templateUrl: "./star-rating.component.html",
    styleUrls: ["./star-rating.component.scss"],
    inputs: ["stars:stars"]
})
export class StarRatingComponent implements OnInit {
    star_objs = [];
    colors = ["#f03c56", "#ffaa76", "#ffc058", "#aed321", "#5ed321"];
    color: string;
    stars: number;
    @Output() private outer = new EventEmitter<any>(true);

    constructor() {}

    ngOnInit() {
        this.star_objs = [];
        for (let i = 0; i < 5; i++) {
            this.star_objs.push({ clicked: false });
        }

        this.toggleStar(this.stars - 1);
    }

    toggleStar(i) {
        let _clicked = false;
        if (i === 0 && !this.star_objs[1].clicked) {
            _clicked = this.star_objs[i].clicked;
        }

        this.star_objs.map(star => {
            star.clicked = false;
        });

        if (i < 0) {
            this.color = this.colors[0];
        } else {
            this.color = !_clicked ? this.colors[i] : this.colors[0];
        }

        for (let index = 0; index <= i; index++) {
            this.star_objs[index].clicked = !_clicked;
        }

        const _stars = this.star_objs.reduce((star_cnt, star) => {
            if (star.clicked) {
                star_cnt += 1;
            }
            return star_cnt;
        }, 0);

        this.stars = _stars;
        this.sendParentStars();
    }

    sendParentStars() {
        this.outer.emit(this.stars); // 广播传递数据给父组件
    }
}
