18.interpolators 插入器

## [](https://github.com/d3/d3/blob/main/API.md#interpolators-d3-interpolate)[Interpolators (d3-interpolate)](https://github.com/d3/d3-interpolate/tree/v3.0.1)

Interpolate numbers, colors, strings, arrays, objects, whatever!
给数字,颜色,字符串,数组，对象等等插入中间值

-   [d3.interpolate](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolate) - interpolate arbitrary values.给任意值插入中间值
-   [d3.interpolateNumber](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateNumber) - interpolate numbers.给数字插入中间值
-   [d3.interpolateRound](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateRound) - interpolate integers.给整数插入中间值
-   [d3.interpolateString](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateString) - interpolate strings with embedded numbers.使用插入数字位字符串设置中间值
-   [d3.interpolateDate](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateDate) - interpolate dates.日期插入值
-   [d3.interpolateArray](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateArray) - interpolate arrays of arbitrary values.给任意对象数组设置插入值
-   [d3.interpolateNumberArray](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateNumberArray) - interpolate arrays of numbers.在数字数组之间插值
-   [d3.interpolateObject](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateObject) - interpolate arbitrary objects. 在任意对象之间插值
-   [d3.interpolateTransformCss](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateTransformCss) - interpolate 2D CSS transforms.在2D CSS变换之间插值
-   [d3.interpolateTransformSvg](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateTransformSvg) - interpolate 2D SVG transforms.在2D SVG变换之间插值
-   [d3.interpolateZoom](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateZoom) - zoom and pan between two views.在两个视图之间缩放和平移
-   [*interpolateZoom*.rho](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolate_rho) - set the curvature *rho* of the zoom interpolator.设置缩放插值器的曲率 *rho*。
-   [d3.interpolateDiscrete](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateDiscrete) - generate a discrete interpolator from a set of values.从一组值生成离散插值器。
-   [d3.quantize](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#quantize) - generate uniformly-spaced samples from an interpolator.从内插器生成均匀间隔的样本
-   [d3.interpolateRgb](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateRgb) - interpolate RGB colors.插入RGB颜色
-   [d3.interpolateRgbBasis](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateRgbBasis) - generate a B-spline through a set of colors.通过一组颜色生成B样条
-   [d3.interpolateRgbBasisClosed](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateRgbBasisClosed) - generate a closed B-spline through a set of colors.通过一组颜色生成一个封闭的 B 样条
-   [d3.interpolateHsl](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateHsl) - interpolate HSL colors.插入HSL颜色
-   [d3.interpolateHslLong](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateHslLong) - interpolate HSL colors, the long way.插入HSL颜色,使用长路径
-   [d3.interpolateLab](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateLab) - interpolate Lab colors.插入Lab颜色
-   [d3.interpolateHcl](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateHcl) - interpolate HCL colors.插入HCL颜色
-   [d3.interpolateHclLong](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateHclLong) - interpolate HCL colors, the long way.插入HCL颜色,使用长路径
-   [d3.interpolateCubehelix](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateCubehelix) - interpolate Cubehelix colors.立方螺旋颜色插值器
-   [d3.interpolateCubehelixLong](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateCubehelixLong) - interpolate Cubehelix colors, the long way.立方螺旋颜色插值,使用长路径
-   [*interpolate*.gamma](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolate_gamma) - apply gamma correction during interpolation.在插值时应用伽马校正
-   [d3.interpolateHue](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateHue) - interpolate a hue angle.插值一个色调角
-   [d3.interpolateBasis](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateBasis) - generate a B-spline through a set of values.通过一组值生成一个B样条
-   [d3.interpolateBasisClosed](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#interpolateBasisClosed) - generate a closed B-spline through a set of values.通过一组值生成闭B样条。
-   [d3.piecewise](https://github.com/d3/d3-interpolate/blob/v3.0.1/README.md#piecewise) - generate a piecewise linear interpolator from a set of values.从一组值生成一个分段线性插值器。
