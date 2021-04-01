const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')



const ScrapePage = async (url) => {
    options = {
        "args": [
            '--disable-gpu'
        ],
        "headless": false
    }
    const browser = await puppeteer.launch(options);
    const page = await browser.newPage();
    let result = []

    await page.goto(url, {
        waitUntil: 'networkidle2'
    });

    link = '#rso > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > a > h3'

    await page.waitForSelector(link)

    const linkNode = await page.$(link); 
    const resp1 = await page.evaluate(() => {
        link = '#rso > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > a'
        h3 = document.querySelector(link).textContent
        href = document.querySelector(link).href
        return {
            h3,
            href
        };
    })
    console.log(resp1)

    const newPagePromise = new Promise(x => browser.once('targetcreated', target => x(target.page())));

    await linkNode.click({button: 'middle'});    
    const page2 = await newPagePromise;  
    await page2.bringToFront();     

    nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
    linkedin_success = false
    page2.waitForTimeout(1000)
    try {
        await page2.waitForSelector(nameSelector, {
            timeout: 10000
        })
        resp = await page2.evaluate(() => {
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            companyName = document.querySelector(nameSelector).textContent
            return {
                companyName
            };
        })
        console.log(page2.url())
        console.log(resp)

    } catch (error) {

        await page2.close();

        await page.bringToFront();     
        await page.click(link)
        await page.waitForSelector(nameSelector, {
            timeout: 10000
        })

        let resp = await page.evaluate(() => {
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            companyName = document.querySelector(nameSelector).textContent
            return {
                companyName
            };
        })
        console.log(page2.url())
        console.log(resp)

    }finally{
        await browser.close();
    }
}

url = "https://www.google.com/search?q=site:linkedin.com+inceptionpad";
ScrapePage(url);
