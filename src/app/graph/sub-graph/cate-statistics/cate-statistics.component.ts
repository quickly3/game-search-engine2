import { Component } from '@angular/core';
import { Datum } from '../../../interface/Datum';
import { GraphService } from '../../../api/graph.service';

@Component({
  templateUrl: './cate-statistics.component.html',
})
export class CateStatistics {
  tagsData: Datum[] = [];

  constructor(private graphService: GraphService) {}

  radiusFix = (i) => Math.sqrt(i);

  ngOnInit() {
    this.getTagsAgg();
  }

  getTagsAgg() {
    this.graphService.getTagsAgg({size: 100}).subscribe((data: any) => {
        this.tagsData = data;
    });
}

}
