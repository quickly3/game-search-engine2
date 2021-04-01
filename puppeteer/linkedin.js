const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')
const sleep = require('sleep');

const ScrapePage = async(url)=>{

    const browser = await puppeteer.launch({
        headless: true,
        args: ['--disable-gpu']
    });

    const page = await browser.newPage();
    await page.goto(url,{
        waitUntil: 'networkidle2'
    });

    link = '#content_left > div:nth-child(1)  > h3 > a'

    await page.waitForSelector(link)
    await page.click(link)

    page.on('popup',async()=>{
        pages = await browser.pages();
        if(pages.length == 3){
            page2 = pages[2]
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            
            try {
                await page2.waitForSelector(nameSelector,{
                    timeout:50000
                })
                const resp = await page2.evaluate(() => {
                    nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
                    companyName = document.querySelector(nameSelector).textContent
                    return {companyName};
                })
                
                console.log(resp);
            } catch (error) {
                console.log("Linnkedin Render failed");
            }finally{            
                await browser.close();
            }

        }
    })
}


const bootstrap = async()=>{
    url = "https://www.baidu.com/s?wd=site%3Alinkedin.com%20inceptionpad";
    for (let i = 0; i < 100; i++) {
        await ScrapePage(url);
        await sleep.msleep(10000);
    }
}
bootstrap();

