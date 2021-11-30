import { Component, OnInit } from '@angular/core';
import { GraphService } from '../api/graph.service';
import { Datum } from '../interface/Datum';

@Component({
    selector: 'app-graph',
    templateUrl: './graph.component.html',
    styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
    private graphService: GraphService;
    totalData: Datum[] = [];
    lastDayData: Datum[] = [];
    totalDataFixed: Datum[] = [];
    lastDayDataFixed: Datum[] = [];
    horizontalData: Datum[] = [];
    tagsData: Datum[] = [];
    MdData: any;

    radiusFix = (i) => Math.sqrt(i);

    constructor(graphService: GraphService) {
        this.graphService = graphService;
    }

    ngOnInit() {
        this.getTotalData();
        this.getlastDayData();
        this.getTagsAgg();
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

    getTagsAgg() {
        this.graphService.getTagsAgg({size: 100}).subscribe((data: any) => {
            this.tagsData = data;
        });
    }
}
