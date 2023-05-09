import { SpeechSynthesizer } from "alibabacloud-nls";
import * as dotenv from "dotenv";
const fs = require("fs");
const readline = require("readline");
const sleep = (waitTimeInMs) =>
  new Promise((resolve) => setTimeout(resolve, waitTimeInMs));
const args = process.argv.slice(2);

dotenv.config({
  path: "../../.env",
});

const APPKEY = process.env.ALI_APPKEY;
const TOKEN = process.env.ALI_TOKEN;
const URL = process.env.TTS_URL;

const config = {
  url: URL,
  appKey: APPKEY,
  token: TOKEN,
};

const tts = new SpeechSynthesizer(config);

let b1 = [];
let loadIndex = 0;
let needDump = true;

async function runOnce(line) {
  loadIndex++;

  let dumpFile = fs.createWriteStream(`test.wav`, { flags: "w" });
  let tts = new SpeechSynthesizer({
    url: URL,
    appkey: APPKEY,
    token: TOKEN,
  });

  tts.on("meta", (msg) => {
    console.log("Client recv metainfo:", msg);
  });

  tts.on("data", (msg) => {
    console.log(`recv size: ${msg.length}`);
    console.log(dumpFile.write(msg, "binary"));
  });

  tts.on("completed", (msg) => {
    console.log("Client recv completed:", msg);
  });

  tts.on("closed", () => {
    console.log("Client recv closed");
  });

  tts.on("failed", (msg) => {
    console.log("Client recv failed:", msg);
  });

  let param = tts.defaultStartParams();
  param.text = line;
  param.voice = "zhimiao_emo";
  try {
    await tts.start(param, true, 6000);
  } catch (error) {
    console.log("error on start:", error);
    return;
  } finally {
    dumpFile.end();
  }
  console.log("synthesis done");
  await sleep(2000);
}

async function bootstrap() {
  console.log("load test case:", args[0]);
  const fileBuffer = fs.readFileSync(args[0]);
  const text = fileBuffer.toString();

  await runOnce(text);
}
bootstrap();
