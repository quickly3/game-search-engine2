### [Interning](https://github.com/d3/d3-array/blob/v3.1.1/README.md#interning)

d3内部使用   
InternMap 和 InternSet 类分别扩展了原生 JavaScript Map 和 Set 类，通过在确定键相等时绕过 SameValueZero 算法来允许日期和其他非原始键。 d3.group、d3.rollup 和 d3.index 使用 InternMap 而不是原生 Map。为方便起见，导出这两个类。

-   [d3.InternMap](https://github.com/d3/d3-array/blob/v3.1.1/README.md#InternMap) - a key-interning Map.
-   [d3.InternSet](https://github.com/d3/d3-array/blob/v3.1.1/README.md#InternSet) - a value-interning Set.