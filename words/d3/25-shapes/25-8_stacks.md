25-8.stacks 栈

### [](https://github.com/d3/d3/blob/main/API.md#stacks)[Stacks](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stacks)

Stack shapes, placing one adjacent to another, as in a stacked bar chart.堆叠形状，将一个形状相邻放置，如在堆叠条形图中。

-   [d3.stack](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack) - create a new stack generator.创建一个新的堆栈生成器。
-   [*stack*](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#_stack) - generate a stack for the given dataset.为给定的数据集生成堆栈。
-   [*stack*.keys](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_keys) - set the keys accessor.设置密钥访问器。
-   [*stack*.value](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_value) - set the value accessor.设置值访问器。
-   [*stack*.order](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_order) - set the order accessor.设置顺序访问器。
-   [*stack*.offset](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stack_offset) - set the offset accessor.设置偏移访问器。
-   [d3.stackOrderAppearance](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderAppearance) - put the earliest series on bottom.将最早的序列放在底部。
-   [d3.stackOrderAscending](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderAscending) - put the smallest series on bottom.将最小的序列放在底部。
-   [d3.stackOrderDescending](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderDescending) - put the largest series on bottom.将最大的序列放在底部。
-   [d3.stackOrderInsideOut](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderInsideOut) - put earlier series in the middle.将更早的序列放在底部。
-   [d3.stackOrderNone](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderNone) - use the given series order.使用给定的序列顺序
-   [d3.stackOrderReverse](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOrderReverse) - use the reverse of the given series order.使用与给定序列顺序相反的顺序
-   [d3.stackOffsetExpand](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetExpand) - normalize the baseline to zero and topline to one.将基线规格化为零，将背线规格化为一
-   [d3.stackOffsetDiverging](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetDiverging) - positive above zero; negative below zero.零以上为正；零下为负数。
-   [d3.stackOffsetNone](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetNone) - apply a zero baseline.应用零基线
-   [d3.stackOffsetSilhouette](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetSilhouette) - center the streamgraph around zero.将流图中心在零附近
-   [d3.stackOffsetWiggle](https://github.com/d3/d3-shape/blob/v3.0.1/README.md#stackOffsetWiggle) - minimize streamgraph wiggling.最小化流图抖动。