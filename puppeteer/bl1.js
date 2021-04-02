const puppeteer = require('puppeteer');
const PageParse = require('./PageParse.js');

ScrapePage = async(name,options)=>{

    url = `https://www.baidu.com/s?wd=site%3Alinkedin.com%20${encodeURI(name)}`;
    const browser = await puppeteer.launch(options);

    const page = await browser.newPage();
    try {
        await page.goto(url, {
            waitUntil: 'networkidle2',
            timeout:10000
        });
    } catch (error) {
        await browser.close();
        return {
            success:false,
            msg:'proxy timeout'
        }
    }

    link = '#content_left > div:nth-child(1) > h3 > a'

    await page.waitForSelector(link)
    await page.click(link)

    page.on('popup',async()=>{
        pages = await browser.pages();
        if(pages.length == 3){
            page2 = pages[2]
            nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
            
            try {
                await page2.waitForSelector(nameSelector,{
                    timeout:5000
                })
                const resp = await page2.evaluate((params) => {
                    return params.PageParse(document);
                },{PageParse})
                
                console.log(resp);
            } catch (error) {
                console.log("Linnkedin Render failed");
            }finally{            
                await browser.close();
            }

        }
    })
}

module.exports = ScrapePage;


