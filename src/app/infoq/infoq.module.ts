import { NgModule } from "@angular/core";
import { InfoqComponent } from "./infoq.component";
import { CommonModule } from "@angular/common";

import { BootstrapModule } from "app/plugins/bootstrap.module";
import { AppRoutingModule } from "app/app-routing.module";
import { FormsModule } from "@angular/forms";
import { ComponentsModule } from "../components/components.module";

const PAGES_COMPONENTS = [
    InfoqComponent
    // NavComponent
];

@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        AppRoutingModule,
        BootstrapModule,
        ComponentsModule
        // AngularFontAwesomeModule
    ],
    declarations: [...PAGES_COMPONENTS]
})
export class EscnDailyModule {}
