import { NgModule } from "@angular/core";
import { InfoqComponent } from "./infoq.component";
import { CommonModule } from "@angular/common";

import { BootstrapModule } from "../plugins/bootstrap.module";
import { AppRoutingModule } from "../app-routing.module";
import { FormsModule } from "@angular/forms";
import { ComponentsModule } from "../components/components.module";
import { MainPipe } from "../pipe/main-pipe.module";

const PAGES_COMPONENTS = [
    // InfoqComponent
    // NavComponent
];

@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        AppRoutingModule,
        BootstrapModule,
        ComponentsModule,
        MainPipe
    ],
})
export class InfoqModule {}
