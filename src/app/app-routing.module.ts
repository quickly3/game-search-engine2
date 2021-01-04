import { ExtraOptions, RouterModule, Routes } from "@angular/router";
import { NgModule } from "@angular/core";

import { GamesComponent } from "./games/games.component";
import { FanjuComponent } from "./fanju/fanju.component";
import { EscnDailyComponent } from "./escn-daily/escn-daily.component";
import { JianshuComponent } from "./jianshu/jianshu.component";
import { JuejinComponent } from "./juejin/juejin.component";
import { InfoqComponent } from "./infoq/infoq.component";

import { GameDetailComponent } from "./game-detail/game-detail.component";
import { ArticleEditorComponent } from "./pages/article-editor/article-editor.component";
import { MovieComponent } from './movie/movie.component';
import { MovieDetailComponent } from './movie/detail/movie.detail.component';


const routes: Routes = [
  { path: "games", component: GamesComponent },
  { path: "fanju", component: FanjuComponent },
  { path: "escn-daily", component: EscnDailyComponent },
  { path: "jianshu", component: JianshuComponent },
  { path: "juejin", component: JuejinComponent },
  { path: "infoq", component: InfoqComponent },
  { path: "movie", component: MovieComponent },
  { path: "movie/:id", component: MovieDetailComponent },
  { path: "article-editor/:id", component: ArticleEditorComponent },
  { path: "game-detail/:id", component: GameDetailComponent },
  { path: "", redirectTo: "infoq", pathMatch: "full" },
  { path: "**", redirectTo: "infoq" }
];

const config: ExtraOptions = {
  useHash: true
  // enableTracing: true
};

@NgModule({
  imports: [RouterModule.forRoot(routes, config)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
