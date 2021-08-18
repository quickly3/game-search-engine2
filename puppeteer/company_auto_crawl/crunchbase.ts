import PuppeteerBase from "./puppeteerBase"
import * as fs from "fs"

export default class Crunchbase extends PuppeteerBase {

    async crawl(org){
        
        const { target_url } = org;

        // const page = await this.browser.newPage();
        const page = (await this.browser.pages())[0];
        await page.setViewport({
            width: 1440,
            height: 636
        })

        let outputData = {
            name: '',
            alias: '',
            Website: '',
            Headquarters: '',
            Size: '',
            Founded: '',
            Type: '',
            Industry: '',
            Revenue: '',
            target_url: ''
        }

        if(target_url.trim() === ""){
            return {...outputData, ...org}
        }


        page.setCacheEnabled(false)
        try {
            await page.goto(target_url, {
                waitUntil: 'domcontentloaded',
                timeout: 10000
            });
        } catch (error) {
            console.error(error)
            await page.close();
            return org
        }

        const nameSelector = '.identifier-nav-title h1'
        const sizeSl = '.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card > ul > li:nth-child(2) > label-with-icon > span > field-formatter'
        const typeSl = '.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card > ul > li:nth-child(3) > label-with-icon > span > field-formatter'
        const webSiteSl = '.overview-divider.ng-star-inserted > div > row-card > div > div:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card > ul > li:nth-child(4) > label-with-icon > span > field-formatter'
        const innduSl = '.main-content > row-card:nth-child(1) > profile-section > section-card > mat-card > div.section-content-wrapper > div > fields-card:nth-child(1) > ul > li:nth-child(1) > field-formatter > identifier-multi-formatter > span > chips-container > a'
        
        try {
            // await page.screenshot({ path: 'cb.png' });
            await page.waitForSelector(nameSelector,{
                timeout:5000
            })

            const sl = {
                nameSelector,
                sizeSl,
                typeSl,
                webSiteSl,
                innduSl
            }

            const datas = await page.evaluate((sl)=>{

                const nameNode = document.querySelector(sl.nameSelector)
                const sizeNode = document.querySelector(sl.sizeSl)
                const typeNode = document.querySelector(sl.typeSl)
                const websiteNode = document.querySelector(sl.webSiteSl)
                const induNodes = document.querySelectorAll(sl.innduSl)

                
                const name = nameNode?nameNode.textContent.trim():"";
                const Size = sizeNode?sizeNode.textContent.trim():"";
                const Type = typeNode?typeNode.textContent.trim():"";
                const Website = websiteNode?websiteNode.textContent.trim():"";
                
                let IndustryArr = []

                for (let i = 0; i < induNodes.length; i++) {
                    const node = induNodes[i];
                    IndustryArr.push(node.text.trim())
                }

                const Industry = IndustryArr.join(" || ")


                const datas = {
                        name,
                        Size,
                        Type,
                        Website,
                        Industry
                    }
                return datas;
            },sl)

            datas.alias = [datas.name, org.name].join(" || ")
            datas.target_url = org.target_url

            console.log(datas)
            outputData = {...outputData, ...org, ...datas}


        } catch (error) {
            console.error(error);
        }

        await page.close();
        await page.deleteCookie();
        return outputData
    }

    async crawlByOrgs(orgs){
        const count = orgs.length
        const current = 0;

        const _orgs = [];

        for(const org of orgs){  
            const _org = await this.crawl(org);
            console.log(_org)  

            _orgs.push(_org)
        }
        return orgs;
    }

}
