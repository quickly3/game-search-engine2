import { Component, Input, OnInit } from '@angular/core';
import * as Plot from '@observablehq/plot';
import * as d3 from 'd3';

@Component({
    selector: 'app-density-calendar',
    templateUrl: './density-calendar.component.html',
    styleUrls: ['./density-calendar.component.scss']
})
export default class DensityCalendarComponent {

    @Input() data: any[] = [];
    @Input() plotText: any = {
      legendTitle: '每日文章数量',
      cellTextTpl: '{date} \n数量：{count}',
      bottomText: '周'
    };
    @Input() dataId = '';

    private svg: any;
    mainSelector;

    ngOnChanges(): void {
        this.mainSelector = `figure#${this.dataId}`;
        if (this.data && this.data.length > 0){
            this.data = this.data.map(d=>{
              return {
                ...d,
                count:d.count === 0?undefined:d.count
              }
            })
            this.data = this.data.map(d => {
                return {
                    ...d,
                    date: new Date(d.date)
                };
            });
            this.drawPlot();
        }
    }

    drawPlot(): void {
        if(!d3.select(this.mainSelector).node()){
          return null;
        }
        d3.select(this.mainSelector).html('');
        const svgNode = this.legend({
            color: d3.scaleSequentialLog(
              // d3.extent(this.data, d => d.count),
              [50, d3.max(this.data, d => d.count)],
              d3.interpolateYlGnBu
            ),
            tickFormat: '.0s',
            title: this.plotText.legendTitle
        });

        const weekMap =['日','一','二','三','四','五','六'];

        const plot = Plot.plot({
            facet: { data: this.data, y: d => d.date.getUTCFullYear() },
            fy: { tickPadding: 0, reverse: true },
            x: { label: this.plotText.bottomText, tickFormat: t => t + 1 },
            y: { tickFormat: t=>{
              // console.log(Plot.formatWeekday()(t))
              return weekMap[t];
            } },
            color: { scheme: 'ylgnbu', type: 'log' },
            marks: [
              Plot.cell(this.data, {
                x: d => d3.utcWeek.count(d3.utcYear(d.date), d.date),
                y: d => d3.utcDay.count(d3.utcWeek(d.date), d.date),
                title: d => {
                  const dateStr = d.date.toISOString().replace(/T.*/, '');
                  const cellText = this.plotText.cellTextTpl.replace('{date}', dateStr).replace('{count}', d.count);
                  return cellText;
                },
                fill: 'count'
              })
            ],
            width: 1000,
            marginTop: 0,
            marginRight: 50,
            marginBottom: 35,
            style: { background: '#fff' }
          });
        d3.select(this.mainSelector).node().append(plot);
    }

    legend({color, ...options}) {
        return this.Legend(color, options);
    }

    Legend(color, {
        title,
        tickSize = 6,
        width = 320,
        height = 44 + tickSize,
        marginTop = 18,
        marginRight = 0,
        marginBottom = 16 + tickSize,
        marginLeft = 0,
        ticks = width / 64,
        tickFormat,
        tickValues
      }: any = {
      }) {

        function ramp(color, n = 256) {
          const canvas = document.createElement('canvas');
          canvas.width = n;
          canvas.height = 1;
          const context = canvas.getContext('2d');
          for (let i = 0; i < n; ++i) {
            context.fillStyle = color(i / (n - 1));
            context.fillRect(i, 0, 1, 1);
          }
          return canvas;
        }

        this.svg = d3.select(this.mainSelector)
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .attr('viewBox', `0, 0, ${width}, ${height}`)
            .style('overflow', 'visible')
            .style('display', 'block');

        let tickAdjust = g => g.selectAll('.tick line').attr('y1', marginTop + marginBottom - height);
        let x;

        // Continuous
        if (color.interpolate) {
          const n = Math.min(color.domain().length, color.range().length);

          x = color.copy().rangeRound(d3.quantize(d3.interpolate(marginLeft, width - marginRight), n));

          this.svg.append('image')
              .attr('x', marginLeft)
              .attr('y', marginTop)
              .attr('width', width - marginLeft - marginRight)
              .attr('height', height - marginTop - marginBottom)
              .attr('preserveAspectRatio', 'none')
              .attr('xlink:href', ramp(color.copy().domain(d3.quantize(d3.interpolate(0, 1), n))).toDataURL());
        }

        // Sequential
        else if (color.interpolator) {
          x = Object.assign(color.copy()
              .interpolator(d3.interpolateRound(marginLeft, width - marginRight)),
              {range() { return [marginLeft, width - marginRight]; }});

          this.svg.append('image')
              .attr('x', marginLeft)
              .attr('y', marginTop)
              .attr('width', width - marginLeft - marginRight)
              .attr('height', height - marginTop - marginBottom)
              .attr('preserveAspectRatio', 'none')
              .attr('xlink:href', ramp(color.interpolator()).toDataURL());

          // scaleSequentialQuantile doesn’t implement ticks or tickFormat.

          if (!x.ticks) {
            if (tickValues === undefined) {
              const n = Math.round(ticks + 1);
              tickValues = d3.range(n).map(i => d3.quantile(color.domain(), i / (n - 1)));
            }
            if (typeof tickFormat !== 'function') {
              tickFormat = d3.format(tickFormat === undefined ? ',f' : tickFormat);
            }
          }
        }

        // Threshold
        else if (color.invertExtent) {
          const thresholds
              = color.thresholds ? color.thresholds() // scaleQuantize
              : color.quantiles ? color.quantiles() // scaleQuantile
              : color.domain(); // scaleThreshold

          const thresholdFormat
              = tickFormat === undefined ? d => d
              : typeof tickFormat === 'string' ? d3.format(tickFormat)
              : tickFormat;

          x = d3.scaleLinear()
              .domain([-1, color.range().length - 1])
              .rangeRound([marginLeft, width - marginRight]);

          this.svg.append('g')
            .selectAll('rect')
            .data(color.range())
            .join('rect')
              .attr('x', (d, i) => x(i - 1))
              .attr('y', marginTop)
              .attr('width', (d, i) => x(i) - x(i - 1))
              .attr('height', height - marginTop - marginBottom)
              .attr('fill', (d: any) => d);

          tickValues = d3.range(thresholds.length);
          tickFormat = i => thresholdFormat(thresholds[i], i);
        }

        // Ordinal
        else {
          x = d3.scaleBand()
              .domain(color.domain())
              .rangeRound([marginLeft, width - marginRight]);

          this.svg.append('g')
            .selectAll('rect')
            .data(color.domain())
            .join('rect')
              .attr('x', x)
              .attr('y', marginTop)
              .attr('width', Math.max(0, x.bandwidth() - 1))
              .attr('height', height - marginTop - marginBottom)
              .attr('fill', color);

          tickAdjust = () => {};
        }
        this.svg.append('g')
            .attr('transform', `translate(0,${height - marginBottom})`)
            .call(d3.axisBottom(x)
              .ticks(ticks, typeof tickFormat === 'string' ? tickFormat : undefined)
              .tickFormat(typeof tickFormat === 'function' ? tickFormat : undefined)
              .tickSize(tickSize)
              .tickValues(tickValues))
            .call(tickAdjust)
            .call(g => g.select('.domain').remove())
            .call(g => g.append('text')
              .attr('x', marginLeft)
              .attr('y', marginTop + marginBottom - height - 6)
              .attr('fill', 'currentColor')
              .attr('text-anchor', 'start')
              .attr('font-weight', 'bold')
              .attr('class', 'title')
              .text(title));

        return this.svg.node();
      }
}
