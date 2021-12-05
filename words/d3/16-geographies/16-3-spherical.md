16-3.spherical 球形相关

### [](https://github.com/d3/d3/blob/main/API.md#spherical-math)[Spherical Math](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#spherical-math)

-   [d3.geoArea](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoArea) - compute the spherical area of a given feature.计算给定特征的球面体区域
-   [d3.geoBounds](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoBounds) - compute the latitude-longitude bounding box for a given feature.计算给定区域的经纬度边界框
-   [d3.geoCentroid](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoCentroid) - compute the spherical centroid of a given feature.计算给定特征的球面质心
-   [d3.geoDistance](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoDistance) - compute the great-arc distance between two points.计算两点之间的大圆弧距离
-   [d3.geoLength](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoLength) - compute the length of a line string or the perimeter of a polygon.计算一行字符串长度或者多边形的周长
-   [d3.geoInterpolate](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoInterpolate) - interpolate between two points along a great arc.沿大圆弧在两点之间进行插值
-   [d3.geoContains](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoContains) - test whether a point is inside a given feature.测试一个点是否在一个给定特征内部
-   [d3.geoRotation](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoRotation) - create a rotation function for the specified angles.为指定的角度创建一个旋转函数
-   [*rotation*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_rotation) - rotate the given point around the sphere. 围绕球体旋转给定点。
-   [*rotation*.invert](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#rotation_invert) - unrotate the given point around the sphere. 围绕球体反向旋转给定点。

### [](https://github.com/d3/d3/blob/main/API.md#spherical-shapes)[Spherical Shapes](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#spherical-shapes)

-   [d3.geoCircle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoCircle) - create a circle generator.创建一个环生成器
-   [*circle*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_circle) - generate a piecewise circle as a Polygon.生成一个分段圆
-   [*circle*.center](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#circle_center) - specify the circle center in latitude and longitude.用经纬度指定一个圆心
-   [*circle*.radius](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#circle_radius) - specify the angular radius in degrees.以度为单位指定角半径
-   [*circle*.precision](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#circle_precision) - specify the precision of the piecewise circle.指定分段圆的精度
-   [d3.geoGraticule](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGraticule) - create a graticule generator.创建一个经纬网生成器
-   [*graticule*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_graticule) - generate a MultiLineString of meridians and parallels.生成经络和纬线的多线字符串
-   [*graticule*.lines](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_lines) - generate an array of LineStrings of meridians and parallels.生成一个由经线和纬线组成的 LineStrings 数组
-   [*graticule*.outline](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_outline) - generate a Polygon of the graticule’s extent.生成经纬网范围的多边形。
-   [*graticule*.extent](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_extent) - get or set the major & minor extents.获取或设置主要和次要范围
-   [*graticule*.extentMajor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_extentMajor) - get or set the major extent.获取或设置主要范围
-   [*graticule*.extentMinor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_extentMinor) - get or set the minor extent.获取或设置次要范围
-   [*graticule*.step](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_step) - get or set the major & minor step intervals.获取或设置主要和次要步骤间隔
-   [*graticule*.stepMajor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_stepMajor) - get or set the major step intervals.获取或设置主要步骤间隔
-   [*graticule*.stepMinor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_stepMinor) - get or set the minor step intervals.获取或设置次要步骤间隔
-   [*graticule*.precision](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_precision) - get or set the latitudinal precision.获取或设置纬度精度
-   [d3.geoGraticule10](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGraticule10) - generate the default 10° global graticule.生成默认的 10° 全局经纬网