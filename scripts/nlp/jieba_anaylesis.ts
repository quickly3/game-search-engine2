const nodejieba = require("nodejieba");


function bootstrap(){
    const list = ["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学", "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"];

    for (const i of list) {
        const result = nodejieba.cut(i);
        console.log(result);   
    }

}

bootstrap();