const Papa = require('papaparse')
const puppeteer = require('puppeteer');
var fs = require('fs');

const bootstrap = async()=>{

    headless = false;
    options = {
        headless: headless
    }

    let browser = await puppeteer.launch(options);
    var input_file = fs.readFileSync('unlinked_companies.csv', "utf8");
    orgs = Papa.parse(input_file,{header:true})
    output = []

    for(const org of orgs.data){

        if(org.url.trim() !== ''){
            url = `https://www.bing.com/search?q=site%3awww.linkedin.com+${encodeURI(org.url)}`;
            url = url.replace("&","%26");
            query_type = 'url'
        }else{
            url = `https://www.bing.com/search?q=site%3awww.linkedin.com+${encodeURI(org.name)}`;
            url = url.replace("&","%26");
            query_type = 'name'

        }

        const page = await browser.newPage();
        try {
            await page.goto(url, {
                waitUntil: 'domcontentloaded',
                timeout:3000
            });
        } catch (error) {
            console.log(error)
            await page.close();
        }

        link = '#b_results > li:nth-child(1) > h2 > a'

        try {
            await page.waitForSelector(link,{
                timeout:5000
            })

            redirect_url = await page.evaluate((link)=>{
                linkNode = document.querySelector(link);
                if(linkNode){
                    return linkNode.getAttribute("href");
                }
            },link)
            if(!redirect_url){
                redirect_url = '';
            }

            if(redirect_url.indexOf('https://www.linkedin.com')>-1){
                if(redirect_url.indexOf('https://www.linkedin.com/jobs')>-1){
                    redirect_url = ''
                }

                if(redirect_url.indexOf('https://www.linkedin.com/in')>-1){
                    redirect_url = ''
                }

                if(redirect_url.indexOf('https://www.linkedin.com/directory')>-1){
                    redirect_url = ''
                }

                if(redirect_url.indexOf('https://www.linkedin.com/pulse')>-1){
                    redirect_url = ''
                }

                if(redirect_url.indexOf('https://www.linkedin.com/salary')>-1){
                    redirect_url = ''
                }

                if(redirect_url.indexOf('https://www.linkedin.com/pub')>-1){
                    redirect_url = ''
                }

                if(redirect_url.indexOf('https://www.linkedin.com/learning')>-1){
                    redirect_url = ''
                }

                if('' != redirect_url.trim()){
                    redirect_url = redirect_url.replace(/\?.*/g,'')
                    redirect_url = redirect_url.replace(/#.*/g,'')
                    redirect_url = redirect_url.replace(/\/$/,'')
                    redirect_url = redirect_url + '/about';
                }
            }

            org.linkedin_url = redirect_url;
            org.query_type = query_type

            if('' != redirect_url.trim()){
                output.push(org)
            }
            await page.close();
        } catch (error) {
            console.error(error);
            await page.close();
        }
    }
    await browser.close();
    console.log(output)
    outputstr = Papa.unparse(output,{header:true})
    fs.writeFileSync('linked_companies.csv', outputstr ,"utf8");
}
bootstrap();

