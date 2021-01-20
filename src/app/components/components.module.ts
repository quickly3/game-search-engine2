import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { NavComponent } from "./nav/nav.component";
import { StarRatingComponent } from "./utils/star-rating/star-rating.component";

@NgModule({
    imports: [CommonModule],
    declarations: [NavComponent, StarRatingComponent],
    exports: [CommonModule, NavComponent, StarRatingComponent]
})
export class ComponentsModule {}
