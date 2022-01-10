/* eslint-disable */
const puppeteer = require("puppeteer");
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
  });

  const page = await browser.newPage();
  const url = "https://www.cnblogs.com/";

  await page.goto(url, {
    waitUntil: "networkidle2",
  });

//   await page.click("#sidenav_category > a > span");
//   await page.waitForNavigation();


  const resp = await page.evaluate(() => {
    const urls = []
    u1 = document.querySelectorAll('#site_categories_card > ul');
    for(n1 of u1){
        u2 = n1.querySelectorAll('li')
        for(n2 of u2){
            linkN = n2.querySelector('a')
            urls.push('https://www.cnblogs.com'+linkN.attributes.href.value);
        }
    }
    return {urls}
  });

  const urls = resp.urls;

  const cate_list = [];
  for(cate_url of urls){

    await page.goto(cate_url, {
        waitUntil: "networkidle2",
    });

    const resp = await page.evaluate(() => {
        const text = document.querySelector('#main_flow > div.card > script').text;
        const matchs = text.match(/(?<=\"CategoryId\":).*?(?=,.*)/gi);
        const title = document.querySelector('#post_list_title > div > a').text;

        const title2_node = document.querySelector('#post_list_title > div > a.current');
        
        const title2 = title2_node?title2_node.text:null;
        
        if(matchs.length > 0){
            return {
                title:title2?title2:title,
                CategoryId:matchs[0]
            };
        }
        return null;
    });

    if(resp){
        cate_list.push(resp);
    }   

    console.log(resp)
  }

    if(cate_list.length > 0){
        const cate_obj = {}

        for(item of cate_list){
            cate_obj[item.title] = {cid:item.CategoryId}
        }

        let obj=JSON.stringify(cate_obj,null,'\t')

        fs.writeFileSync('cates.txt',obj)
    
        console.log(cate_obj);

    }


  

  await page.close();
  await browser.close();
})();
