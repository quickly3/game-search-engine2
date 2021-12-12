import { Component } from '@angular/core';
import { Datum } from '../../../interface/Datum';
import { GraphService } from '../../../api/graph.service';

@Component({
  templateUrl: './source-statistics-lastday.component.html',
})
export class SourceStatisticsLastDay {
  lastDayData: Datum[] = [];

  constructor(private graphService: GraphService) {}

  ngOnInit() {
    this.getlastDayData();
  }

  radiusFix = (i) => Math.sqrt(i);

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
