const puppeteer = require('puppeteer');
const cookies = require('./cookies.json');
const fs = require('fs')



const ScrapePage = async(url)=>{

    file = '/Users/hongbinzhou/Downloads/linkedin1.jpeg'
    file2 = '/Users/hongbinzhou/Downloads/linkedin2.jpeg'
    file3 = '/Users/hongbinzhou/Downloads/linkedin3.jpeg'

    if(fs.existsSync(file)){
        fs.unlinkSync(file);
    }

    const browser = await puppeteer.launch({
        headless: false,
    });

    const width = 1920 
    let height = 1200

    const page = await browser.newPage();
    let result = []

    await page.setViewport({
        width : width,
        height : height
    })

    await page.goto(url,{
        waitUntil: 'networkidle2'
    });
    
    await page.screenshot({path:file});
    // await page.setCookie(...cookies);

    link = '#content_left > div:nth-child(1)  > h3 > a'

        
    await page.waitForSelector(link)
    await page.click(link)

    pages = await browser.pages();
    page2 = pages[2]

    // console.log(await page.content())
    await page2.reload({
        waitUntil: 'networkidle2'
    })
    await page2.waitForNavigation()
    console.log(await page2.content())



}
url = "https://www.baidu.com/s?wd=site%3Alinkedin.com%20inceptionpad";
ScrapePage(url);
