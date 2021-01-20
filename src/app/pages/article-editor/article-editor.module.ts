import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { ArticleEditorComponent } from "./article-editor.component";

import { ComponentsModule } from "app/components/components.module";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";

@NgModule({
    declarations: [ArticleEditorComponent],
    imports: [CommonModule, ComponentsModule, FormsModule, ReactiveFormsModule]
})
export class ArticleEditorModule {}
