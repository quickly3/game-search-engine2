import { Component } from '@angular/core';
import { Datum } from '../../../interface/Datum';
import { GraphService } from '../../../api/graph.service';

@Component({
  templateUrl: './source-statistics.component.html',
})
export class SourceStatistics {
  totalData: Datum[] = [];

  constructor(private graphService: GraphService) {}

  radiusFix = (i) => Math.sqrt(i);

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

  ngOnInit() {
    this.getTotalData();
  }
}
