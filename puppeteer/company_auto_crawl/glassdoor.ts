import PuppeteerBase from "./puppeteerBase"
import { proxyRequest } from 'puppeteer-proxy';
import * as fs from "fs"

export default class Glassdoor extends PuppeteerBase {

    async crawl(org){
        
        const { target_url } = org;

        const page = (await this.browser.pages())[0];

        // await page.setRequestInterception(true);

        // page.on('request', async (request) => {
        //     await proxyRequest({
        //     page,
        //     proxyUrl: {
        //         https:'179.1.84.122:999',
        //         http: '67.207.83.225:80'

        //         // http:'http://127.0.0.1:9999',
        //         // https: 'https://127.0.0.1:9999'
        //     },
        //     request,
        //     });
        // });

        let outputData = {
            name: '',
            alias: '',
            Website: '',
            Headquarters: '',
            Size: '',
            Founded: '',
            Type: '',
            Industry: '',
            Revenue: '',
            target_url: ''
        }

        if(target_url.trim() === ""){
            return {...outputData, ...org}
        }

        page.setCacheEnabled(false)

        try {
            await page.goto(target_url, {
                waitUntil: 'domcontentloaded',
                timeout: 10000
            });
        } catch (error) {
            console.error(error)
            await page.close();
            return org
        }

        const datasSelector = '#EIOverviewContainer > div > div:nth-child(1) > ul > li'
        const nameSelector = '#EmpHeroAndEmpInfo > div.empInfo.tbl.hideHH > div.header.cell.info > h1 > span'
        try {
            // await page.screenshot({ path: 'example.png' });
            // const html = await page.evaluate(()=>{
            //     const html = $("html").first().text();
            //     return html;
            // },{})

            // fs.writeFileSync("gd.html", html)

            await page.waitForSelector(datasSelector,{
                timeout:5000
            })

            const datas = await page.evaluate((datasSelector)=>{
                const data = {}
                const texts = $(datasSelector).map((i,d)=> $(d).text()).map((i,t)=>{  
                    const arr = t.split(":");
                    data[arr[0]] = arr[1]
                });
                return data;
            },datasSelector)

            datas.name = await page.evaluate((nameSelector)=>{
                return $(nameSelector).text().trim();
            },nameSelector)

            datas.alias = [datas.name, org.name].join(" || ")
            datas.target_url = org.target_url
            outputData = {...outputData, ...org, ...datas}

            console.log(outputData);

        } catch (error) {
            console.error(error);
        }

        await page.close();
        await page.deleteCookie();
        return outputData
    }

    async crawlByOrgs(orgs){
        const count = orgs.length
        const current = 0;

        const _orgs = [];

        for(const org of orgs){  
            const _org = await this.crawl(org);
            console.log(_org)  

            _orgs.push(_org)
        }
        return orgs;
    }

}
