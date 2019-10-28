import { RouterModule, Routes } from "@angular/router";
import { NgModule } from "@angular/core";
import { JuejinComponent } from "./juejin.component";
// import { EscnDailyRoutingModule } from './escn-daily-routing.module';
import { CommonModule } from "@angular/common";

import { BootstrapModule } from "app/plugins/bootstrap.module";
import { AppRoutingModule } from "app/app-routing.module";
import { FormsModule } from "@angular/forms";

import { ComponentsModule } from "../components/components.module";
// import { AngularFontAwesomeModule } from 'angular-font-awesome';

const PAGES_COMPONENTS = [
    JuejinComponent
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
