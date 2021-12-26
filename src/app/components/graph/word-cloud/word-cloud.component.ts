import { Component, Input, OnInit } from "@angular/core";
import * as d3 from 'd3';
import * as d3Cloud from "d3-cloud";
import { Primitive } from "d3";
import { Word } from "d3-cloud";

@Component({
  selector: "app-word-cloud",
  templateUrl: "./word-cloud.component.html",
  styleUrls: ["./word-cloud.component.scss"],
})
export default class WordCloudComponent implements OnInit {
  @Input() words: any[] = [];
  private svg: any;
  @Input() dataId = 'defaultId';
  @Input() clickTextFunc = null;

  mainSelector
  maxCount
  maxSize = 40;
  baseSize = 12;

  ngOnInit(): void {

  }

  sizeInterpolate(count){
    const interpolate = d3.interpolateRound(0, this.maxSize);
    return interpolate(count/this.maxCount);
  }

  ngOnChanges(): void {
    this.mainSelector = `figure#${this.dataId}`;

    if(!d3.select(this.mainSelector).node()){
        return null;
    }

    this.maxCount = d3.max(this.words.map(w=>w.doc_count));

    const svg = this.WordCloud(this.words, {
        width: 1280,
        height: 600,
      });

    d3.select(this.mainSelector).html('');
    const node = d3.select(this.mainSelector).node().append(svg);
  }

  WordCloud = (
    words,
    {
      size = (group) => {
          return this.sizeInterpolate(group[0].doc_count);
      }, // Given a grouping of words, returns the size factor for that word
      word = (d) => d.key, // Given an item of the data array, returns the word
      marginTop = 0, // top margin, in pixels
      marginRight = 0, // right margin, in pixels
      marginBottom = 0, // bottom margin, in pixels
      marginLeft = 0, // left margin, in pixels
      width = 640, // outer width, in pixels
      height = 400, // outer height, in pixels
      maxWords = 200, // maximum number of words to extract from the text
      fontFamily = "sans-serif", // font family
      fontScale = 15, // base font size
      padding = 0, // amount of padding between the words (in pixels)
      rotate = 0, // a constant or function to rotate the words
      invalidation, // when this promise resolves, stop the simulation
    }: any
  ) => {
    const data = d3
      .rollups(words.map(w=>w), size, (w) => w)
      .sort(([, a], [, b]) => {
        return d3.descending((a as Primitive), (b as Primitive));
      })
      .slice(0, maxWords)
      .map((dataList) => {
        const [key, size] = dataList;
        const sizeRate = (key as any).doc_count/this.maxCount;
        return ({ text: word(key), size, sizeRate })
      });
    
    const svg = d3
      .create("svg")
      .attr("viewBox", `0, 0, ${width}, ${height}`)
      .attr("width", width)
      .attr("font-family", fontFamily)
      .attr("text-anchor", "middle")
      .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

    const g = svg
      .append("g")
      .attr("transform", `translate(${marginLeft},${marginTop})`);

    const cloud = d3Cloud()
      .size([
        width - marginLeft - marginRight,
        height - marginTop - marginBottom,
      ])
      .words((data as Word[]))
      .padding(padding)
      .rotate(rotate)
      .font(fontFamily)
      .fontSize((d) => Math.sqrt(d.size) * fontScale)
      .on("word", (d:any) => {
        const { size, x, y, rotate, text, sizeRate} = d;
        // const curColor = d3.interpolateViridis(1-sizeRate);
        const curColor = d3.schemeCategory10[Math.ceil(Math.random()*10)]
        g.append("text")
          .attr("font-size", size)
          .attr("fill",curColor)
          .attr("class","cloud-cell")
          .attr("transform", `translate(${x},${y}) rotate(${rotate})`)
          .text(text)
          .on('click',(e)=>{
            if(this.clickTextFunc){
              // console.log(e.target.textContent)
              this.clickTextFunc(e.target.textContent);
            }
          })
      });

    cloud.start();
    invalidation && invalidation.then(() => cloud.stop());
    return svg.node();
  };
}
