import { Client } from "@elastic/elasticsearch";
const config = require("dotenv").config({ path: "../../.env" }).parsed;

const ES_HOST = config.ES_HOST.replace("http://", "");
const ES_PORT = config.ES_PORT;
const ES_USER = config.ES_USER;
const ES_PWD = config.ES_PWD;

const es_url = `http://${ES_USER}:${ES_PWD}@${ES_HOST}:${ES_PORT}`;
const es = new Client({ node: es_url });

async function bootstrap() {
  const resp = await es.search({
    index: "article",
    query: {
      query_string: {
        query: "source:escn",
      },
    },
  });

  console.log(resp.hits.hits);
}

bootstrap();
