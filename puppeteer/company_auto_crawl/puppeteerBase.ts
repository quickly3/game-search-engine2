import * as puppeteer from "puppeteer"

export default class PuppeteerBase{
    browser:any;

    async init (headless=true){

        const userAgent = 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'

        const options = {
            headless,
            args: [
                "--disable-gpu",
                `--user-agent=${userAgent}`,
                '--window-size=1920,1080',
            ]
        }
        this.browser = await puppeteer.launch(options);
    }

    async close(){
        await this.browser.close();
    }
}