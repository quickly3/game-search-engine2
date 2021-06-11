import { Component, OnInit } from '@angular/core';
import * as d3 from "d3";

@Component({
  selector: 'app-graph',
  templateUrl: './graph.component.html',
  styleUrls: ['./graph.component.scss']
})
export class GraphComponent implements OnInit {

  private svg:any;
  
  ngOnInit(): void {
    this.drawPie();
  }

  private drawPie(): void {

    const width = 500
    const height = 500

    const data = [{
        name:"a",
        value:100
      },{
        name:"b",
        value:100
      }]


    const color = d3.scaleOrdinal()
      .domain(data.map((d:any) => d.name))
      .range(d3.quantize((t:any) => d3.interpolateSpectral(t * 0.8 + 0.1), data.length).reverse())

    const arc = d3.arc()
        .innerRadius(0)
        .outerRadius(Math.min(width, height) / 2 - 1)

    const arcLabel = () => {
      const radius = Math.min(width, height) / 2 * 0.8;
      return d3.arc().innerRadius(radius).outerRadius(radius);
    }

    const pie = d3.pie()
      .sort(null)
      .value((d:any) => d.value)

    const arcs = pie(data);

    this.svg = d3.select("figure#bar")
      .append("svg")
      .attr("viewBox", [-width / 2, -height / 2, width, height]);

    this.svg.append("g")
        .attr("stroke", "white")
      .selectAll("path")
      .data(arcs)
      .join("path")
        .attr("fill", (d:any) => color(d.data.name))
        .attr("d", arc)
      .append("title")
        .text((d:any) => `${d.data.name}: ${d.data.value.toLocaleString()}`);

    this.svg.append("g")
        .attr("font-family", "sans-serif")
        .attr("font-size", 12)
        .attr("text-anchor", "middle")
      .selectAll("text")
      .data(arcs)
      .join("text")
        .attr("transform", (d:any) => `translate(${arcLabel.centroid(d)})`)
        .call((text:any) => text.append("tspan")
            .attr("y", "-0.4em")
            .attr("font-weight", "bold")
            .text((d:any) => d.data.name))
        .call((text:any) => text.filter((d:any) => (d.endAngle - d.startAngle) > 0.25).append("tspan")
            .attr("x", 0)
            .attr("y", "0.7em")
            .attr("fill-opacity", 0.7)
            .text((d:any) => d.data.value.toLocaleString()));

  }



}
