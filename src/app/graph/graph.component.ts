import { Component, OnInit } from '@angular/core';
import DynamicComponentList from './sub-graph/dynamic.component.list';
@Component({
    selector: 'app-graph',
    templateUrl: './graph.component.html',
    styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
    dynamicComponents: any[];
    graphList = DynamicComponentList.components;

    dynamicComponent;

    ngOnInit() {
        this. dynamicComponent = DynamicComponentList.getComponentByName(this.graphList[0].name);
    }

    subGraphChange(subGraph){
        this.dynamicComponent = DynamicComponentList.getComponentByName(subGraph.name);
    }
}
