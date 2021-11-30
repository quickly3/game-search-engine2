// @ts-nocheck
import { Component, Input, OnChanges, OnInit } from '@angular/core';
import * as d3 from 'd3';
import { Datum } from 'src/app/interface/Datum';
import * as _ from 'lodash';

@Component({
    selector: 'app-bubble',
    templateUrl: './bubble.component.html',
    styleUrls: ['./bubble.component.scss']
})
export default class BubbleComponent implements OnInit, OnChanges {

    @Input() data: Datum[] = [];
    @Input() dataId = '';
    @Input() textSize = '1rem';
    @Input() radiusFix = null;

    private svg: any;

    ngOnInit(): void {
        this.drawBubble();
    }

    ngOnChanges(): void {
        this.drawBubble();
        // this.d3ArrayStatistics();
        // this.d3ArraySearch();

        // this.d3ArrayBin();
        // this.d3Iterable();
        // this.d3Transformations();
        if (this.data.length > 20){
          this.d3Colors();
        }
    }

    private drawBubble(): void {
        const options = {
            name: d => d.name,
            value: d => d.value,
            group: d => d.name,
            title: d => d.name,
            colors: d3.schemeTableau10,
            width: 1960
          };

        const chart = this.BubbleChart(this.data, options);
    }

    d3Colors():void {
      console.log('colors1', d3.interpolateSpectral(0));
      console.log('colors2', d3.interpolateSpectral(1));

      console.log('colors3', d3.schemeSpectral);
      console.log('colors4', d3.schemeSpectral);


    }

    d3Transformations(): void {
      if (this.data.length > 20){
        const dataArr = this.data;
        const valueArr = this.data.map(i => i.value).sort((a, b) => a - b);
        console.log('transformation');
        console.log('group');
        console.log(d3.group(dataArr,i => i.value));
      }
    }

    d3ArrayStatistics(): void{
      if (this.data.length > 20){
        console.log(this.data);
        const dataArr = this.data.map(i => i.value);
        console.log('min');
        console.log(d3.min(dataArr));
        console.log('minIndex');
        console.log(d3.minIndex(dataArr));
        console.log('max');
        console.log(d3.max(dataArr));
        console.log('maxIndex');
        console.log(d3.maxIndex(dataArr));
        console.log('extent');
        console.log(d3.extent(dataArr));
        console.log('median');
        console.log(d3.median(dataArr));
        console.log('mode');
        console.log(d3.mode(dataArr));
        console.log('cumsum');
        console.log(d3.cumsum(dataArr));
        console.log('rank');
        console.log(d3.rank(dataArr));
        console.log('quantile');
        console.log(d3.quantile(dataArr, 0.5));
        console.log('quantileSorted');
        console.log(d3.quantileSorted(dataArr, 0.5));
        console.log('variance');
        console.log(d3.variance(dataArr));
        console.log('deviation');
        console.log(d3.deviation(dataArr));
        console.log('fcumsum');
        console.log(d3.fcumsum(dataArr));
        console.log('fsum');
        console.log(d3.fsum(dataArr));
      }
    }

    d3ArraySearch(): void{
      if (this.data.length > 20){
        const dataArr = this.data;
        const valueArr = this.data.map(i => i.value).sort((a, b) => a - b);
        // console.log(valueArr);
        console.log('least');
        console.log(d3.least(dataArr, (a, b) => a.value - b.value));
        console.log('leastIndex');
        console.log(d3.leastIndex(dataArr, (a, b) => a.value - b.value));

        console.log('bisect');
        console.log(d3.bisect(valueArr, 2196));
        console.log('bisectLeft');
        console.log(d3.bisectLeft(valueArr, 2196));
        console.log('bisectRight');
        console.log(d3.bisectRight(valueArr, 2196));
        console.log('bisectCenter');
        console.log(d3.bisectCenter(valueArr, 2196));


        console.log(d3.bisector((a: any, b: any) => a.value - b.value));
        console.log('quickselect');
        console.log(d3.quickselect(valueArr, 40).join('-'));
        console.log(d3.quickselect(valueArr, 60).join('-'));


      }
    }

    d3ArrayBin(): void{
      if (this.data.length > 20){
        const valueArr = this.data.map(i => i.value).sort((a, b) => a - b);
        const dataChunk = _.chunk(valueArr, 10);
        const bin1 = d3.bin().value(d => d.value);
        const buckets1 = bin1(this.data);
        console.log(buckets1);
        console.log(buckets1.values);

        const thresholdFreedmanDiaconis = d3.bin().thresholds(d3.thresholdFreedmanDiaconis);
        const thresholdScott = d3.bin().thresholds(d3.thresholdScott);
        const thresholdSturges = d3.bin().thresholds(d3.thresholdSturges);
        console.log('thresholdFreedmanDiaconis', thresholdFreedmanDiaconis(valueArr));
        console.log('thresholdScott', thresholdScott(valueArr));
        console.log('thresholdSturges', thresholdSturges(valueArr));
      }
    }

    d3Iterable(): void{
      if (this.data.length > 20){
        console.log(d3.every(this.data, d => {
          return d.value > 1000;
        }));
      }
    }

    // tslint:disable: no-unnecessary-initializer
    BubbleChart(data, {
      name = ([x]) => x, // alias for label
      label = name, // given d in data, returns text to display on the bubble
      value = ([, y]) => y, // given d in data, returns a quantitative size
      group = undefined, // given d in data, returns a categorical value for color
      title = undefined, // given d in data, returns text to show on hover
      link = undefined, // given a node d, its link (if any)
      linkTarget = '_blank', // the target attribute for links, if any
      width = 640, // outer width, in pixels
      height = width, // outer height, in pixels
      padding = 3, // padding between circles
      margin = 1, // default margins
      marginTop = margin, // top margin, in pixels
      marginRight = margin, // right margin, in pixels
      marginBottom = margin, // bottom margin, in pixels
      marginLeft = margin, // left margin, in pixels
      groups = undefined, // array of group names (the domain of the color scale)
      colors = d3.schemeTableau10, // an array of colors (for groups)
      fill = '#ccc', // a static fill color, if no group channel is specified
      fillOpacity = 0.7, // the fill opacity of the bubbles
      stroke = undefined, // a static stroke around the bubbles
      strokeWidth = undefined, // the stroke width around the bubbles, if any
      strokeOpacity = undefined, // the stroke opacity around the bubbles, if any
      } = {}) {
        if (data.length === 0){
            return false;
        }
        // Compute the values.
        const D = d3.map(data, d => d);
        const V = d3.map(data, value);
        const G = group == null ? null : d3.map(data, group);
        const I = d3.range(V.length).filter(i => V[i] > 0).reverse();

        // Unique the groups.
        if (G && groups === undefined) { groups = I.map(i => G[i]); }
        groups = G && new d3.InternSet(groups);


        const color = d3.scaleOrdinal(groups, colors);

        // Compute labels and titles.
        const L = label == null ? null : d3.map(data, label);
        const T = title === undefined ? L : title == null ? null : d3.map(data, title);


        // Compute layout: create a 1-deep hierarchy, and pack it.
        const root = d3.pack()
          .size([width - marginLeft - marginRight, height - marginTop - marginBottom])
          .padding(padding)
        (d3.hierarchy({children: I})
          .sum((i: any) => V[i]));


        // A unique identifier for clip paths (to avoid conflicts).
        const uid = `O-${Math.random().toString(16).slice(2)}`;

        const eleSelector = `figure#${this.dataId}`;

        this.svg = d3
          .select(eleSelector)
          .html('');

        this.svg = d3
          .select(eleSelector)
          .append('svg');

        this.svg.attr('width', width)
            .attr('height', height)
            .attr('viewBox', `${-marginLeft}, ${-marginTop}, ${width}, ${height}`)
            .attr('style', 'max-width: 100%; height: auto; height: intrinsic;')
            .attr('fill', 'currentColor')
            .attr('font-size', 10)
            .attr('font-family', 'sans-serif')
            .attr('text-anchor', 'middle');

        const leaf = this.svg.selectAll('a')
            .data(root.leaves())
            .join('a')
              .attr('xlink:href', link == null ? null : (d, i) => link(D[d.data], i, data))
              .attr('target', link == null ? null : linkTarget)
              .attr('transform', d => `translate(${d.x},${d.y})`);

        leaf.append('circle')
              .attr('stroke', stroke)
              .attr('stroke-width', strokeWidth)
              .attr('stroke-opacity', strokeOpacity)
              .attr('fill', G ? d => color(G[d.data]) : fill == null ? 'none' : fill)
              .attr('fill-opacity', fillOpacity)
              .attr('r', d => {
                return d.r;
              });


        if (T) { leaf.append('title').text(d => T[d.data]); }

        if (L) {
          // A unique identifier for clip paths (to avoid conflicts).
          const uid = `O-${Math.random().toString(16).slice(2)}`;

          leaf.append('clipPath')
              .attr('id', d => `${uid}-clip-${d.data}`)
            .append('circle')
              .attr('r', d => d.r);

          leaf.append('text')
              .attr('clip-path', d => `url()`)
            .selectAll('tspan')
            .data(d => `${L[d.data]}\n${V[d.data]}`.split(/\n/g))
            .join('tspan')
              .attr('font-size', this.textSize)
              .attr('x', 0)
              .attr('y', (d, i, D) => `${i - D.length / 2 + 0.85}em`)
              .attr('fill-opacity', (d, i, D) => i === D.length - 1 ? 0.7 : null)
              .text(d => d);
    }
        return Object.assign(this.svg.node(), {scales: {color}});
      }

}
