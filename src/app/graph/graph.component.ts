import { Component, OnInit } from "@angular/core";
import { GraphService } from "../api/graph.service";
import { Datum } from "../interface/Datum";
import * as json2md from "json2md";

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
        this.graphService.dailyMd().subscribe((data: any) => {
            const dd = json2md([
                { h1: "JSON To Markdown" },
                { blockquote: "A JSON to Markdown converter." },
                {
                    img: [
                        {
                            title: "Some image",
                            source: "https://example.com/some-image.png",
                        },
                        {
                            title: "Another image",
                            source: "https://example.com/some-image1.png",
                        },
                        {
                            title: "Yet another image",
                            source: "https://example.com/some-image2.png",
                        },
                    ],
                },
                { h2: "Features" },
                {
                    ul: [
                        "Easy to use",
                        "You can programmatically generate Markdown content",
                        "...",
                    ],
                },
                { h2: "How to contribute" },
                {
                    ol: [
                        "Fork the project",
                        "Create your branch",
                        "Raise a pull request",
                    ],
                },
                { h2: "Code blocks" },
                { p: "Below you can see a code block example." },
                {
                    code: {
                        language: "js",
                        content: [
                            "function sum (a, b) {",
                            "   return a + b",
                            "}",
                            "sum(1, 2)",
                        ],
                    },
                },
            ]);

            this.MdData = dd;
        });
    }
}
