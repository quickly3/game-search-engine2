const puppeteer = require('puppeteer');

const ScrapePage = async (name,options) => {

    name = name.replace(/ /g,'+')
    url = `https://www.google.com/search?q=site:www.linkedin.com+${name}`;
    
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


    link = '#main > div:nth-child(4) > div > div:nth-child(1) > a'
    link2 = '#rso > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > a > h3'

    try {
        await page.waitForSelector(link,{
            timeout:5000
        })
    } catch (error) {
        try {
            await page.waitForSelector(link2,{
                timeout:5000
            })
            link = link2;
        } catch (error) {
            await browser.close();
            return {
                success:false
            }
        }
    }

    const linkNode = await page.$(link); 

    const newPagePromise = new Promise(x => browser.once('targetcreated', target => x(target.page())));
    await linkNode.click({button: 'middle'});    
    const page2 = await newPagePromise;  
    await page2.bringToFront();     

    nameSelector = '#main-content > section.core-rail > section.top-card-layout > div > div.top-card-layout__entity-info-container > div:nth-child(1) > h1'
    success = false;
    let resp = {}
    try {
        await page2.waitForSelector(nameSelector,{
            timeout:5000
        })
        resp = await page2.evaluate((params) => {
            return params.PageParse(document);
        },{PageParse})
        if(resp.name){
            success = true;
        }
        console.log(resp);
    } catch (error) {
        console.log("Linnkedin Render failed");
    }finally{            
        await browser.close();
    }
    return {
        success,
        resp
    };
}

module.exports = ScrapePage;
