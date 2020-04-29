import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AppRoutingModule } from 'app/app-routing.module';
import { BootstrapModule } from 'app/plugins/bootstrap.module';
import { FormsModule } from '@angular/forms';
import { ComponentsModule } from 'app/components/components.module';
import { AngularFontAwesomeModule } from 'angular-font-awesome';

import { MovieDetailComponent } from './movie.detail.component';

@NgModule({
  declarations: [MovieDetailComponent],
  imports: [
    CommonModule,
    BootstrapModule,
    AppRoutingModule,
    FormsModule,
    ComponentsModule,
    AngularFontAwesomeModule
  ]
})
export class MovieDetailModule { }
