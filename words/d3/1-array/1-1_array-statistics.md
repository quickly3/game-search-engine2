1-1.Array Statistics 统计相关
### [Statistics 统计](https://github.com/d3/d3-array/blob/v3.1.1/README.md#statistics)

Methods for computing basic summary statistics.  计算汇总同统计的基本方法

-   [d3.min](https://github.com/d3/d3-array/blob/v3.1.1/README.md#min) - compute the minimum value in an iterable.求一个可迭代对象中的最小值
-   [d3.minIndex](https://github.com/d3/d3-array/blob/v3.1.1/README.md#minIndex) - compute the index of the minimum value in an iterable.求一个可迭代对象中的最小值的索引
-   [d3.max](https://github.com/d3/d3-array/blob/v3.1.1/README.md#max) - compute the maximum value in an iterable.求一个可迭代对象中的最大值
-   [d3.maxIndex](https://github.com/d3/d3-array/blob/v3.1.1/README.md#maxIndex) - compute the index of the maximum value in an iterable.求一个可迭代对象中的最大值的索引
-   [d3.extent](https://github.com/d3/d3-array/blob/v3.1.1/README.md#extent) - compute the minimum and maximum value in an iterable.求一个可迭代对象中的最小值和最大值
-   [d3.sum](https://github.com/d3/d3-array/blob/v3.1.1/README.md#sum) - compute the sum of an iterable of numbers.求和
-   [d3.mean](https://github.com/d3/d3-array/blob/v3.1.1/README.md#mean) - compute the arithmetic mean of an iterable of numbers.求平均值
-   [d3.median](https://github.com/d3/d3-array/blob/v3.1.1/README.md#median) - compute the median of an iterable of numbers (the 0.5-quantile).求中位数（0.5分位数）
-   [d3.mode](https://github.com/d3/d3-array/blob/v3.1.1/README.md#mode) - compute the mode (the most common value) of an iterable of numbers.求频率最高的值
-   [d3.cumsum](https://github.com/d3/d3-array/blob/v3.1.1/README.md#cumsum) - compute the cumulative sum of an iterable.求累积和
-   [d3.rank](https://github.com/d3/d3-array/blob/v3.1.1/README.md#rank) - compute the rank order of an iterable.计算各值排名
-   [d3.quantile](https://github.com/d3/d3-array/blob/v3.1.1/README.md#quantile) - compute a quantile for an iterable of numbers.计算分位数
-   [d3.quantileSorted](https://github.com/d3/d3-array/blob/v3.1.1/README.md#quantileSorted) - compute a quantile for a sorted array of numbers.计算排序过数组分位数
-   [d3.variance](https://github.com/d3/d3-array/blob/v3.1.1/README.md#variance) - compute the variance of an iterable of numbers.求方差
-   [d3.deviation](https://github.com/d3/d3-array/blob/v3.1.1/README.md#deviation) - compute the standard deviation of an iterable of numbers.求偏离（标准差）
-   [d3.fcumsum](https://github.com/d3/d3-array/blob/v3.1.1/README.md#fcumsum) - compute a full precision cumulative summation of numbers.求浮点数累积和
-   [d3.fsum](https://github.com/d3/d3-array/blob/v3.1.1/README.md#fsum) - compute a full precision summation of an iterable of numbers.浮点数求和
-   [new d3.Adder](https://github.com/d3/d3-array/blob/v3.1.1/README.md#adder) - creates a full precision adder.创建一个全精度添加器
-   [*adder*.add](https://github.com/d3/d3-array/blob/v3.1.1/README.md#adder_add) - add a value to an adder.
-   [*adder*.valueOf](https://github.com/d3/d3-array/blob/v3.1.1/README.md#adder_valueOf) - returns a double precision representation of an adder’s value.