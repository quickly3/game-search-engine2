import { Client } from "@elastic/elasticsearch";
import * as _ from "lodash";
import * as extractDomain from "extract-domain";
import * as Papa from "papaparse";
import * as fs from "fs";

const config = require("dotenv").config({ path: "../../.env" }).parsed;

const ES_HOST = config.ES_HOST.replace("http://", "");
const ES_PORT = config.ES_PORT;
const ES_USER = config.ES_USER;
const ES_PWD = config.ES_PWD;

const es_url = `http://${ES_USER}:${ES_PWD}@${ES_HOST}:${ES_PORT}`;
const es = new Client({ node: es_url });

class DomainQuery {
  scrollId;
  domains = [];
  urls = [];
  total_value = 0;
  count = 0;
  hits_cnt = 0;

  getDomains(resp) {
    const hits = _.get(resp, "hits.hits");
    const urls = hits.map((i) => i._source.url);

    const domains = extractDomain(urls);


    for(const hit of hits){
      const url = hit._source.url;
      const title = hit._source.title.trim();
      const created_at = hit._source.created_at;

      this.urls.push({
        domain:extractDomain(url),
        url,
        title,
        created_at
      });
    }

    for (const d of domains) {
      let found = false;
      for (const d2 of this.domains) {
        if (d2.domain === d) {
          found = true;
          d2.cnt++;
          continue;
        }
      }
      if (!found) {
        this.domains.push({
          domain: d,
          cnt: 1,
        });
      }
    }
  }

  async query() {
    const resp = await es.search({
      index: "article",
      scroll: "30s",
      query: {
        query_string: {
          query: "source:escn",
        },
      },
      _source: ["url","title","created_at"],
      size: 500,
    });

    this.scrollId = resp._scroll_id;
    this.total_value = _.get(resp, "hits.total.value");

    this.hits_cnt = _.get(resp, "hits.hits").length;
    this.count = this.count + this.hits_cnt;

    console.log(`${this.count}/${this.total_value}`);

    if (this.total_value > 0) {
      this.getDomains(resp);
      await this.next_scroll();
    }

    this.domains = _.sortBy(this.domains, ["cnt"]);
    this.urls = _.sortBy(this.urls, ["domain"]);

    console.log(this.domains);

    const outputstr = Papa.unparse(this.domains, { header: true });
    fs.writeFileSync("linked_companies.csv", outputstr, "utf8");


    const outputstr2 = Papa.unparse(this.urls, { header: true });
    fs.writeFileSync("urls.csv", outputstr2, "utf8");

  }

  async next_scroll() {
    while (this.hits_cnt > 0) {
      const resp = await es.scroll({
        scroll_id: this.scrollId,
        scroll: "30s",
      });

      this.scrollId = resp._scroll_id;
      this.hits_cnt = _.get(resp, "hits.hits").length;

      this.count = this.count + this.hits_cnt;
      console.log(`${this.count}/${this.total_value}`);

      if (this.hits_cnt > 0) {
        this.getDomains(resp);
      }
    }
  }
}

const domainQuery = new DomainQuery();

domainQuery.query();
