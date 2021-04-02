const puppeteer = require('puppeteer');
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
    const linkNode = await page.$(link); 
    await page.click(link)

    const newPagePromise = new Promise(x => browser.once('targetcreated', target => x(target.page())));
    await linkNode.click({button: 'middle'});    
    const page2 = await newPagePromise;  
    await page2.bringToFront();     

    nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
    

    try {
        await page2.waitForSelector(nameSelector,{
            timeout:5000
        })
        const resp = await page2.evaluate(() => {
            company = {}
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            company.name = document.querySelector(nameSelector).textContent

 
            tableDateKeySelector = '#main-content > section.core-rail > section.about-us.section-container > dl > div:nth-child(1) > dt'
            tableDateKeyNodes = document.querySelectorAll(tableDateKeySelector)

            tableDateKeys = tableDateKeyNodes.map(node=>{
                return node.textContent;
            })

            tableDateValueSelector = '#main-content > section.core-rail > section.about-us.section-container > dl > div:nth-child(1) > dd'
            tableDateValueNodes = document.querySelectorAll(tableDateValueSelector)
            tableDateValues = tableDateValueNodes.map(node=>{
                return node.textContent;
            })

            tableDateKeys.map((key,i)=>{
                company[key] = tableDateValues[i];
            })

            return company;
        })
        
        console.log(resp);
    } catch (error) {
        console.log("Linnkedin Render failed");
    }finally{            
        await browser.close();
    }

}


const bootstrap = async()=>{

    companies = [
        'InceptionPad',
        'Bergen Community College','BoxTone Inc','24 Hour Fitness','2U','3Com Corporation',
        '3S Media','522 Productions','A-Town Bar and Grill','Abbott Laboratories/Quintiles Commercial',
        'Abercrombie & Fitch','Absolute Software','Abstract','Accents by Design','Accenture',
        'Access Funding, LLC','ACE Hardware Corporation','Fortren Funding LLC','Acendre',
        'Achieved Solutions','Acquia','Acterna','Actian, Corporation','Actuate (opentext)',
        'Acuity Audio Visual','AD PAGES MARKETING','ADF Solutions, Inc','Adobe','Adrian College',
        'American University','BaseInfoSec','Adtran','Advance Business Systems',
        'Advanced & Emerging Technologies','Advanced Computer Concepts','Advantage Green, Inc',
        'Advantech','AECOM, Inc','AEG Worldwide','Aerva, Inc','Aether Systems'
    ]

    for (const i in companies) {
        name = companies[i]
        url = `https://www.baidu.com/s?wd=site%3Alinkedin.com%20${encodeURI(name)}`;
        await ScrapePage(url);
        const random = Math.ceil(Math.random() *10 - 5);
        await sleep.sleep(17+random);
    }
}
bootstrap();

