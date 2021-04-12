const google = async (name,options,browser) => {
    name = name.replace(/ /g,'+')
    url = `https://www.google.com/search?q=site:www.linkedin.com+${name}`;
    const page = await browser.newPage();
    try {
        await page.goto(url, {
            waitUntil: 'networkidle2',
            timeout:5000
        });
    } catch (error) {
        await page.close();
        return {
            success:false,
            msg:'proxy timeout'
        }
    }
    
    robot = false;
    robotNode = 'body > div:nth-child(1) > div > b'
    try {
        await page.waitForSelector(robotNode,{
            timeout:500
        })
        robotTxt = await page.evaluate((robotNode) => {
            node = document.querySelector(robotNode)
            return node?node.textContent:'';
        },robotNode)
        if(robotTxt == 'About this page'){
            robot = true;
        }
    } catch (error) {

    }

    link = '#main > div:nth-child(4) > div > div:nth-child(1) > a'
    link2 = '#rso > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > a'
    link3 = '#rso > div:nth-child(1) > div > div:nth-child(1) > a'
    link4 = '#main > div:nth-child(5) > div > div:nth-child(1) > a'

    
    links = [link,link4,link2,link3]

    linkedin_url = null;
    invalid_keyword = true
    success = false;


    while(!robot && links.length > 0){
        link = links[0]
        links.shift();
        try {
            await page.waitForSelector(link,{
                timeout:500
            })
            linkedin_url = await page.evaluate((link)=>{
                linkNode = document.querySelector(link);
                if(linkNode){
                    return linkNode.getAttribute("href");
                }
            },link)
            if(linkedin_url){
                success = true;
                invalid_keyword = false;
            }
            break;
        } catch (error) {
            if(links.length == 0){
                invalid_keyword = true;
            }
        }
    }

    let resp = {
        success:success,
        invalid_keyword:invalid_keyword,
        linkedin_url:linkedin_url,
        robot:robot
    }

    await page.close();
    return resp;
}

module.exports = google;
