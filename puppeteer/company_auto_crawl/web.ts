
import * as http from 'http'
import * as url from 'url'

import Bing2glassdoor from './bing2glassdoor'
import Glassdoor from './glassdoor'
import Crunchbase from './crunchbase'

async function getDataFromBingGD(org){
    const crawler = new Bing2glassdoor();
    crawler.setSourceWebSite('gd')
    const gd_crawler = new Glassdoor();

    try {
        await crawler.init();
        const org_with_dataLink  = await crawler.crawlOrg(org);
        await crawler.close();

        if(org_with_dataLink.target_url == ""){
            return false;
        }

        await gd_crawler.init();
        const orgs_gd  = await gd_crawler.crawl(org_with_dataLink);
        await gd_crawler.close();
        return orgs_gd;

    } catch (error) {
        console.error(error)
        await gd_crawler.close();
        await crawler.close();
        return false;
    }
}

async function getDataFromBingCB(org){
    const crawler = new Bing2glassdoor();
    crawler.setSourceWebSite('cb')
    const cb_crawler = new Crunchbase();

    try {
        await crawler.init();
        const org_with_dataLink  = await crawler.crawlOrg(org);
        await crawler.close();

        if(org_with_dataLink.target_url == ""){
            return false;
        }
        await cb_crawler.init();
        const orgs_cb  = await cb_crawler.crawl(org_with_dataLink);
        await cb_crawler.close();


        return orgs_cb;

    } catch (error) {
        console.error(error)
        await crawler.close();
        await cb_crawler.close();
        return false;
    }
}


async function bootstrap(){
    const server = http.createServer(async (request, response) => {

        const pathname = url.parse(request.url).pathname;
        const query = url.parse(request.url,true).query
        let resp = "Invalid"

        if(!query.name && !query.url){
            resp = "Company name or url is must required."
        }else{
            const org = {
                name: query.name || "",
                url: query.url || ""
            }
            let data = {}
            switch (pathname) {
                case "/queryFromGD":
                    data = await getDataFromBingGD(org);
                    resp = JSON.stringify(data);
                    break;
                case "/queryFromCB":
                    data = await getDataFromBingCB(org);
                    if(!data){
                        resp = 'Missing url from bing'
                    }else{
                        resp = JSON.stringify(data);
                    }
                    break; 
                default:
                    break;
            }
        }

        response.write(resp);
        response.end()

    })

    const port = 8080

    server.listen(port)
    console.log(`Start at port: ${port}`)
}

bootstrap();