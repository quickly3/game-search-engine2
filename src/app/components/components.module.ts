import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavComponent } from './nav/nav.component';
import HorizontalBarComponent from './graph/horizontal-bar/horizontal-bar.component';
import PieComponent from './graph/pie/pie.component';
import TagsModalComponent from './modal/tags-modal/tags-modal.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@NgModule({
    imports: [
        CommonModule,
        FontAwesomeModule
    ],
    declarations: [
        NavComponent,
        HorizontalBarComponent,
        PieComponent,
        TagsModalComponent
    ],
    exports: [
        CommonModule,
        NavComponent,
        HorizontalBarComponent,
        PieComponent,
        TagsModalComponent
    ]
})
export class ComponentsModule {}
