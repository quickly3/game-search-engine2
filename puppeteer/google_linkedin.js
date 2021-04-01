const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')



const ScrapePage = async (url) => {
    options = {
        "useChrome": false,
        "stealth": false,
        "args": [
            '--no-sandbox', 
            '--disable-setuid-sandbox', 
            '--single-process'],
        "timeout": 15000,
        "headless": true
    }
    const browser = await puppeteer.launch(options);
    const page = await browser.newPage();
    let result = []

    await page.goto(url, {
        waitUntil: 'networkidle2'
    });

    link = '#rso > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > a > h3'

    console.log(link)
    await page.waitForSelector(link)

    const linkNode = await page.$(link); 
    const newPagePromise = new Promise(x => browser.once('targetcreated', target => x(target.page())));
    await linkNode.click({button: 'middle'});    
    const page2 = await newPagePromise;  
    await page2.bringToFront();     

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
url = "https://www.google.com/search?q=site:linkedin.com+inceptionpad";
ScrapePage(url);
