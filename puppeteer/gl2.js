const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')



const ScrapePage = async (url) => {
    options = {
        "useChrome": false,
        "args": [
            "--no-sandbox", 
        ],
        "headless": true
    }
    const browser = await puppeteer.launch(options);
    const page = await browser.newPage();

    await page.goto(url, {
        waitUntil: 'networkidle2'
    });

    link = '#rso > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > a > h3'

    await page.waitForSelector(link)
    await page.click(link)

    nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
    await page.waitForSelector(nameSelector, {
        timeout: 10000
    })

    page.on('console', msg => {
        for (let i = 0; i < msg.args.length; i++)[
            console.log(`${i}:${msg.args[i]}`)
        ]
    })
    const resp = await page.evaluate(() => {
        nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
        companyName = document.querySelector(nameSelector).textContent
        return {
            companyName
        };
    })
    console.log(page.url())
    console.log(resp)
    await browser.close();


}
url = "https://www.google.com/search?q=site:linkedin.com+inceptionpad";
ScrapePage(url);
