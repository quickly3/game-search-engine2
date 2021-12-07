25-5.curves 曲线

### [](https://github.com/d3/d3/blob/main/API.md#curves)[Curves](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curves)

Interpolate between points to produce a continuous shape.
在点之间进行插值以产生连续的形状。

-   [d3.curveBasis](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBasis) - a cubic basis spline, repeating the end points.三次基样条，重复端点
-   [d3.curveBasisClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBasisClosed) - a closed cubic basis spline.封闭的三次基样条。
-   [d3.curveBasisOpen](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBasisOpen) - a cubic basis spline.三次基样条。
-   [d3.curveBundle](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBundle) - a straightened cubic basis spline.拉直的三次基样条。
-   [*bundle*.beta](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBundle_beta) - set the bundle tension *beta*.设置束张力 *beta*。
-   [d3.curveBumpX](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBumpX) - a cubic Bézier spline with horizontal tangents.具有水平切线的三次贝塞尔样条。
-   [d3.curveBumpY](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBumpY) - a cubic Bézier spline with vertical tangents.具有垂直切线的三次贝塞尔样条。
-   [d3.curveCardinal](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinal) - a cubic cardinal spline, with one-sided difference at each end.三次基数样条，每端都有一侧差异。
-   [d3.curveCardinalClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinalClosed) - a closed cubic cardinal spline.闭合三次基数样条。
-   [d3.curveCardinalOpen](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinalOpen) - a cubic cardinal spline.三次基数样条。
-   [*cardinal*.tension](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinal_tension) - set the cardinal spline tension.设置基数样条张力
-   [d3.curveCatmullRom](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRom) - a cubic Catmull–Rom spline, with one-sided difference at each end.三次 Catmull-Rom 样条，每一端都有一侧差异。
-   [d3.curveCatmullRomClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRomClosed) - a closed cubic Catmull–Rom spline.闭合三次 Catmull-Rom 样条。
-   [d3.curveCatmullRomOpen](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRomOpen) - a cubic Catmull–Rom spline.三次 Catmull-Rom 样条。
-   [*catmullRom*.alpha](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRom_alpha) - set the Catmull–Rom parameter *alpha*.设置 Catmull–Rom 参数 alpha值。
-   [d3.curveLinear](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveLinear) - a polyline.多段线
-   [d3.curveLinearClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveLinearClosed) - a closed polyline.闭合的多段线
-   [d3.curveMonotoneX](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveMonotoneX) - a cubic spline that, given monotonicity in *x*, preserves it in *y*.三次样条，给定 *x* 中的单调性，将其保留在 *y* 中。
-   [d3.curveMonotoneY](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveMonotoneY) - a cubic spline that, given monotonicity in *y*, preserves it in *x*.三次样条，给定 *y* 中的单调性，将其保留在 *x* 中。
-   [d3.curveNatural](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveNatural) - a natural cubic spline.自然三次样条。
-   [d3.curveStep](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveStep) - a piecewise constant function.
-   [d3.curveStepAfter](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveStepAfter) - a piecewise constant function.分段常数函数
-   [d3.curveStepBefore](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveStepBefore) - a piecewise constant function.分段常数函数
-   [*curve*.areaStart](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_areaStart) - start a new area segment.开始一个新的区域段
-   [*curve*.areaEnd](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_areaEnd) - end the current area segment.结束当前区域段。
-   [*curve*.lineStart](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_lineStart) - start a new line segment.开始一个新的线段
-   [*curve*.lineEnd](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_lineEnd) - end the current line segment.结束当前线段。
-   [*curve*.point](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_point) - add a point to the current line segment.向当前线段添加一个点