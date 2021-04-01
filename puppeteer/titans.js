const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();

    browser.on('targetchanged', async (target) => {
        const targetPage = await target.page();
        const client = await targetPage.target().createCDPSession();
        await client.send('Runtime.evaluate', {
          expression: `
            localStorage.setItem('refreshToken', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjRjMjVmMDU0LTkxZGEtNGYxNC05NDgzLWJjNjMxOTcyMzIwMyIsImV4cGlyZSI6IjIwMjEtMDMtMTVUMDg6MTM6NDUuMTAwWiJ9.jlUMuBE76Q8WcFvarnCtO-qQ_Un7NKzjU3O08P2-f3s');
            localStorage.setItem('token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImEwMjM3ZDljLWM3MzQtNDYyNS1hY2NkLWI4ZWI3MmQwNTMyYyIsImVtYWlsIjoid3VqaWFudGFvK3Rlc3QxQGluY2VwdGlvbnBhZC5jb20iLCJhY3RpdmUiOnRydWUsInRpdGFuSWQiOiIwMjA1YTRjZS0yMTlhLTQ3NTgtYjliYi1jNDJhNmI0OTY1ZjQiLCJyZWdpc3RlcmVkIjp0cnVlLCJmaXJzdE5hbWUiOiJKaWFuIiwibGFzdE5hbWUiOiJUYW8iLCJhY2NvdW50RW1haWwiOiJ3dWppYW50YW8rdGVzdDFAaW5jZXB0aW9ucGFkLmNvbSIsInByZWZlcnJlZEVtYWlsIjoid3VqaWFudGFvK3Rlc3QxQGluY2VwdGlvbnBhZC5jb20iLCJleHBpcmUiOiIyMDIxLTAzLTA4VDA5OjEzOjQ1LjEwMFoifQ.b0NDCs7rUaj3XJzZUQLOtJlNKZ8QZ9tW1ZPZ3u6XfrM');
            localStorage.setItem('userId', 'a0237d9c-c734-4625-accd-b8eb72d0532c');
            localStorage.setItem('tokenExpire', '2021-03-08T09:13:45.100Z');
            `,
        });
    });

    const page = await browser.newPage();
  
    await page.goto('https://titans.dev.titanhouse.com/profile', {
      waitUntil: 'networkidle2'
    });

    // await page.pdf({ path: '/Users/hongbinzhou/Downloads/c1.pdf' });
    await page.screenshot({path: '/Users/hongbinzhou/Downloads/titan.png'});

    await browser.close();
})();