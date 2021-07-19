import { Component, Input, OnInit } from '@angular/core';
import { Datum } from 'src/app/interface/Datum';
import * as d3 from 'd3';

@Component({
    selector: 'app-horizontal-bar',
    templateUrl: './horizontal-bar.component.html',
    styleUrls: ['./horizontal-bar.component.scss']
})
export default class HorizontalBarComponent implements OnInit {

    @Input() data: Datum[] = [];
    private svg: any;

    ngOnInit(): void {
        console.log('app-horizontal-bar');
    }


    private drawPie(): void {

    }
}
