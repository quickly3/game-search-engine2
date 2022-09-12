import { Component, OnInit } from "@angular/core";
import { GraphService } from "../api/graph.service";
import * as json2md from "json2md";

@Component({
  selector: "app-news",
  templateUrl: "./kr-news.component.html",
  styleUrls: ["./kr-news.component.scss"],
})
export class KrNewsComponent implements OnInit {
  private graphService: GraphService;
  MdData: any;
  MdText: any;
  showRawMd = "html";

  constructor(graphService: GraphService) {
    this.graphService = graphService;
  }

  ngOnInit() {
    this.getDailyKr();
  }

  getDailyKr() {
    this.graphService.dailyKr().subscribe((resp: any) => {
      const dd: any[] = [{ h2: resp.title }];
      const dtext: any[] = [{ h2: resp.title }];

      for (const item of resp.data) {
        if (item.data.length > 0) {
          dd.push({ h5: item.title });
          dtext.push({ h5: item.title });

          item.data.forEach((item2: any, i: any) => {
            dd.push({
              p: {
                link: {
                  title: `${i + 1}.${item2.title}`,
                  source: item2.url,
                },
              },
            });
            dtext.push({
              p: `${i + 1}.${item2.title}`,
            });
          });
        }
      }
      this.MdData = json2md(dd).replace(/\n\n/g, "  \n");
      this.MdText = json2md(dtext).replace(/\n\n/g, "  \n");
    });
  }

  switchRaw(mode) {
    this.showRawMd = mode;
  }

  copyMessage(val: string) {
    const selBox = document.createElement("textarea");
    selBox.style.position = "fixed";
    selBox.style.left = "0";
    selBox.style.top = "0";
    selBox.style.opacity = "0";
    selBox.value = val;
    document.body.appendChild(selBox);
    selBox.focus();
    selBox.select();
    document.execCommand("copy");
    document.body.removeChild(selBox);
  }
}
