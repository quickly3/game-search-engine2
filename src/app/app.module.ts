import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";

import { AppRoutingModule } from "app/app-routing.module";
import { AppComponent } from "app/app.component";
import { ComponentsModule } from "./components/components.module";
import { ModalsModule } from "./components/modals/modals.module";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { MainPipe } from "./pipe/main-pipe.module";

@NgModule({
    declarations: [AppComponent],
    imports: [
        BrowserModule,
        BrowserAnimationsModule,
        HttpClientModule,
        AppRoutingModule,
        ComponentsModule,
        ModalsModule,
        NgbModule,
        MainPipe
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {}
