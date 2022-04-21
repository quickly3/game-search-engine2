import { Component, OnInit } from "@angular/core";
import { GraphService } from "../api/graph.service";
import * as json2md from "json2md";


@Component({
  selector: "app-news",
  templateUrl: "./github.component.html",
  styleUrls: ["./github.component.scss"],
})
export class GithubComponent implements OnInit {
  private graphService: GraphService;
  MdData: any;
  MdText: any;
  showRawMd = "html";

  lans = [
    "javascript",
    "html",
    "typescript",
    "python",
    "php",
    "css",
    "Go",
    "C++",
    "Shell",
    "C#",
    "jupyter-notebook",
  ];
  spls = [
    'zh', 'en',
  ]
  sinces = [
    'daily','weekly','monthly'
  ]
  splList = [
  ]
  sinceList =[]
  lanList =[]

  selectedSpl
  selectedSince
  selectedLan

  constructor(graphService: GraphService) {
    this.graphService = graphService;
    this.splList = this.spls.map((d,i)=>{
      return {
        id:`splid_${i}`,
        text:d
      }
    })
    this.selectedSpl = this.splList[0];
    this.sinceList = this.sinces.map((d,i)=>{
      return {
        id:`splid_${i}`,
        text:d
      }
    })
    this.selectedSince = this.sinceList[0];
    this.lanList = this.lans.map((d,i)=>{
      return {
        id:`splid_${i}`,
        text:d
      }
    })
    this.selectedLan = this.lanList[0];
  }

  ngOnInit() {
    this.dailyGitHub();
  }

  dailyGitHub() {
    const params = { 
      since: this.selectedSince?.text,
      lan: this.selectedLan?.text,
      spl: this.selectedSpl?.text,
    }

    this.graphService.dailyGitHub(params).subscribe((resp: any) => {
      const dd: any[] = [{ h2: resp.title }];
      const dtext: any[] = [{ h2: resp.title }];

      for (const item of resp.data) {
        if (item.data.length > 0) {
          dd.push({ h5: item.title });
          dtext.push({ h5: item.title });

          item.data.forEach((item2: any, i: any) => {
            const summary = item2.summary;
            const starFork = `star : ${item2.digg_count} fork : ${item2.comment_count}`;
            dd.push({
              p: {
                link: {
                  title: `${i + 1}.${item2.title}`,
                  source: item2.url,
                },
              },
            });

            dd.push({
              p: summary,
            });
            dd.push({
              p: starFork,
            });

            dtext.push({
              p: `${i + 1}.${item2.title}`,
            });
            dtext.push({
              p: summary,
            });
            dtext.push({
              p: starFork,
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

  switchSpl(spl){
    this.selectedSpl = spl
    this.dailyGitHub();
  }

  switchLan(lan){
    this.selectedLan = lan
    this.dailyGitHub();
  }

  switchSince(since){
    this.selectedSince = since
    this.dailyGitHub();
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
