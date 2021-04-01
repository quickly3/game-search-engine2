const puppeteer = require('puppeteer');
const fs = require('fs');

function base64Encode(file) {
    var bitmap = fs.readFileSync(file);
    return new Buffer.from(bitmap).toString('base64');
}

(async () => {
    const browser = await puppeteer.launch();
    const png = '/Users/hongbinzhou/Downloads/cp-hide-btn.png'
    const pdf = '/Users/hongbinzhou/Downloads/cp-hide-btn.pdf'

    const image = 'data:image/png;base64,' + base64Encode(png);

    const page3 = await browser.newPage();
    await page3.goto(image, {waitUntil: 'networkidle2'});
    await page3.pdf({
        landscape:true,
        path: pdf,
        width:'500px'
    });
    // await page3.pdf({path: '/Users/hongbinzhou/Downloads/cp-hide-btn-a4.pdf',format:'A4'});

    await browser.close();
})