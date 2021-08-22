import config from '../config';
import { Client } from '@elastic/elasticsearch'
import Bing2glassdoor from './bing2glassdoor'
import Glassdoor from './glassdoor'
import Crunchbase from './crunchbase'

import * as dotenv from 'dotenv';
dotenv.config()

const es_config = config.es[process.env.env];

async function getCompanyFeeds(){
    const es = new Client({node: es_config})
    const query = {
        "query": {
            "query_string": {
            "query": "company:* && -company.id:* && updatedAt:[2021-08-11 TO 2021-08-12]"
            }
        },
        "_source": [
            "id",
            "company",
            "updatedAt"
        ],
        "sort": {
            "updatedAt": {
            "order": "desc"
            }
        }
    }

    const resp = await es.search({
        index:"4_Experiences",
        body:query
    })

    const hits = resp.body.hits.hits
    const datas = hits.map(i=>i._source);
    const outputData = datas.map(data=>({
        id:data.id,
        companyName:data.company.name,
        companyUrl:data.company.url
    }));

    const names = [];
    const nameIds = {}

    for (const exp of outputData) {
      if (!nameIds[exp.companyName]) {
        nameIds[exp.companyName] = [exp.id];
      } else {
        nameIds[exp.companyName].push(exp.id);
      }
    }

    for (const name of Object.keys(nameIds)) {
      let url = '';
      for (const exp of outputData) {
        if (exp.companyName === name && exp.companyUrl && exp.companyUrl.trim() !== '') {
          url = exp.companyUrl.trim()
        }
      }

      url = url.replace(/.*:\/\//,'').replace(/\/.*/,'')
      names.push({
        name,
        url,
        exp_ids: nameIds[name].join(','),
      });
    }

    // const dateStr = (new Date).toISOString().replace(/T.*/,"");
    // const dir = 'feeds'
    // const fileName = `${dir}/feeds-${dateStr}.csv`
    // const datasStr = Papa.unparse(names,{header:true})

    // if (!fs.existsSync(dir)){
    //     fs.mkdirSync(dir);
    // }

    // fs.writeFileSync(fileName, datasStr, "utf8");
    return names;
}

async function bing2gd(){
    const orgs = await getCompanyFeeds();
    
    const crawler = new Bing2glassdoor();
    // crawler.setSourceWebSite('gd')
    crawler.setSourceWebSite('gd')

    const gd_crawler = new Glassdoor();

    try {
        await crawler.init();
        const orgs_with_dataLink  = await crawler.crawlByOrgs(orgs);


        await gd_crawler.init();
        const orgs_gd  = await gd_crawler.crawlByOrgs(orgs_with_dataLink);


    } catch (error) {
        console.error(error)
    }

    await crawler.close();
    await gd_crawler.close();

}

async function bing2cb(){
    const orgs = await getCompanyFeeds();
    
    const crawler = new Bing2glassdoor();
    crawler.setSourceWebSite('cb')
    const cb_crawler = new Crunchbase();


    try {
        await crawler.init();
        const orgs_with_dataLink  = await crawler.crawlByOrgs(orgs);


        await cb_crawler.init();

        const orgs_cb  = await cb_crawler.crawlByOrgs(orgs_with_dataLink);


    } catch (error) {
        console.error(error)
    }

    await crawler.close();
    await cb_crawler.close();

}

bing2cb();


// bing2gd();