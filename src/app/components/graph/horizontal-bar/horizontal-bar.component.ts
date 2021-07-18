import { Component, Input, OnInit } from '@angular/core';
import { Datum } from 'src/app/interface/Datum';
import * as d3 from 'd3';

@Component({
    selector: 'app-horizontal-bar',
    templateUrl: './horizontal-bar.component.html',
    styleUrls: ['./horizontal-bar.component.scss']
})
export default class HorizontalBarComponent implements OnInit {

    @Input() data: Datum[] = [];
    private svg: any;

    ngOnInit(): void {
        console.log('app-horizontal-bar');
    }


    private drawPie(): void {

        const width = 500;
        const height = 500;

        const svg = d3.create('svg')
            .attr('viewBox', [0, 0, width, height].join(' '));

        svg.append('g')
            .attr('fill', 'steelblue')
            .selectAll('rect')
            .data(this.data)
            .join('rect')
            .attr('x', x(0))
            .attr('y', (d, i) => y(i))
            .attr('width', d => x(d.value) - x(0))
            .attr('height', y.bandwidth());

        svg.append('g')
            .attr('fill', 'white')
            .attr('text-anchor', 'end')
            .attr('font-family', 'sans-serif')
            .attr('font-size', 12)
            .selectAll('text')
            .data(this.data)
            .join('text')
            .attr('x', d => x(d.value))
            .attr('y', (d, i) => y(i) + y.bandwidth() / 2)
            .attr('dy', '0.35em')
            .attr('dx', -4)
            .text(d => format(d.value))
            .call(text => text.filter(d => x(d.value) - x(0) < 20) // short bars
            .attr('dx', +4)
            .attr('fill', 'black')
            .attr('text-anchor', 'start'));

        svg.append('g')
            .call(xAxis);

        svg.append('g')
            .call(yAxis);

    }
}