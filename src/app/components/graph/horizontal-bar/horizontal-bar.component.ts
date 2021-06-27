import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-horizontal-bar',
    templateUrl: './horizontal-bar.component.html',
    styleUrls: ['./horizontal-bar.component.scss']
})
export default class HorizontalBarComponent implements OnInit {

    ngOnInit(): void {
        console.log('app-horizontal-bar');
    }

}
