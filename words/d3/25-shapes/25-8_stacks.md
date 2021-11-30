25-8.stacks 栈

### [](https://github.com/d3/d3/blob/main/API.md#stacks)[Stacks](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stacks)

Stack shapes, placing one adjacent to another, as in a stacked bar chart.

-   [d3.stack](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack) - create a new stack generator.
-   [*stack*](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#_stack) - generate a stack for the given dataset.
-   [*stack*.keys](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_keys) - set the keys accessor.
-   [*stack*.value](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_value) - set the value accessor.
-   [*stack*.order](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_order) - set the order accessor.
-   [*stack*.offset](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_offset) - set the offset accessor.
-   [d3.stackOrderAppearance](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderAppearance) - put the earliest series on bottom.
-   [d3.stackOrderAscending](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderAscending) - put the smallest series on bottom.
-   [d3.stackOrderDescending](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderDescending) - put the largest series on bottom.
-   [d3.stackOrderInsideOut](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderInsideOut) - put earlier series in the middle.
-   [d3.stackOrderNone](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderNone) - use the given series order.
-   [d3.stackOrderReverse](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderReverse) - use the reverse of the given series order.
-   [d3.stackOffsetExpand](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetExpand) - normalize the baseline to zero and topline to one.
-   [d3.stackOffsetDiverging](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetDiverging) - positive above zero; negative below zero.
-   [d3.stackOffsetNone](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetNone) - apply a zero baseline.
-   [d3.stackOffsetSilhouette](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetSilhouette) - center the streamgraph around zero.
-   [d3.stackOffsetWiggle](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetWiggle) - minimize streamgraph wiggling.