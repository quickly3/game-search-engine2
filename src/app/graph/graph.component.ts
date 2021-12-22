import { Component, OnInit } from '@angular/core';
import DynamicComponentList from './sub-graph/dynamic.component.list';
import { Router, ActivatedRoute } from '@angular/router';



@Component({
    selector: 'app-graph',
    templateUrl: './graph.component.html',
    styleUrls: ['./graph.component.scss'],
})
export class GraphComponent implements OnInit {
    dynamicComponents: any[];
    graphList = DynamicComponentList.components;

    dynamicComponent;

    constructor(
        private route: ActivatedRoute,
        private router: Router
    ) { }

    ngOnInit() {
        const urlParams = this.route.snapshot.queryParams;
        if(urlParams.name && this.graphList.filter(item=>item.name == urlParams.name ).length > 0){
            this.dynamicComponent = DynamicComponentList.getComponentByName(urlParams.name);
        }else{
            this.dynamicComponent = DynamicComponentList.getComponentByName(this.graphList[0].name);
            this.urlChangeByName(this.graphList[0].name);
        }
    }

    subGraphChange(subGraph){
        this.urlChangeByName(subGraph.name);
        this.dynamicComponent = DynamicComponentList.getComponentByName(subGraph.name);
    }

    urlChangeByName(name){
        const nativeParams: any  = {name};
        this.router.navigate([], {
            relativeTo: this.route,
            queryParams: nativeParams,
        });
    }

}
