1-6 Array Histograms 数组生成直方图相关数据操作方法
### [Histograms](https://github.com/d3/d3-array/blob/v3.1.1/README.md#bins)

Bin discrete samples into continuous, non-overlapping intervals.
将离散样本分成连续的不间断的间隔

-   [d3.bin](https://github.com/d3/d3-array/blob/v3.1.1/README.md#bin) - create a new bin generator.bin生成器
-   [*bin*](https://github.com/d3/d3-array/blob/v3.1.1/README.md#_bin) - bins a given array of samples.使用数组生成样本
-   [*bin*.value](https://github.com/d3/d3-array/blob/v3.1.1/README.md#bin_value) - specify a value accessor for each sample.指定分组用的值
-   [*bin*.domain](https://github.com/d3/d3-array/blob/v3.1.1/README.md#bin_domain) - specify the interval of observable values.指定分组区域
-   [*bin*.thresholds](https://github.com/d3/d3-array/blob/v3.1.1/README.md#bin_thresholds) - specify how values are divided into bins.指定分隔间
-   [d3.thresholdFreedmanDiaconis](https://github.com/d3/d3-array/blob/v3.1.1/README.md#thresholdFreedmanDiaconis) - the Freedman–Diaconis binning rule.弗里德曼分组法
-   [d3.thresholdScott](https://github.com/d3/d3-array/blob/v3.1.1/README.md#thresholdScott) - Scott’s normal reference binning rule.斯科特分组法
-   [d3.thresholdSturges](https://github.com/d3/d3-array/blob/v3.1.1/README.md#thresholdSturges) - Sturges’ binning formula.斯特奇斯分组法