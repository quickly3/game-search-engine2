import { Component, Input, OnInit, OnChanges, ViewChild, ComponentFactoryResolver } from '@angular/core';

import { SubGraph } from './subGraph.directive';

@Component({
  selector: 'dynamic-sub-graph',
  template: `
              <div class="dynamic-sub-graph">
                <div class="container">
                  <h2>{{title}}</h2>
                  <ng-template subGraph></ng-template>
                </div>
              </div>
            `,
  styleUrls: ['./dynamic-sub-graph.component.scss'],
})
export class DynamicSubGraph implements OnInit, OnChanges {
  @Input() dynamicComponent: any;
  @ViewChild(SubGraph, {static: true}) subGraph: SubGraph;
  title;

  constructor(private componentFactoryResolver: ComponentFactoryResolver) { }

  ngOnInit() {
    // this.loadComponent();
  }

  ngOnChanges(): void {
    this.loadComponent();
  }

  loadComponent() {
    this.title = this.dynamicComponent.title;

    const componentFactory = this.componentFactoryResolver.resolveComponentFactory(this.dynamicComponent.component);
    const viewContainerRef = this.subGraph.viewContainerRef;

    viewContainerRef.clear();
    viewContainerRef.createComponent(componentFactory);

  }
}
