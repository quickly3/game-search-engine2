import { InfoqComponent } from './infoq/infoq.component';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ComponentsModule } from './components/components.module';
import { NgbModule,NgbTypeaheadModule } from '@ng-bootstrap/ng-bootstrap';
import { MainPipe } from './pipe/main-pipe.module';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FormsModule } from '@angular/forms';
import { GraphComponent } from './graph/graph.component'; 

@NgModule({
  declarations: [
    AppComponent,
    InfoqComponent,
    GraphComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,
    ComponentsModule,
    NgbModule,
    NgbTypeaheadModule,
    MainPipe,
    FontAwesomeModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
