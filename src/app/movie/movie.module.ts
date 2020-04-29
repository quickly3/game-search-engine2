import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MovieComponent } from './movie.component';

import { AppRoutingModule } from 'app/app-routing.module';

import { BootstrapModule } from 'app/plugins/bootstrap.module';
import { FormsModule } from '@angular/forms';
import { ComponentsModule } from '../components/components.module';
import { AngularFontAwesomeModule } from 'angular-font-awesome';

@NgModule({
  declarations: [MovieComponent],
  imports: [
    CommonModule,
    BootstrapModule,
    AppRoutingModule,
    FormsModule,
    ComponentsModule,
    AngularFontAwesomeModule
  ]
})
export class MovieModule { }
