const bing = async(name,options,browser)=>{
    
    url = `https://www.bing.com/search?q=site%3a(www.linkedin.com)+${encodeURI(name)}`;

    const page = await browser.newPage();
    try {
        await page.goto(url, {
            waitUntil: 'domcontentloaded',
            timeout:5000
        });
    } catch (error) {
        console.log(error)
        await page.close();
        return {
            success:false,
            msg:'proxy timeout'
        }
    }

    linkedin_url = null;
    invalid_keyword = true
    success = false;

    link = '#b_results > li:nth-child(1) > h2 > a'
    try {
        await page.waitForSelector(link,{
            timeout:5000
        })

        redirect_url = await page.evaluate((link)=>{
            linkNode = document.querySelector(link);
            if(linkNode){
                return linkNode.getAttribute("href");
            }
        },link)

        if(redirect_url && redirect_url.indexOf('https://www.linkedin.com')>-1){
            linkedin_url = redirect_url;
            success = true
            invalid_keyword = false;

            if(redirect_url.indexOf('https://www.linkedin.com/jobs')>-1){
                success = false;
                invalid_keyword = true;
                linkedin_url = null;
            }

            if(redirect_url.indexOf('https://www.linkedin.com/in')>-1){
                success = false;
                invalid_keyword = true;
                linkedin_url = null;
            }

            if(redirect_url.indexOf('https://www.linkedin.com/pulse')>-1){
                success = false;
                invalid_keyword = true;
                linkedin_url = null;
            }
        }

        let resp = {
            success:success,
            invalid_keyword:invalid_keyword,
            linkedin_url:linkedin_url,
            msg:'',
            robot:false
        }
        await page.close();
        return resp;

    } catch (error) {
        await page.close();
        return {
            success:false,
            invalid_keyword:true,
            msg:'engine page failed'
        }
    }




}
module.exports = bing;
