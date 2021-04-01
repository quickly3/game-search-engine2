const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')



const ScrapePage = async(url)=>{

    // file = '/Users/hongbinzhou/Downloads/linkedin1.jpeg'
    // file2 = '/Users/hongbinzhou/Downloads/linkedin2.jpeg'
    
    // if(fs.existsSync(file)){
    //     fs.unlinkSync(file);
    // }

    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--single-process']
    });
    console.log(1)

    // const width = 1920 
    // let height = 1200

    const page = await browser.newPage();
    console.log(2)
    let result = []

    // await page.setViewport({
    //     width : width,
    //     height : height
    // })

    await page.goto(url,{
        waitUntil: 'networkidle2'
    });

    console.log(3)
    
    // await page.screenshot({path:file});
    // await page.setCookie(...cookies);

    link = '#content_left > div:nth-child(1)  > h3 > a'

    await page.waitForSelector(link)
    console.log(link)

    await page.click(link)

    page.on('popup',async()=>{
        pages = await browser.pages();
        if(pages.length == 3){
            page2 = pages[2]
            console.log(page2.url())
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            await page2.waitForSelector(nameSelector,{
                timeout:10000
            })

            page2.on('console',msg=>{
                for(let i = 0; i < msg.args.length; i++)[
                    console.log(`${i}:${msg.args[i]}`)
                ]
            })
            const resp = await page2.evaluate(() => {
                nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
                companyName = document.querySelector(nameSelector).textContent
                return {companyName};
            })
            console.log(page2.url())
            console.log(resp)
            await browser.close();

        }
    })
}
url = "https://www.baidu.com/s?wd=site%3Alinkedin.com%20inceptionpad";
ScrapePage(url);
