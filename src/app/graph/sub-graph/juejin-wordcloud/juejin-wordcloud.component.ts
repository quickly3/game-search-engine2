import { Component } from "@angular/core";
import { Datum } from "../../../interface/Datum";
import { InfoqService } from "../../../api/infoq.service";

@Component({
  templateUrl: "./juejin-wordcloud.component.html",
})
export class JuejinWordCloud {
  words: string[] = [];

  constructor(private infoqService: InfoqService) {}
  ngOnInit() {
    this.loadCloud();
  }

  loadCloud() {
    this.infoqService
      .getWordsCloud({ tag: "*", source: "juejin",size:1000 })
      .subscribe((resp:any) => {
        this.words = resp;
      });
  }
}
