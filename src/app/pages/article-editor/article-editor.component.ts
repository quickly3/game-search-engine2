import { Component, OnInit } from "@angular/core";
import { FormControl, FormGroup } from "@angular/forms";

@Component({
    selector: "app-article-editor",
    templateUrl: "./article-editor.component.html",
    styleUrls: ["./article-editor.component.scss"]
})
export class ArticleEditorComponent implements OnInit {
    heroForm;
    constructor() {}

    ngOnInit() {}

    updateVal() {}

    onSubmit() {
        // console.warn(this.articleForm);
    }
}
