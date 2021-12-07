23-5.ordinal scales 顺序尺

### [](https://github.com/d3/d3/blob/main/API.md#ordinal-scales)[Ordinal Scales](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal-scales)

Map a discrete domain to a discrete range.将离散域映射到离散范围。

-   [d3.scaleOrdinal](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleOrdinal) - create an ordinal scale.创建顺序刻度。
-   [*ordinal*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_ordinal) - compute the range value corresponding to a given domain value.计算与给定域值对应的范围值。
-   [*ordinal*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_domain) - set the input domain.设置输入域。
-   [*ordinal*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_range) - set the output range.设置输出范围。
-   [*ordinal*.unknown](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_unknown) - set the output value for unknown inputs.设置未知输入的输出值。
-   [*ordinal*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_copy) - create a copy of this scale.创建此比例的副本。
-   [d3.scaleImplicit](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleImplicit) - a special unknown value for implicit domains.隐式域的特殊未知值
-   [d3.scaleBand](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleBand) - create an ordinal band scale.创建一个有序的乐队规模。
-   [*band*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_band) - compute the band start corresponding to a given domain value.计算与给定域值对应的频带起始值。
-   [*band*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_domain) - set the input domain.设置输入域。
-   [*band*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_range) - set the output range.设置输出范围。
-   [*band*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*band*.round](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_round) - enable rounding.启用舍入。
-   [*band*.paddingInner](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_paddingInner) - set padding between bands.在带之间设置填充。
-   [*band*.paddingOuter](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_paddingOuter) - set padding outside the first and last bands.在第一个和最后一个标注栏之外设置填充。
-   [*band*.padding](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_padding) - set padding outside and between bands.设置带外和带间的填充。
-   [*band*.align](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_align) - set band alignment, if there is extra space.如果有额外空间，则设置标注栏对齐。
-   [*band*.bandwidth](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_bandwidth) - get the width of each band.获取每个频带的宽度。
-   [*band*.step](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_step) - get the distance between the starts of adjacent bands.获取相邻条带起点之间的距离。
-   [*band*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_copy) - create a copy of this scale.创建此比例的副本。
-   [d3.scalePoint](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scalePoint) - create an ordinal point scale.创建序号点比例。
-   [*point*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_point) - compute the point corresponding to a given domain value.计算与给定域值对应的点。
-   [*point*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_domain) - set the input domain.设置输入域。
-   [*point*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_range) - set the output range.设置输出范围。
-   [*point*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_rangeRound) - set the output range and enable rounding.设置输出范围并启用舍入。
-   [*point*.round](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_round) - enable rounding.启用舍入
-   [*point*.padding](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_padding) - set padding outside the first and last point.在第一个和最后一个点之外设置填充。
-   [*point*.align](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_align) - set point alignment, if there is extra space.在第一个和最后一个点之外设置填充
-   [*point*.bandwidth](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_bandwidth) - returns zero.返回零。
-   [*point*.step](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_step) - get the distance between the starts of adjacent points.获取相邻点起点之间的距离。
-   [*point*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_copy) - create a copy of this scale.创建此比例的副本。