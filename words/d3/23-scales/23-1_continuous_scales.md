23-1.continuous scales 连续尺

### [](https://github.com/d3/d3/blob/main/API.md#continuous-scales)[Continuous Scales](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous-scales)

Map a continuous, quantitative domain to a continuous range.
将一个连续的、 量化的 域映射到一个连续的范围。

-   [*continuous*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_continuous) - compute the range value corresponding to a given domain value.计算给定域值对应的范围值
-   [*continuous*.invert](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_invert) - compute the domain value corresponding to a given range value.计算给定范围值对应的域值。
-   [*continuous*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_domain) - set the input domain.设置输入域
-   [*continuous*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_range) - set the output range.设置输出范围
-   [*continuous*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*continuous*.clamp](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_clamp) - enable clamping to the domain or range.使夹持到域或范围内。
-   [*continuous*.unknown](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_unknown) - set the output value for unknown inputs.对未知输入设定输出值。
-   [*continuous*.interpolate](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_interpolate) - set the output interpolator.设置输出插值器。
-   [*continuous*.ticks](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_ticks) - compute representative values from the domain.从域中计算代表值。
-   [*continuous*.tickFormat](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_tickFormat) - format ticks for human consumption.用于人类消费的格式标签。
-   [*continuous*.nice](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_nice) - extend the domain to nice round numbers.将域扩展为良好的圆数。
-   [*continuous*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#continuous_copy) - create a copy of this scale.创建此量表的副本。
-   [d3.tickFormat](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#tickFormat) - format ticks for human consumption.用于人类消费的格式标签。
-   [d3.scaleLinear](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleLinear) - create a quantitative linear scale.创建一个量化的线性尺度。
-   [d3.scalePow](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scalePow) - create a quantitative power scale.创建一个量化的幂刻度尺
-   [*pow*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_pow) - compute the range value corresponding to a given domain value.计算与给定域值对应的范围值。
-   [*pow*.invert](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_invert) - compute the domain value corresponding to a given range value.计算与给定范围值对应的域值。
-   [*pow*.exponent](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_exponent) - set the power exponent.设置幂指数。
-   [*pow*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_domain) - set the input domain.设置输入域。
-   [*pow*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_range) - set the output range.设置输出范围。
-   [*pow*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*pow*.clamp](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_clamp) - enable clamping to the domain or range.启用对域或范围的钳制
-   [*pow*.interpolate](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_interpolate) - set the output interpolator.设置输出插值器。
-   [*pow*.ticks](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_ticks) - compute representative values from the domain.计算域中的代表性值。
-   [*pow*.tickFormat](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_tickFormat) - format ticks for human consumption.为人类消费设置刻度的格式。
-   [*pow*.nice](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_nice) - extend the domain to nice round numbers.将域扩展到漂亮的整数。
-   [*pow*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#pow_copy) - create a copy of this scale.创建此比例的副本
-   [d3.scaleSqrt](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSqrt) - create a quantitative power scale with exponent 0.5.创建指数为0.5的定量幂标度。
-   [d3.scaleLog](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleLog) - create a quantitative logarithmic scale.创建一个定量对数刻度。
-   [*log*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_log) - compute the range value corresponding to a given domain value.计算与给定域值对应的范围值。
-   [*log*.invert](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_invert) - compute the domain value corresponding to a given range value.计算与给定范围值对应的域值。
-   [*log*.base](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_base) - set the logarithm base.设置对数基数
-   [*log*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_domain) - set the input domain.设置输入域
-   [*log*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_range) - set the output range.设置输出范围
-   [*log*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*log*.clamp](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_clamp) - enable clamping to the domain or range.启用对域或范围的钳制。
-   [*log*.interpolate](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_interpolate) - set the output interpolator.设置输出插值器。
-   [*log*.ticks](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_ticks) - compute representative values from the domain.计算域中的代表性值。
-   [*log*.tickFormat](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_tickFormat) - format ticks for human consumption.为人类消费设置刻度的格式
-   [*log*.nice](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_nice) - extend the domain to nice round numbers.将域扩展到漂亮的整数。
-   [*log*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#log_copy) - create a copy of this scale.创建此比例的副本。
-   [d3.scaleSymlog](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleSymlog) - create a symmetric logarithmic scale.创建对称对数刻度
-   [*symlog*.constant](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#symlog_constant) - set the constant of a symlog scale.设置符号刻度的常数。
-   [d3.scaleIdentity](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleIdentity) - creates an identity scale.创建标识比例。
-   [d3.scaleRadial](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleRadial) - creates a radial scale.创建一个径向尺度。
-   [d3.scaleTime](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleTime) - create a linear scale for time.为时间创建一个线性尺度
-   [*time*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_time) - compute the range value corresponding to a given domain value.计算给定域值对应的范围值
-   [*time*.invert](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_invert) - compute the domain value corresponding to a given range value.计算给定范围值对应的域值
-   [*time*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_domain) - set the input domain.设置输入域。
-   [*time*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_range) - set the output range.设置输出范围。
-   [*time*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*time*.clamp](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_clamp) - enable clamping to the domain or range.启用对域或范围的钳制。
-   [*time*.interpolate](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_interpolate) - set the output interpolator.设置输出插值器。
-   [*time*.ticks](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_ticks) - compute representative values from the domain.计算域中的代表性值。
-   [*time*.tickFormat](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_tickFormat) - format ticks for human consumption.为人类消费设置刻度的格式。
-   [*time*.nice](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_nice) - extend the domain to nice round times.将域扩展到良好的循环时间。
-   [*time*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#time_copy) - create a copy of this scale.创建此比例的副本。
-   [d3.scaleUtc](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleUtc) - create a linear scale for UTC.为UTC创建线性比例