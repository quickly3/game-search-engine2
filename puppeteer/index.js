const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();

    browser.on('targetchanged', async (target) => {
        const targetPage = await target.page();
        const client = await targetPage.target().createCDPSession();
        await client.send('Runtime.evaluate', {
          expression: `
            localStorage.setItem('auth::token', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyZGZlY2UwMC03ZmQ0LTExZWItOTBmYy1mOTE1NmJjZDQ1YjMiLCJpYXQiOjE2MTUxODM0ODQsImV4cCI6MTYxNTI2OTg4NH0.SlCQ9TRtcE7D5708FBFy_EYEVxJFxIg-9t23vgldrFo');
            localStorage.setItem('auth::user', '{"id":75,"username":"tanlu@inceptionpad.com","id_organization":"a482835b-0cb5-41b4-9457-e9722a3055e7","firstName":"Tan","lastName":"Lu","Client":{"id":"a482835b-0cb5-41b4-9457-e9722a3055e7","name":"TitanHouse Inc","restrictEmail":false,"restrictSearch":false,"deleted":false,"type":null,"ClientUser":{"role":"SUPER_ADMIN","feature":null},"url":"http://titanhouse.com"},"company":"TitanHouse","position":"CTO","termsCon":true,"displayTitanAge":true,"displayWelcomeTour":false,"displayMergeHelp":null,"profileImageUrl":null,"role":"SUPER_ADMIN","feature":[],"roles":["SUPER_ADMIN"]}');
            `,
        });
    });

    const page = await browser.newPage();
  
    await page.goto('https://clients.dev.titanhouse.com/titan/a176170d-0b19-435f-b8bf-6f4600b9f746', {
      waitUntil: 'networkidle2'
    });

    // await page.pdf({ path: '/Users/hongbinzhou/Downloads/c1.pdf' });
    await page.screenshot({path: '/Users/hongbinzhou/Downloads/c1.png'});

    await browser.close();
})();