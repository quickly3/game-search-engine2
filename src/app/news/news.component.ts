import { Component, OnInit } from '@angular/core';
import { GraphService } from '../api/graph.service';
import { Datum } from '../interface/Datum';
import * as json2md from 'json2md';

@Component({
    selector: 'app-news',
    templateUrl: './news.component.html',
    styleUrls: ['./news.component.scss'],
})
export class NewsComponent implements OnInit {
    private graphService: GraphService;
    MdData: any;
    showRawMd = true;

    constructor(graphService: GraphService) {
        this.graphService = graphService;
    }

    ngOnInit() {
        this.getDailyMd();
    }

    getDailyMd() {
        this.graphService.dailyMd().subscribe((resp: any) => {

            const dd: any[] = [
                {h2: resp.title}
            ];

            for (const item of resp.data){
                if (item.data.length > 0){
                    dd.push({h5: item.title});
                    for (const item2 of item.data){
                        dd.push({
                            link: {
                                title: item2.title,
                                source: item2.url
                            }
                        });
                    }
                }
            }

            this.MdData = json2md(dd);
        });
    }

    switchRaw(){
        this.showRawMd = !this.showRawMd;
    }

    copyMessage(val: string){
        const selBox = document.createElement('textarea');
        selBox.style.position = 'fixed';
        selBox.style.left = '0';
        selBox.style.top = '0';
        selBox.style.opacity = '0';
        selBox.value = val;
        document.body.appendChild(selBox);
        selBox.focus();
        selBox.select();
        document.execCommand('copy');
        document.body.removeChild(selBox);
      }

}
