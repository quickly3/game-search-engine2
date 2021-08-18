import PuppeteerBase from "./puppeteerBase"

export default class Bing2glassdoor extends PuppeteerBase{

    sourceSite:string
    link:string

    setSourceWebSite(type){
        switch (type) {
            case 'cb':
                this.sourceSite = "www.crunchbase.com/organization"
                break;
            case 'gd':
            default:
                this.sourceSite = "www.glassdoor.com/Overview"
                break;
        }
    }

    async crawlGlassdoorUrl(org, useNameFirst=false){
        let redirect_url = ""
        let url = ""
        let query_type = ""
        const website = this.sourceSite.replace("/","%2F");

        if(org.url.trim() === '' || useNameFirst){
            url = `https://www.bing.com/search?q=site%3a${website}+${encodeURI(org.name)}`;
            url = url.replace("&","%26");
            query_type = 'name'
        }else{
            const fm_org_url = org.url.replace(/.*\/\//,'').replace(/\/.*/,'')
            url = `https://www.bing.com/search?q=site%3a${website}+${encodeURI(fm_org_url)}`;
            url = url.replace("&","%26");
            query_type = 'url'
        }

        const page = (await this.browser.pages())[0];

        console.log(url)

        const link1 = '#b_results > li:nth-child(1) > h2 > a'
        const link2 = '#b_results > li:nth-child(2) > h2 > a'
        const link3 = '#b_results > li.b_algo.b_algoBorder > div.b_algo_group > div > h2 > a'
        
        const links = [link1, link2, link3]

        try {
            await page.goto(url);

            await page.waitForSelector(links.join(", "),{
                timeout:5000
            }); 

        } catch (error) {
            console.error(error)
            console.error(`missing glassdoor url from bing`)

            await page.close();

            return redirect_url;
        }

        try {
            redirect_url = await page.evaluate((links)=>{
                let url = ""
                for(const link of links){
                    const linkNode = document.querySelector(links);
                    if(linkNode){
                        url = linkNode.getAttribute("href");
                        break;
                    }
                }
                return url;
            },links);

            

            if(redirect_url.indexOf(this.sourceSite) < 0){
                redirect_url = "";
            }

            console.log(redirect_url)

            if('' == redirect_url.trim() && query_type == 'url'){
                redirect_url = await this.crawlGlassdoorUrl(org,true)
            }

        } catch (error) {
            console.log(error)
            if(query_type == 'url'){
                redirect_url = await this.crawlGlassdoorUrl(org,true)
            }
        }
        await page.close();
        return redirect_url

    }

    async crawlByOrgs(orgs){
        const count = orgs.length
        const current = 0;

        for(const org of orgs){  
            org.target_url = await this.crawlGlassdoorUrl(org)
            console.log(org)  
        }
        return orgs;
    }

    async crawlOrg(org){
        org.target_url = await this.crawlGlassdoorUrl(org)

        return org;
    }

}