const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--disable-gpu'],
  });
  const page = await browser.newPage();
  const url = 'https://clients.dev.titanhouse.com/titan/93825832-fd5a-4137-b02e-e8ae9115ec63'
  
  const width = 1920 
  let height = 1200

  await page.goto(url, {
    waitUntil: 'networkidle2'
  });

  await page.screenshot();
  const submit = '.submit';
  await page.type('input[type=email]', 'tanlu@inceptionpad.com')
  await page.type('input[type=password]', 'Password1!')
  await page.waitForSelector(submit)
  await page.click(submit)
  await page.waitForNavigation()

  const page2 = page;
  await page2.setViewport({
    width : width,
    height : height
  })

  await page2.goto(url, {
    waitUntil: 'networkidle2'
  });
  await browser.close();
 
})();
