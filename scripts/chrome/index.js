function download(src) {
    var $a = document.createElement('a');
    $a.setAttribute("href", src);
    var fileInfos = src.split("/")
    var fileName = fileInfos[fileInfos.length - 1]
    fileName = fileName.replace('.jpg','.gif')
    $a.setAttribute("download", fileName);
    var evObj = document.createEvent('MouseEvents');
    evObj.initMouseEvent('click', true, true, window, 0, 0, 0, 0, 0, false, false, true, false, 0, null);
    $a.dispatchEvent(evObj);
};

// $$("#link-report > div > div > div:nth-child(30) > div > img").map(function(img){
//     console.log(img)
// })


// $x('*[@id="link-report"]/div/div/div[16]/div/img').forEach(function(a,i){
//     console.log(a)
// });

const urls = $x('/html/body/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/div/img').map(function(img){
    url = img.getAttribute('data-original-url')
    return url
})

urls.join("\n\r")


const img_urls = $x('//*[@id="link-report"]/div/div/div/div/img').map(function(img){
  url = img.getAttribute('src')
  return url
})

img_urls.join("\n\r")




const downloadImage = (imageUrl, name) => {
    fetch(imageUrl, {
      method: 'get',
      mode: 'cors',
    })
      .then((response) => response.blob())
      .then((data) => {
        const downloadUrl = window.URL.createObjectURL(new Blob([data]));
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.setAttribute('download', name);
        document.body.appendChild(link);
        link.click();
        link.remove();
      });
  };






for(const i in urls){
    setTimeout(()=>{
        console.log(urls[i])
        download(urls[i])
    },i*1000);
}