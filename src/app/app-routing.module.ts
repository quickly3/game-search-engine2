import { RouterModule, Routes } from "@angular/router";
import { NgModule } from "@angular/core";
import { InfoqComponent } from "./infoq/infoq.component";


const appRoutes: Routes = [

  { path: "infoq", component: InfoqComponent },
  { path: "", redirectTo: "infoq", pathMatch: "full" },
  { path: "**", redirectTo: "infoq" }
];
@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes,
      {
        useHash :true,
        enableTracing: true
      },
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule {}
