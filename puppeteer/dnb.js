const puppeteer = require('puppeteer');
const cookies = require('./dnb_cookies.json');
const fs = require('fs')


const isAgencyUrl = url => url.includes("https://www.dnb.com")

const ScrapePage = async(url)=>{

    file = '/Users/hongbinzhou/Downloads/dnb.jpeg'

    if(fs.existsSync(file)){
        fs.unlinkSync(file);
    }

    const browser = await puppeteer.launch({
        headless: true,
        args: [
          '--proxy-server=socks5://127.0.0.1:10000',
          '--disable-gpu'
        ]
    });
    const width = 1920 
    let height = 1200

    const page = await browser.newPage();
    await page.setCookie(...cookies);
    let result = []

    await page.setViewport({
        width : width,
        height : height
    })

    await page.goto(url,{
        waitUntil: 'networkidle2'
    });

    await page.screenshot({path:file});

    await browser.close();
}

const init = (url)=>{
    if(isAgencyUrl(url)){
        ScrapePage(url);
    }
}

init("https://www.dnb.com/business-directory/top-results.html?term=inceptionpad&page=1")