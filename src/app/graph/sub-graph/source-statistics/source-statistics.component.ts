import { Component } from '@angular/core';
import { Datum } from '../../../interface/Datum';
import { GraphService } from '../../../api/graph.service';
import { ArticleService } from '../../../api/article.service';

@Component({
  templateUrl: './source-statistics.component.html',
})
export class SourceStatistics {
  totalData: Datum[] = [];

  constructor(
    private graphService: GraphService,
    private articleService: ArticleService,
  ) {}

  radiusFix = (i) => Math.sqrt(i);
  ngOnInit() {
    this.getTotalData();
    this.getHistogram();
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

  getHistogram(){
    this.articleService.getHistogram({
      query:"*:*",
      calendar_interval:"month"
    }).subscribe((data: any) => {
      console.log(data);
    })
  }
}
