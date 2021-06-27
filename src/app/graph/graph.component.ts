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
    });
  }
}
