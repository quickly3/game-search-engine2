import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import { InfoqComponent } from './infoq/infoq.component';
import { AuthorComponent } from './author/author.component';
import { GraphComponent } from './graph/graph.component';
import { NewsComponent } from './news/news.component';
import { GithubComponent } from './github/github.component';
import { KrNewsComponent } from './kr-news/kr-news.component';


const appRoutes: Routes = [
  { path: 'infoq', component: InfoqComponent },
  { path: 'author', component: AuthorComponent },
  { path: 'graph', component: GraphComponent },
  { path: 'news', component: NewsComponent },
  { path: 'kr-news', component: KrNewsComponent },
  { path: 'github', component: GithubComponent },
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
