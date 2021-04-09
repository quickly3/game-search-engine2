const bl_login = async(name,options,browser)=>{
    
    url = `https://www.baidu.com/s?wd=site%3Alinkedin.com%20${encodeURI(name)}`;

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

    link = '#content_left > div:nth-child(1)  > h3 > a'
    try {
        await page.waitForSelector(link,{
            timeout:5000
        })
    } catch (error) {
        await page.close();
        return {
            success:false,
            msg:'engine page failed'
        }
    }

    const linkNode = await page.$(link); 
    const newPagePromise = new Promise(x => browser.once('targetcreated', target => x(target.page())));
    await linkNode.click({button: 'middle'});    

    const page2 = await newPagePromise; 

    linkedin_url = null;
    invalid_keyword = true
    success = false;
    
    page2.on('response', response => {
        status = response.status()
        if ((status >= 300) && (status <= 399)) {
            redirect_url = response.headers()['location'];
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
            }
        }
    })

    await page2.bringToFront();     
    await page2.waitForTimeout(7000)
   
    let resp = {
        success:success,
        invalid_keyword:invalid_keyword,
        linkedin_url:linkedin_url,
        robot:false
    }

    await page.close();
    await page2.close();
    return resp;

}
module.exports = bl_login;
