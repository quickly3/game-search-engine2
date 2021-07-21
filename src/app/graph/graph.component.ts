import { Component, OnInit } from '@angular/core';
import { GraphService } from '../api/graph.service';
import { Datum } from '../interface/Datum';
import * as json2md from 'json2md';

@Component({
    selector: 'app-graph',
    templateUrl: './graph.component.html',
    styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
    private graphService: GraphService;
    totalData: Datum[] = [];
    lastDayData: Datum[] = [];
    horizontalData: Datum[] = [];
    MdData: any;

    constructor(graphService: GraphService) {
        this.graphService = graphService;
    }

    ngOnInit() {
        this.getTotalData();
        this.getlastDayData();
        this.getDailyMd();
    }

    getTotalData() {
        this.graphService.getTotalGraph().subscribe((data: any) => {
            const totalData = [];
            for (const i of Object.keys(data)) {
                totalData.push({
                    name: i,
                    value: data[i],
                });
            }
            this.totalData = totalData;

            //   const total = pieData.map(i => i.value).reduce((x, y) => x + y);
            //   this.horizontalData = pieData.map(d => {
            //     return {
            //       name: d.name,
            //       value: Math.floor((d.value / total) * 100) / 100
            //     };
            //   });
        });
    }

    getlastDayData() {
        this.graphService.getLastDayData().subscribe((data: any) => {
            const lastDayData = [];
            for (const i of Object.keys(data)) {
                lastDayData.push({
                    name: i,
                    value: data[i],
                });
            }
            this.lastDayData = lastDayData;
        });
    }

    getDailyMd() {
        this.graphService.dailyMd().subscribe((resp: any) => {

            const dd: any[] = [
                {h2: resp.title}
            ];

            for (const item of resp.data){
                if (item.data.length > 0){
                    dd.push({h5: item.title});
                    for (const item2 of item.data){
                        dd.push({
                            link: {
                                title: item2.title,
                                source: item2.url
                            }
                        });
                    }
                }
            }

            this.MdData = json2md(dd);
        });
    }
}
