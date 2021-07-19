import { Component, OnInit } from "@angular/core";
import { GraphService } from "../api/graph.service";
import { Datum } from "../interface/Datum";

@Component({
    selector: "app-graph",
    templateUrl: "./graph.component.html",
    styleUrls: ["./graph.component.scss"],
})
export class GraphComponent implements OnInit {
    private graphService: GraphService;
    totalData: Datum[] = [];
    lastDayData: Datum[] = [];
    horizontalData: Datum[] = [];

    constructor(graphService: GraphService) {
        this.graphService = graphService;
    }

    ngOnInit() {
        this.getTotalData();
        this.getlastDayData();
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
}
