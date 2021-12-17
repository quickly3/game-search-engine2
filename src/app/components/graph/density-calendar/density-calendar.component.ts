import { Component, Input, OnInit } from '@angular/core';
import { Datum } from 'src/app/interface/Datum';
import * as d3 from 'd3';

@Component({
    selector: 'app-density-calendar',
    templateUrl: './density-calendar.component.html',
    styleUrls: ['./density-calendar.component.scss']
})
export default class DensityCalendarComponent implements OnInit {

    @Input() data: Datum[] = [];
    private svg: any;

    ngOnInit(): void {
        console.log('app-horizontal-bar');
    }


    private drawPie(): void {

    }
}
