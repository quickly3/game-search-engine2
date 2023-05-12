/* Created by iflytek on 2020/03/01.
 *
 * 运行前：请先填写 appid、apiSecret、apiKey
 * 
 * 在线语音合成调用demo
 * 此demo只是一个简单的调用示例，不适合用到实际生产环境中
 *
 * 在线语音合成 WebAPI 接口调用示例 接口文档（必看）：https://www.xfyun.cn/doc/tts/online_tts/API.html
 * 错误码链接：
 * https://www.xfyun.cn/document/error-code （code返回错误码时必看）
 * 
 */
const CryptoJS = require('crypto-js')
const WebSocket = require('ws')
var log = require('log4node')
var fs = require('fs')

// 系统配置 
const config = {
    // 请求地址
    hostUrl: "wss://tts-api.xfyun.cn/v2/tts",
    host: "tts-api.xfyun.cn",
    //在控制台-我的应用-在线语音合成（流式版）获取
    appid: "55ba1c61",
    //在控制台-我的应用-在线语音合成（流式版）获取
    apiSecret: "YmYzMmY1MmVmYmJjZmFkNGIzNTJiY2I0",
    //在控制台-我的应用-在线语音合成（流式版）获取
    apiKey: "16a3e3c36b43bd1ae26cf234e40fcfc8",
    text: `我是一名热爱生活、学习和编程的程序员，外向且严肃又活泼。小时候随军在广东生活，初中回成都，大学在山东读书。现在我住在欢乐谷附近，利用远程办公服务为美软件开发。

    我的父亲已去世多年，母亲已退休多年，她经常旅行和徒步旅行。家里有几套老房子，但我也有独立购房的能力，只是因为交通拥堵，我没有买车。
    
    我在职场里是一个刻苦学习的人，我一直保持着对学习的热情和求知欲。在生活中，我喜欢简简单单地生活，下班后会研究技术、打游戏或者和几个好友一起打球和吃饭。
    
    我有很好的生活习惯，包括健康的饮食、早起早睡、早锻炼等。我没有挥霍浪费的习惯，更多地是在科技产品和体育运动方面进行消费，同时也是稳健型理财选手。
    
    希望这些信息可以让您更了解我。`,
    uri: "/v2/tts",
    aue: "lame"
}

// 获取当前时间 RFC1123格式
let date = (new Date().toUTCString())
// 设置当前临时状态为初始化

let wssUrl = config.hostUrl + "?authorization=" + getAuthStr(date) + "&date=" + date + "&host=" + config.host
let ws = new WebSocket(wssUrl)

// 连接建立完毕，读取数据进行识别
ws.on('open', () => {
    log.info("websocket connect!")
    send()
    // 如果之前保存过音频文件，删除之
    if (fs.existsSync('./test.mp3')) {
        fs.unlink('./test.mp3', (err) => {
            if (err) {
                log.error('remove error: ' + err)   
            }
        })
    }
})

// 得到结果后进行处理，仅供参考，具体业务具体对待
ws.on('message', (data, err) => {
    if (err) {
        log.error('message error: ' + err)
        return
    }

    let res = JSON.parse(data)

    if (res.code != 0) {
        log.error(`${res.code}: ${res.message}`)
        ws.close()
        return
    }

    let audio = res.data.audio
    let audioBuf = Buffer.from(audio, 'base64')
    
    save(audioBuf)

    if (res.code == 0 && res.data.status == 2) {
        ws.close()
    }
})

// 资源释放
ws.on('close', () => {
    log.info('connect close!')
})

// 连接错误
ws.on('error', (err) => {
    log.error("websocket connect err: " + err)
})

// 鉴权签名
function getAuthStr(date) {
    let signatureOrigin = `host: ${config.host}\ndate: ${date}\nGET ${config.uri} HTTP/1.1`
    let signatureSha = CryptoJS.HmacSHA256(signatureOrigin, config.apiSecret)
    let signature = CryptoJS.enc.Base64.stringify(signatureSha)
    let authorizationOrigin = `api_key="${config.apiKey}", algorithm="hmac-sha256", headers="host date request-line", signature="${signature}"`
    let authStr = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(authorizationOrigin))
    return authStr
}

// 传输数据
function send() {
    let frame = {
        // 填充common
        "common": {
            "app_id": config.appid
        },
        // 填充business
        "business": {
            "aue": "lame",
            "auf": "audio/L16;rate=16000",
            "vcn": "x4_lingxiaolu_em_v2",
            "tte": "UTF8",
            "sfl": 1
        },
        // 填充data
        "data": {
            "text": Buffer.from(config.text).toString('base64'),
            "status": 2
        }
    }
    ws.send(JSON.stringify(frame))
}

// 保存文件
function save(data) {
    fs.writeFile('./test.mp3', data, { flag: 'a' }, (err) => {
        if (err) {
            log.error('save error: ' + err)
            return 
        }

        log.info('文件保存成功')
    })
}