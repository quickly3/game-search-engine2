23-4.Quantize Scales 量尺

### [](https://github.com/d3/d3/blob/main/API.md#quantize-scales)[Quantize Scales](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize-scales)

Map a continuous, quantitative domain to a discrete range.

-   [d3.scaleQuantize](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleQuantize) - create a uniform quantizing linear scale.
-   [*quantize*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_quantize) - compute the range value corresponding to a given domain value.
-   [*quantize*.invertExtent](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_invertExtent) - compute the domain values corresponding to a given range value.
-   [*quantize*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_domain) - set the input domain.
-   [*quantize*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_range) - set the output range.
-   [*quantize*.ticks](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_ticks) - compute representative values from the domain.
-   [*quantize*.tickFormat](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_tickFormat) - format ticks for human consumption.
-   [*quantize*.nice](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_nice) - extend the domain to nice round numbers.
-   [*quantize*.thresholds](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_thresholds) - return the array of computed thresholds within the domain.
-   [*quantize*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantize_copy) - create a copy of this scale.
-   [d3.scaleQuantile](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleQuantile) - create a quantile quantizing linear scale.
-   [*quantile*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_quantile) - compute the range value corresponding to a given domain value.
-   [*quantile*.invertExtent](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantile_invertExtent) - compute the domain values corresponding to a given range value.
-   [*quantile*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantile_domain) - set the input domain.
-   [*quantile*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantile_range) - set the output range.
-   [*quantile*.quantiles](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantile_quantiles) - get the quantile thresholds.
-   [*quantile*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#quantile_copy) - create a copy of this scale.
-   [d3.scaleThreshold](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#scaleThreshold) - create an arbitrary quantizing linear scale.
-   [*threshold*](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#_threshold) - compute the range value corresponding to a given domain value.
-   [*threshold*.invertExtent](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#threshold_invertExtent) - compute the domain values corresponding to a given range value.
-   [*threshold*.domain](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#threshold_domain) - set the input domain.
-   [*threshold*.range](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#threshold_range) - set the output range.
-   [*threshold*.copy](https://github.com/d3/d3-scale/blob/v4.0.2/README.md#threshold_copy) - create a copy of this scale.