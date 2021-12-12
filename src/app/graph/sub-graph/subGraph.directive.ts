// tslint:disable: directive-selector
import { Directive, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[subGraph]',
})
export class SubGraph {
  constructor(public viewContainerRef: ViewContainerRef) { }
}

