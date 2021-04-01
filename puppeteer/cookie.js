const puppeteer = require('puppeteer');
// const fs = require('fs');
// const {jsPDF} = require('jspdf');
// const AWS  = require('aws-sdk');

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
  });
  const page = await browser.newPage();
  const url = 'https://clients.dev.titanhouse.com/titan/93825832-fd5a-4137-b02e-e8ae9115ec63'
  
  // const width = 1920 
  // let height = 1200

  await page.goto(url, {
    waitUntil: 'networkidle2'
  });



  const submit = '.submit';
  await page.type('input[type=email]', 'tanlu@inceptionpad.com')
  await page.type('input[type=password]', 'Password1!')

  await page.waitForSelector(submit)
  await page.click(submit)
  await page.waitForNavigation()


  const page2 = page;
  // await page2.setViewport({
  //   width : width,
  //   height : height
  // })

  await page2.goto(url, {
    waitUntil: 'networkidle2'
  });

  // const resp = await page2.evaluate(() => {
  //     const pdfHideNodes = ['bread-crumb', 'nav-links', 'nav-options', 'actions-wrapper'];
  //     const pdfBlurNodes = ['userPhoto', 'media-panel', 'resume-label', 'exp_position', 'exp_company'];
     
  //     pdfBlurNodes.forEach(selector=>{
  //       var elements = document.getElementsByClassName(selector);
  //       elements.forEach((ele) => {
  //         ele.style.filter = "blur(10px)";
  //       });
  //     })

  //     pdfHideNodes.forEach(selector=>{
  //       var elements = document.getElementsByClassName(selector);
  //       elements.forEach((ele) => {
  //         ele.style.opacity = '0';
  //       });
  //     })

  //     return {
  //       clientHeight:document.body.clientHeight,
  //       scrollHeight:document.body.scrollHeight      
  //     }
  // })


  // height = resp.clientHeight

  // await page2.setViewport({
  //   width : width,
  //   height : height,
  //   deviceScaleFactor : 3
  // })

  // const pdf = '/Users/hongbinzhou/Downloads/final.pdf'

  // const image_buff = await page2.screenshot({type:'jpeg',fullPage:true});


  // const image = 'data:image/jpeg;base64,' + image_buff.toString('base64');

  await browser.close();


  // if (width > height) {
  //   _pdf = new jsPDF('landscape', 'pt', [width, height]);
  // } else {
  //   _pdf = new jsPDF('', 'pt', [width, height]);
  // }

  // _pdf.addImage(image, 'JPEG', 0, 0, width, height);
  // _pdf.save(pdf)

})();
