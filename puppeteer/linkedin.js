const sleep = require('sleep');
const baidu2 = require('./bl2.js');
const google1 = require('./gl1.js');
const google2 = require('./gl2.js');
const ObjectsToCsv = require('objects-to-csv')
var fs = require('fs');



const bootstrap = async()=>{

    let start = Date.parse(new Date());

    var userAgents = fs.readFileSync('user-agents.txt').toString().split("\n");
    var proxys = fs.readFileSync('proxy.txt').toString().split("\n");

    file1 = './linkedin_company.csv';
    file2 = './failed_agents.csv';
    file3 = './failed_company.csv';
    file4 = './failed_robot.csv';

    [file1,file2,file3].map((file)=>{
        if(fs.existsSync(file)){
            fs.unlinkSync(file)
        }
    })


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
    lastComapnyRetry = 0;

    while(companies[0]){
        name = companies[0]
        userAgent = userAgents[Math.floor(Math.random() * userAgents.length)]

        // userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"

        // Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0
        proxy = proxys[Math.floor(Math.random() * proxys.length)]
        ScrapePages = [baidu2,google1,google2]
        // ScrapePages = [baidu2]

        _ScrapePage = ScrapePages[Math.floor(Math.random() * ScrapePages.length)]
        
        options = {
            args: [
                "--disable-gpu",
                `--user-agent=${userAgent}`,
                // `--proxy-server=${proxy}`,
            ],
            headless: true
        }

        const resp = await _ScrapePage(name,options);

        resp.keyword = name;
        resp.search_engine = _ScrapePage.name;
        resp.user_agent = userAgent;
        let current = Date.parse(new Date());
        resp.cost = Math.floor((current-start)/1000);
        console.log(resp);

        if(!resp.success){

            if(resp.msg == 'engine page failed'){
                const csvFailed = new ObjectsToCsv([{user_agent:resp.user_agent}]);
                await csvFailed.toDisk(file2,{append:true});
            }

            if(resp.msg == 'robot found'){
                const csvFailed = new ObjectsToCsv([{
                    user_agent:resp.user_agent,
                    search_engine:userAgent
                }]);
                await csvFailed.toDisk(file4,{append:true});
            }

            if(resp.msg == 'Linnkedin Render failed'){
                lastComapnyRetry = lastComapnyRetry + 1
            }
        }

        if(resp.success && (lastComapnyRetry < 5)){
            lastComapnyRetry = 0;
            const csv = new ObjectsToCsv([resp]);
            await csv.toDisk(file1,{append:true});

            companies.shift();
            if(companies.length ==  0){
                console.log('end');
                return false;
            }
            
        }else{
            if(lastComapnyRetry == 5){
                companies.shift();
                if(companies.length ==  0){
                    console.log('end');
                    return false;
                }
                const companyFailed = new ObjectsToCsv([{name:resp.keyword}]);
                await companyFailed.toDisk(file3,{append:true});
                lastComapnyRetry = 0;
            }

        }

        const random = Math.floor(Math.random() *10 - 5);
        await sleep.sleep(17+random);
    }
}
bootstrap();

