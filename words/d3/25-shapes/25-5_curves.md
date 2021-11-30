25-5.curves 曲线

### [](https://github.com/d3/d3/blob/main/API.md#curves)[Curves](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curves)

Interpolate between points to produce a continuous shape.

-   [d3.curveBasis](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBasis) - a cubic basis spline, repeating the end points.
-   [d3.curveBasisClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBasisClosed) - a closed cubic basis spline.
-   [d3.curveBasisOpen](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBasisOpen) - a cubic basis spline.
-   [d3.curveBundle](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBundle) - a straightened cubic basis spline.
-   [*bundle*.beta](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBundle_beta) - set the bundle tension *beta*.
-   [d3.curveBumpX](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBumpX) - a cubic Bézier spline with horizontal tangents.
-   [d3.curveBumpY](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveBumpY) - a cubic Bézier spline with vertical tangents.
-   [d3.curveCardinal](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinal) - a cubic cardinal spline, with one-sided difference at each end.
-   [d3.curveCardinalClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinalClosed) - a closed cubic cardinal spline.
-   [d3.curveCardinalOpen](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinalOpen) - a cubic cardinal spline.
-   [*cardinal*.tension](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCardinal_tension) - set the cardinal spline tension.
-   [d3.curveCatmullRom](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRom) - a cubic Catmull–Rom spline, with one-sided difference at each end.
-   [d3.curveCatmullRomClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRomClosed) - a closed cubic Catmull–Rom spline.
-   [d3.curveCatmullRomOpen](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRomOpen) - a cubic Catmull–Rom spline.
-   [*catmullRom*.alpha](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveCatmullRom_alpha) - set the Catmull–Rom parameter *alpha*.
-   [d3.curveLinear](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveLinear) - a polyline.
-   [d3.curveLinearClosed](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveLinearClosed) - a closed polyline.
-   [d3.curveMonotoneX](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveMonotoneX) - a cubic spline that, given monotonicity in *x*, preserves it in *y*.
-   [d3.curveMonotoneY](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveMonotoneY) - a cubic spline that, given monotonicity in *y*, preserves it in *x*.
-   [d3.curveNatural](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveNatural) - a natural cubic spline.
-   [d3.curveStep](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveStep) - a piecewise constant function.
-   [d3.curveStepAfter](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveStepAfter) - a piecewise constant function.
-   [d3.curveStepBefore](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curveStepBefore) - a piecewise constant function.
-   [*curve*.areaStart](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_areaStart) - start a new area segment.
-   [*curve*.areaEnd](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_areaEnd) - end the current area segment.
-   [*curve*.lineStart](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_lineStart) - start a new line segment.
-   [*curve*.lineEnd](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_lineEnd) - end the current line segment.
-   [*curve*.point](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#curve_point) - add a point to the current line segment.