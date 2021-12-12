import { Component, OnInit } from '@angular/core';
import { GraphService } from '../api/graph.service';
import { Datum } from '../interface/Datum';

import DynamicComponentList from './sub-graph/dynamic.component.list';
@Component({
    selector: 'app-graph',
    templateUrl: './graph.component.html',
    styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
    dynamicComponents: any[];

    graphList = [{
        id: '1',
        title: '全部数据分布',
        name: 'SourceStatistics'
    }, {
        id: '2',
        title: '昨日数据分布',
        name: 'SourceStatisticsLastDay'
    }, {
        id: '3',
        title: '文章分类分布',
        name: 'CateStatistics'
    }];
    activeGraph = this.graphList[0].id;
    dynamicComponent;

    ngOnInit() {
        this. dynamicComponent = DynamicComponentList.getComponentByName(this.graphList[0].name);
    }

    subGraphChange(subGraph){
        this.dynamicComponent = DynamicComponentList.getComponentByName(subGraph.name);
    }
}
