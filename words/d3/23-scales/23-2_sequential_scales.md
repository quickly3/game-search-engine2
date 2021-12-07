23-2.Sequential Scales 顺序尺

### [](https://github.com/d3/d3/blob/main/API.md#sequential-scales)[Sequential Scales](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential-scales)

Map a continuous, quantitative domain to a continuous, fixed interpolator.将一个连续的、定量的域映射为一个连续的、修正过的插值器。

-   [d3.scaleSequential](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSequential) - create a sequential scale.创建一个连续的尺度。
-   [*sequential*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_sequential) - compute the range value corresponding to an input value.计算与输入值对应的范围值。
-   [*sequential*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential_domain) - set the input domain.设置输入域。
-   [*sequential*.clamp](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential_clamp) - enable clamping to the domain.启用对域的钳制。
-   [*sequential*.interpolator](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential_interpolator) - set the scale’s output interpolator.设置比例的输出插值器。
-   [*sequential*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential_range) - set the output range.设置输出范围。
-   [*sequential*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*sequential*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequential_copy) - create a copy of this scale.创建此比例的副本。
-   [d3.scaleSequentialLog](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSequentialLog) - create a logarithmic sequential scale.创建对数顺序刻度。
-   [d3.scaleSequentialPow](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSequentialPow) - create a power sequential scale.创建电源顺序比例。
-   [d3.scaleSequentialSqrt](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSequentialSqrt) - create a power sequential scale with exponent 0.5.创建指数为0.5的幂序列比例。
-   [d3.scaleSequentialSymlog](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSequentialSymlog) - create a symmetric logarithmic sequential scale.创建对称对数顺序刻度。
-   [d3.scaleSequentialQuantile](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSequentialQuantile) - create a sequential scale using a *p*-quantile transform.使用*p*-分位数变换创建顺序比例。
-   [*sequentialQuantile*.quantiles](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#sequentialQuantile_quantiles) - return the scale’s quantiles.返回刻度的分位数。