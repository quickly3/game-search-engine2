import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { NavComponent } from "./nav/nav.component";
import { ModalsModule } from "./modals/modals.module";

@NgModule({
    imports: [CommonModule, ModalsModule],
    declarations: [NavComponent],
    exports: [CommonModule, NavComponent]
})
export class ComponentsModule {}
