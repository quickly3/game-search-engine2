1-5 Array Transformations 数组转换（生成）相关工具方法
### [Transformations](https://github.com/d3/d3-array/blob/v3.1.1/README.md#transformations)

Methods for transforming arrays and for generating new arrays.
用于转换数组的方法

-   [d3.flatGroup](https://github.com/d3/d3-array/blob/v3.1.1/README.md#flatGroup) - group an iterable into a flat array.两重或多重group,和groups类似只是传参方式不同
-   [d3.flatRollup](https://github.com/d3/d3-array/blob/v3.1.1/README.md#flatRollup) - reduce an iterable into a flat array.两重或多重rollup,和rollups类似只是传参方式不同
-   [d3.group](https://github.com/d3/d3-array/blob/v3.1.1/README.md#group) - group an iterable into a nested Map.
    group by key将元素字段名作为index 聚合元素
-   [d3.groups](https://github.com/d3/d3-array/blob/v3.1.1/README.md#groups) - group an iterable into a nested array. 多重group方法
-   [d3.groupSort](https://github.com/d3/d3-array/blob/v3.1.1/README.md#groupSort) - sort keys according to grouped values. 根据聚合计算后值排序元素，并能放回去重后排序的元素指定字段数组
-   [d3.index](https://github.com/d3/d3-array/blob/v3.1.1/README.md#index) - index an iterable into a nested Map.将元素字段值作为index 聚合元素
-   [d3.indexes](https://github.com/d3/d3-array/blob/v3.1.1/README.md#indexes) - index an iterable into a nested array.多重index方法
-   [d3.rollup](https://github.com/d3/d3-array/blob/v3.1.1/README.md#rollup) - reduce an iterable into a nested Map.分组并根据组员值进行计算，并返回计算后的分组结果
-   [d3.rollups](https://github.com/d3/d3-array/blob/v3.1.1/README.md#rollups) - reduce an iterable into a nested array.多重rollu方法
-   [d3.count](https://github.com/d3/d3-array/blob/v3.1.1/README.md#count) - count valid number values in an iterable.根据元素字段字段值进行计数
-   [d3.cross](https://github.com/d3/d3-array/blob/v3.1.1/README.md#cross) - compute the Cartesian product of two iterables.求笛卡尔积
-   [d3.merge](https://github.com/d3/d3-array/blob/v3.1.1/README.md#merge) - merge multiple iterables into one array.合并
-   [d3.pairs](https://github.com/d3/d3-array/blob/v3.1.1/README.md#pairs) - create an array of adjacent pairs of elements.用数组元素两两重组一个数组
-   [d3.permute](https://github.com/d3/d3-array/blob/v3.1.1/README.md#permute) - reorder an iterable of elements according to an iterable of indexes.用指定排序数组对原数组进行重排
-   [d3.shuffle](https://github.com/d3/d3-array/blob/v3.1.1/README.md#shuffle) - randomize the order of an iterable.随机重排
-   [d3.shuffler](https://github.com/d3/d3-array/blob/v3.1.1/README.md#shuffler) - randomize the order of an iterable. 使用指定seed生成随机重排函数
-   [d3.ticks](https://github.com/d3/d3-array/blob/v3.1.1/README.md#ticks) - generate representative values from a numeric interval.生成刻度数组
-   [d3.tickIncrement](https://github.com/d3/d3-array/blob/v3.1.1/README.md#tickIncrement) - generate representative values from a numeric interval.获得生成刻度 步增值
-   [d3.tickStep](https://github.com/d3/d3-array/blob/v3.1.1/README.md#tickStep) - generate representative values from a numeric interval.获得生成刻度 总步数（刻度）
-   [d3.nice](https://github.com/d3/d3-array/blob/v3.1.1/README.md#nice) - extend an interval to align with ticks. 获得一个修正过的生成总步数（保证与刻度对其）
-   [d3.range](https://github.com/d3/d3-array/blob/v3.1.1/README.md#range) - generate a range of numeric values. like python range获得范围值数组 默认increment为1的ticks方法
-   [d3.transpose](https://github.com/d3/d3-array/blob/v3.1.1/README.md#transpose) - transpose an array of arrays. zip压缩的另外一种形式（参数传递方式不同）
-   [d3.zip](https://github.com/d3/d3-array/blob/v3.1.1/README.md#zip) - transpose a variable number of arrays.将两个数组压缩成一个