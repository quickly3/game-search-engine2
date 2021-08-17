const Papa = require('papaparse')
const puppeteer = require('puppeteer');
var fs = require('fs');



const bootstrap = async()=>{

    headless = true;
    options = {
        headless: headless,
        args: [
            "--disable-gpu",
        ]
    }

    var browser = await puppeteer.launch(options);


    async function crawl(url){

        const page = await browser.newPage();
        page.setCacheEnabled(false)
        try {
            await page.goto(url, {
                waitUntil: 'domcontentloaded',
                timeout: 10000
            });
        } catch (error) {
            console.error(error)
            await page.close();
            return
        }

        datasSelector = '#EIOverviewContainer > div > div:nth-child(1) > ul > li'
        nameSelector = '#EmpHeroAndEmpInfo > div.empInfo.tbl.hideHH > div.header.cell.info > h1 > span'
        try {
            await page.waitForSelector(datasSelector,{
                timeout:10000
            })

            datas = await page.evaluate((datasSelector)=>{
                data = {}
                texts = $(datasSelector).map((i,d)=> $(d).text()).map((i,t)=>{
                    const arr = t.split(":");
                    data[arr[0]] = arr[1]
                });
                return data;
            },datasSelector)


            datas.name = await page.evaluate((nameSelector)=>{
                return $(nameSelector).text().trim();
            },nameSelector)

            console.log(datas)

        } catch (error) {
            console.error(error);
            await page.close();
        }

        await page.close();
        await page.deleteCookie();
    }


    await crawl("https://www.glassdoor.com.hk/Overview/Working-at-Foundation-Medicine-EI_IE779924.11,30.htm?countryRedirect=true")
    // await browser.close();



}


bootstrap();
