const sleep = require('sleep');
const baidu2 = require('./bl2.js');
const google1 = require('./gl1.js');
const google2 = require('./gl2.js');


const bootstrap = async()=>{

    var fs = require('fs');
    var userAgents = fs.readFileSync('user-agents.txt').toString().split("\n");
    var proxys = fs.readFileSync('proxy.txt').toString().split("\n");

    companies = [
        '3S Media','522 Productions','A-Town Bar and Grill','Abbott Laboratories/Quintiles Commercial',
        'Abercrombie & Fitch','Absolute Software','Abstract','Accents by Design','Accenture',
        'Access Funding, LLC','ACE Hardware Corporation','Fortren Funding LLC','Acendre',
        'Achieved Solutions','Acquia','Acterna','Actian, Corporation','Actuate (opentext)',
        'Acuity Audio Visual','AD PAGES MARKETING','ADF Solutions, Inc','Adobe','Adrian College',
        'American University','BaseInfoSec','Adtran','Advance Business Systems',
        'Advanced & Emerging Technologies','Advanced Computer Concepts','Advantage Green, Inc',
        'InceptionPad',
        'Bergen Community College','BoxTone Inc','24 Hour Fitness','2U','3Com Corporation',
        'Advantech','AECOM, Inc','AEG Worldwide','Aerva, Inc','Aether Systems'
    ]

    for (const i in companies) {
        name = companies[i]
        userAgent = userAgents[Math.floor(Math.random() * userAgents.length)]
        // proxy = proxys[Math.floor(Math.random() * proxys.length)]
        ScrapePages = [baidu2,google1,google2]
        ScrapePages = [baidu2]
        _ScrapePage = ScrapePages[Math.floor(Math.random() * ScrapePages.length)]

        console.log(name)
        // console.log(proxy)
        console.log(userAgent)

        options = {
            args: [
                "--disable-gpu",
                "--no-sandbox", 
                `--user-agent=${userAgent}`,
                // `--proxy-server=${proxy}`,
            ],
            headless: false
        }



        const resp = await _ScrapePage(name,options);
        console.log(resp);

        if(resp.msg == 'proxy timeout'){
            return false;
        }

        const random = Math.floor(Math.random() *10 - 5);
        await sleep.sleep(17+random);
    }
}
bootstrap();

