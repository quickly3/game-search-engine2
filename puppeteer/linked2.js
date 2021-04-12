const sleep = require('sleep');
const google = require('./google.js');
const baidu = require('./bl_login.js');



const ObjectsToCsv = require('objects-to-csv')
var fs = require('fs');
const puppeteer = require('puppeteer');

const bootstrap = async()=>{

    let start = Date.parse(new Date());

    var userAgents = fs.readFileSync('user-agents.txt').toString().split("\n");
    var proxys = fs.readFileSync('proxy.txt').toString().split("\n");

    file1 = './companies_linkedin.csv';
    file2 = './failed_agents.csv';
    file4 = './failed_robot.csv';

    [file1,file2,file4].map((file)=>{
        if(fs.existsSync(file)){
            fs.unlinkSync(file)
        }
    })
    companies_file = './companies.csv';
    data = fs.readFileSync(companies_file);

    var companies = data.toString().split("\n");
    companies.shift();

    companies = companies.map(e=>e.replace(/\"/g,""));

    // companies = [
    //     'Acterna',
    //     'Access Funding, LLC','ACE Hardware Corporation','Fortren Funding LLC','Acendre',
    //     '3S Media','522 Productions','A-Town Bar and Grill','Abbott Laboratories/Quintiles Commercial',
    //     'Abercrombie & Fitch','Absolute Software','Abstract','Accents by Design','Accenture',
    //     'Achieved Solutions','Acquia','Acterna','Actian, Corporation','Actuate (opentext)',
    //     'Acuity Audio Visual','AD PAGES MARKETING','ADF Solutions, Inc','Adobe','Adrian College',
    //     'American University','BaseInfoSec','Adtran','Advance Business Systems',
    //     'Advanced & Emerging Technologies','Advanced Computer Concepts','Advantage Green, Inc',
    //     'InceptionPad',
    //     'Bergen Community College','BoxTone Inc','24 Hour Fitness','2U','3Com Corporation',
    //     'Advantech','AECOM, Inc','AEG Worldwide','Aerva, Inc','Aether Systems'
    // ]
    lastComapnyRetry = 0;

    // userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"

    userAgent = userAgents[Math.floor(Math.random() * userAgents.length)]
    headless = true

    options = {
        args: [
            "--disable-gpu",
            `--user-agent=${userAgent}`,
            // `--proxy-server=${proxy}`,
        ],
        headless: headless
    }

    let browser = await puppeteer.launch(options);

    while(companies[0]){
        name = companies[0]


        // Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
        proxy = proxys[Math.floor(Math.random() * proxys.length)]
        // ScrapePages = [baidu2,google1,google2]
        ScrapePages = [google]

        _ScrapePage = ScrapePages[Math.floor(Math.random() * ScrapePages.length)]
        

        const resp = await _ScrapePage(name,options,browser);

        resp.keyword = name;
        resp.search_engine = _ScrapePage.name;
        resp.user_agent = userAgent;
        let current = Date.parse(new Date());
        resp.cost = Math.floor((current-start)/1000);
        console.log(resp);
        missing = false

        if(!resp.msg){
            resp.msg = ''
        }

        next = false
        if(!resp.success){

            if(resp.msg == 'engine page failed'){
                const csvFailed = new ObjectsToCsv([{user_agent:resp.user_agent}]);
                await csvFailed.toDisk(file2,{append:true});
            }

            if(resp.robot){
                lastComapnyRetry = lastComapnyRetry + 1

                userAgent = userAgents[Math.floor(Math.random() * userAgents.length)]
                options = {
                    args: [
                        "--disable-gpu",
                        `--user-agent=${userAgent}`,
                        // `--proxy-server=${proxy}`,
                    ],
                    headless:headless
                }
                await browser.close();
                browser = await puppeteer.launch(options);

            }

            if(resp.msg == 'Linnkedin Render failed'){
                lastComapnyRetry = lastComapnyRetry + 1
            }

            if(resp.invalid_keyword){
                const csv = new ObjectsToCsv([{
                    "company":resp.keyword,
                    "linkedin_url":resp.linkedin_url,
                    "time cost":resp.cost,
                    "msg":"no available result",
                    "success":resp.success.toString()
                }]);
                await csv.toDisk(file1,{append:true});
                next = true;
            }

            if(lastComapnyRetry == 5){
                const companyFailed = new ObjectsToCsv([{
                    "company":resp.keyword,
                    "linkedin_url":resp.linkedin_url,
                    "time cost":resp.cost,
                    "msg":"",
                    "success":resp.success.toString()
                }]);
                await companyFailed.toDisk(file1,{append:true});
                lastComapnyRetry = 0;
                next = true;
            }

        }else{
            lastComapnyRetry = 0;
            const csv = new ObjectsToCsv([{
                "company":resp.keyword,
                "linkedin_url":resp.linkedin_url,
                "time cost":resp.cost,
                "msg":"",
                "success":resp.success.toString()
                
            }]);
            await csv.toDisk(file1,{append:true});
            next = true;
        }

        if(next){
            if(companies.length ==  0){
                console.log('end');
                return false;
            }
            companies.shift();
        }

        const random = Math.floor(Math.random() * 10 - 5);
        await sleep.sleep(10+random);
    }
}
bootstrap();

