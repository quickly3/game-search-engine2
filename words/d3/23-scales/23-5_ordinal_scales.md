23-5.ordinal scales 顺序尺

### [](https://github.com/d3/d3/blob/main/API.md#ordinal-scales)[Ordinal Scales](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal-scales)

Map a discrete domain to a discrete range.

-   [d3.scaleOrdinal](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleOrdinal) - create an ordinal scale.
-   [*ordinal*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_ordinal) - compute the range value corresponding to a given domain value.
-   [*ordinal*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_domain) - set the input domain.
-   [*ordinal*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_range) - set the output range.
-   [*ordinal*.unknown](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_unknown) - set the output value for unknown inputs.
-   [*ordinal*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#ordinal_copy) - create a copy of this scale.
-   [d3.scaleImplicit](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleImplicit) - a special unknown value for implicit domains.
-   [d3.scaleBand](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleBand) - create an ordinal band scale.
-   [*band*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_band) - compute the band start corresponding to a given domain value.
-   [*band*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_domain) - set the input domain.
-   [*band*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_range) - set the output range.
-   [*band*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_rangeRound) - set the output range and enable rounding.
-   [*band*.round](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_round) - enable rounding.
-   [*band*.paddingInner](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_paddingInner) - set padding between bands.
-   [*band*.paddingOuter](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_paddingOuter) - set padding outside the first and last bands.
-   [*band*.padding](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_padding) - set padding outside and between bands.
-   [*band*.align](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_align) - set band alignment, if there is extra space.
-   [*band*.bandwidth](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_bandwidth) - get the width of each band.
-   [*band*.step](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_step) - get the distance between the starts of adjacent bands.
-   [*band*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#band_copy) - create a copy of this scale.
-   [d3.scalePoint](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scalePoint) - create an ordinal point scale.
-   [*point*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_point) - compute the point corresponding to a given domain value.
-   [*point*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_domain) - set the input domain.
-   [*point*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_range) - set the output range.
-   [*point*.rangeRound](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_rangeRound) - set the output range and enable rounding.
-   [*point*.round](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_round) - enable rounding.
-   [*point*.padding](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_padding) - set padding outside the first and last point.
-   [*point*.align](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_align) - set point alignment, if there is extra space.
-   [*point*.bandwidth](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_bandwidth) - returns zero.
-   [*point*.step](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_step) - get the distance between the starts of adjacent points.
-   [*point*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#point_copy) - create a copy of this scale.