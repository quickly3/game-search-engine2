import { ExtraOptions, RouterModule, Routes } from "@angular/router";
import { NgModule } from "@angular/core";

import { GamesComponent } from "./games/games.component";
import { InfoqComponent } from "./infoq/infoq.component";
import { GameDetailComponent } from "./game-detail/game-detail.component";


const routes: Routes = [
  { path: "games", component: GamesComponent },
  { path: "infoq", component: InfoqComponent },
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
