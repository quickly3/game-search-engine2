import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavComponent } from './nav/nav.component';
import HorizontalBarComponent from './graph/horizontal-bar/horizontal-bar.component';
import PieComponent from './graph/pie/pie.component';

@NgModule({
    imports: [CommonModule],
    declarations: [
        NavComponent,
        HorizontalBarComponent,
        PieComponent],
    exports: [
        CommonModule,
        NavComponent,
        HorizontalBarComponent,
        PieComponent
    ]
})
export class ComponentsModule {}
