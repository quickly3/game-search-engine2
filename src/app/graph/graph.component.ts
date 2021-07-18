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
  pieData: Datum[] = [];
  horizontalData: Datum[] = [];

  constructor(graphService: GraphService) {
    this.graphService = graphService;
  }

  async ngOnInit(): Promise<void> {
    this.graphService
    .getTotalGraph()
    .subscribe((data: any) => {
      const pieData = [];
      for (const i of Object.keys(data)){
        pieData.push({
            name: i,
            value: data[i]
        });
      }
      this.pieData = pieData;

      const total = pieData.map(i => i.value).reduce((x, y) => x + y);

      this.horizontalData = pieData.map(d => {
        return {
          name: d.name,
          value: Math.floor((d.value / total) * 100) / 100
        };
      });
    });
  }
}
