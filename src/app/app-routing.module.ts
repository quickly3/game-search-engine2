import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import { InfoqComponent } from './infoq/infoq.component';
import { GraphComponent } from './graph/graph.component';
import { NewsComponent } from './news/news.component';


const appRoutes: Routes = [
  { path: 'infoq', component: InfoqComponent },
  { path: 'graph', component: GraphComponent },
  { path: 'news', component: NewsComponent },
  { path: '', redirectTo: 'infoq', pathMatch: 'full' },
  { path: '**', redirectTo: 'infoq' }
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes,
      {
        useHash : true,
        enableTracing: false
      },
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {}
