const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')



const ScrapePage = async (url) => {
    options = {
        "useChrome": false,
        "stealth": false,
        "args": [
            "--remote-debugging-port=9222", 
            "--no-sandbox", 
        ],
        "timeout": 15000,
        "headless": false
    }
    const browser = await puppeteer.launch(options);
    const page = await browser.newPage();
    let result = []

    await page.goto(url, {
        waitUntil: 'networkidle2'
    });

    link = '#content_left > div:nth-child(1)  > h3 > a'

    console.log(link)
    await page.waitForSelector(link)
    await page.click(link)

    page.on('popup', async () => {
        pages = await browser.pages();
        if (pages.length == 3) {
            page2 = pages[2]
            console.log(page2.url())
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            await page2.waitForSelector(nameSelector, {
                timeout: 10000
            })

            page2.on('console', msg => {
                for (let i = 0; i < msg.args.length; i++)[
                    console.log(`${i}:${msg.args[i]}`)
                ]
            })
            const resp = await page2.evaluate(() => {
                nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
                companyName = document.querySelector(nameSelector).textContent
                return {
                    companyName
                };
            })
            console.log(page2.url())
            console.log(resp)
            await browser.close();

        }
    })
}
url = "https://www.google.com/search?q=site:linkedin.com+inceptionpad";
ScrapePage(url);
