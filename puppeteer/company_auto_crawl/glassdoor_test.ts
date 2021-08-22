import Glassdoor from './glassdoor'

async function bootstrap(){
    const cb_crawler = new Glassdoor();

    const org = {
        name: "",
        url: "",
        target_url:"https://www.glassdoor.com/Overview/Working-at-TitanHouse-EI_IE1731558.11,21.htm"
    }

    await cb_crawler.init();
    const orgs_cb  = await cb_crawler.crawl(org);
    await cb_crawler.close();

    console.log(orgs_cb);
}

bootstrap()