const puppeteer = require('puppeteer');
const fs = require('fs');
const {jsPDF} = require('jspdf');
const AWS  = require('aws-sdk');

function base64Encode(file) {
    var bitmap = fs.readFileSync(file);
    return new Buffer.from(bitmap).toString('base64');
}

function captureDomTOoPDF(png,pdf){
    (async () => {
        const browser = await puppeteer.launch({args: ['--allow-file-access-from-files', '--enable-local-file-accesses']});
        const page = await browser.newPage();
        const image = 'data:image/png;base64,' + base64Encode(png);
        await page.goto(image, {waitUntil: 'networkidle0'});
        await page.pdf({path: pdf, format: 'A4'});
    
        await browser.close();
        console.log("done");
    })();

}

bootstrap = async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const url = 'https://clients.dev.titanhouse.com/titan/93825832-fd5a-4137-b02e-e8ae9115ec63'
  // const url = 'https://clients.dev.titanhouse.com/titan/a176170d-0b19-435f-b8bf-6f4600b9f746'
  
  const width = 1920 
  const height = 3500

  await page.goto(url, {
    waitUntil: 'networkidle2'
  });

  await page.type('input[type=email]', 'tanlu@inceptionpad.com')
  await page.type('input[type=password]', 'Password1!')

  await page.waitForSelector('#root > div > div.App__main-view > div > form > div > div:nth-child(6) > button')
  await page.click('#root > div > div.App__main-view > div > form > div > div:nth-child(6) > button')
  await page.$eval('#root > div > div.App__main-view > div > form > div > div:nth-child(6) > button', (elem) => elem.click())
  await page.waitForNavigation()

  const page2 = page;
  await page2.setViewport({
    width : width,
    height : height,
    deviceScaleFactor : 3
  })

  await page2.goto(url, {
    waitUntil: 'networkidle2'
  });

  await page2.evaluate((sel) => {
      const pdfHideNodes = ['bread-crumb', 'nav-links', 'nav-options', 'actions-wrapper'];

      pdfHideNodes.forEach(selector=>{
        var elements = document.getElementsByClassName(selector);
        elements.forEach((ele) => {
          ele.style.opacity = '0';
        });
      })
  })

  const png = '/Users/hongbinzhou/Downloads/cp-hide-btn.png'
  const pdf = '/Users/hongbinzhou/Downloads/cp-hide-btn.pdf'

  const image_buff = await page2.screenshot({path:png});
  const imageBase64 = 'data:image/jpeg;base64,' + image_buff.toString('base64');

  await page2.evaluate((option) => {
    document.body.innerHTML = "";

    var canvas = document.createElement('canvas');
    canvas.width = option.width*3; 
    canvas.height = option.height*3;
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');

    var image = new Image();
    image.width = option.width*3; 
    image.height = option.height*3;
    image.onload = function() {
      ctx.drawImage(image, 0, 0,option.width,option.height);
    };
    image.src = option.imageBase64;

  },{
    imageBase64,
    width,
    height
  })

    await page2.pdf({
        path: pdf,
        width,
        height,
        landscape:true
    });


  

//   fs.writeFileSync('/Users/hongbinzhou/Downloads/base64.txt',imageBase64);

//   const page3 = await browser.newPage();
//   await page3.setViewport({
//     width,
//     height,
//     deviceScaleFactor : 3
//   })
  
//   await page3.goto(image);
//   await page3.pdf();
//   await page3.pdf({path: '/Users/hongbinzhou/Downloads/cp-hide-btn-a4.pdf',format:'A4'});

  await browser.close();

}

bootstrap();
