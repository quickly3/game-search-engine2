import { Component, OnInit } from '@angular/core';
import { GraphService } from '../api/graph.service';
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
                    item.data.forEach((item2:any,i:any)=>{
                        dd.push({
                            link: {
                                title: `${i+1}. ${item2.title}`,
                                source: item2.url
                            }
                        });
                    });
                }
            }

            dd.push('')
            dd.push('关注微信公众号，上班摸鱼，获取更多每日互联网新闻~')
            dd.push('')
            dd.push('![即刻资讯](https://mp.weixin.qq.com/mp/qrcode?scene=10000004&size=102&__biz=Mzg2NzUzODY1Nw==&mid=2247483673&idx=1&sn=2c7edf333dada253bfb152646d891b92&send_time= "微信公众号")');
            dd.push('')

            this.MdData = json2md(dd).replace(/\n\n/g,'  \n');
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
