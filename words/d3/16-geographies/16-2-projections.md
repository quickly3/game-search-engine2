16-2.Projections 投影
### [](https://github.com/d3/d3/blob/main/API.md#projections)[Projections](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projections)

-   [*projection*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_projection) - project the specified point from the sphere to the plane.将球体上指定的点投影到平面
-   [*projection*.invert](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_invert) - unproject the specified point from the plane to the sphere.将平面上的点反向投影到球体上
-   [*projection*.stream](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_stream) - wrap the specified stream to project geometry.将指定的流环绕到项目几何投影
-   [*projection*.preclip](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_preclip) - set the projection’s spherical clipping function.设置投影的球形剪裁函数
-   [*projection*.postclip](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_postclip) - set the projection’s cartesian clipping function.设置投影的笛卡尔剪裁函数
-   [*projection*.clipAngle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_clipAngle) - set the radius of the clip circle.设置剪裁圆半径
-   [*projection*.clipExtent](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_clipExtent) - set the viewport clip extent, in pixels.设置视口剪辑范围，像素级
-   [*projection*.scale](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_scale) - set the scale factor.设置比例因子
-   [*projection*.translate](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_translate) - set the translation offset.设置平移迁移
-   [*projection*.center](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_center) - set the center point.设置中心点
-   [*projection*.angle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_angle) - set the post-projection rotation.设置投影后旋转
-   [*projection*.reflectX](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_reflectX) - reflect the *x*-dimension.反映x方向尺寸
-   [*projection*.reflectY](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_reflectY) - reflect the *y*-dimension.反映y方向尺寸
-   [*projection*.rotate](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_rotate) - set the three-axis spherical rotation angles.设置三轴球面旋转角
-   [*projection*.precision](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_precision) - set the precision threshold for adaptive sampling.设置自适应样本的精度阈值
-   [*projection*.fitExtent](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitExtent) - set the scale and translate to fit a GeoJSON object.设置比例并转换以适合 GeoJSON 对象
-   [*projection*.fitSize](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitSize) - set the scale and translate to fit a GeoJSON object.设置比例并转换以适合 GeoJSON 对象
-   [*projection*.fitWidth](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitWidth) - set the scale and translate to fit a GeoJSON object.设置比例并转换以适合 GeoJSON 对象
-   [*projection*.fitHeight](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitHeight) - set the scale and translate to fit a GeoJSON object.设置比例并转换以适合 GeoJSON 对象
-   [d3.geoAzimuthalEqualArea](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEqualArea) - the azimuthal equal-area projection.方位角等积投影
-   [d3.geoAzimuthalEqualAreaRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEqualAreaRaw) - the raw azimuthal equal-area projection.原始方位角等积投影
-   [d3.geoAzimuthalEquidistant](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEquidistant) - the azimuthal equidistant projection.方位角等距投影
-   [d3.geoAzimuthalEquidistantRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEquidistantRaw) - the raw azimuthal equidistant projection.原始方位角等距投影
-   [d3.geoGnomonic](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGnomonic) - the gnomonic projection.日晷投影
-   [d3.geoGnomonicRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGnomonicRaw) - the raw gnomonic projection.原始日晷投影
-   [d3.geoOrthographic](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoOrthographic) - the azimuthal orthographic projection.方位正交投影
-   [d3.geoOrthographicRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoOrthographicRaw) - the raw azimuthal orthographic projection.原始方位正交投影
-   [d3.geoStereographic](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoStereographic) - the azimuthal stereographic projection.方位赤平投影
-   [d3.geoStereographicRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoStereographicRaw) - the raw azimuthal stereographic projection.原始方位赤平投影
-   [d3.geoEqualEarth](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEqualEarth) - the Equal Earth projection.等地球投影
-   [d3.geoEqualEarthRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEqualEarthRaw) - the raw Equal Earth projection.原始等地球投影
-   [d3.geoAlbersUsa](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAlbersUsa) - a composite Albers projection for the United States.美国的综合反射率预测。
-   [*conic*.parallels](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#conic_parallels) - set the two standard parallels.设置两条标准平行线
-   [d3.geoAlbers](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAlbers) - the Albers equal-area conic projection.阿尔伯斯等积圆锥投影
-   [d3.geoConicConformal](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicConformal) - the conic conformal projection.圆锥形共形投影
-   [d3.geoConicConformalRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicConformalRaw) - the raw conic conformal projection.原始圆锥形共形投影
-   [d3.geoConicEqualArea](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEqualArea) - the conic equal-area (Albers) projection.圆锥等面积 (Albers) 投影。
-   [d3.geoConicEqualAreaRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEqualAreaRaw) - the raw conic equal-area (Albers) projection.原始圆锥等面积 (Albers) 投影。
-   [d3.geoConicEquidistant](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEquidistant) - the conic equidistant projection.圆锥等距投影
-   [d3.geoConicEquidistantRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEquidistantRaw) - the raw conic equidistant projection.原始圆锥等距投影
-   [d3.geoEquirectangular](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEquirectangular) - the equirectangular (plate carreé) projection.等距柱状投影图
-   [d3.geoEquirectangularRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEquirectangularRaw) - the raw equirectangular (plate carreé) projection.原始等距柱状投影图
-   [d3.geoMercator](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoMercator) - the spherical Mercator projection.球面墨卡托投影
-   [d3.geoMercatorRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoMercatorRaw) - the raw Mercator projection.原始球面墨卡托投影
-   [d3.geoTransverseMercator](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoTransverseMercator) - the transverse spherical Mercator projection.横向球面墨卡托投影。
-   [d3.geoTransverseMercatorRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoTransverseMercatorRaw) - the raw transverse spherical Mercator projection.原始横向球面墨卡托投影。
-   [d3.geoNaturalEarth1](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoNaturalEarth1) - the Equal Earth projection, version 1.等地球投影第一版
-   [d3.geoNaturalEarth1Raw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoNaturalEarth1Raw) - the raw Equal Earth projection, version 1 原始等地球投影第一版

### [](https://github.com/d3/d3/blob/main/API.md#raw-projections)[Raw projections](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#raw-projections)

-   [*project*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_project) - project the specified point from the sphere to the plane.将指定点从球体投影到平面
-   [*project*.invert](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#project_invert) - unproject the specified point from the plane to the sphere.将指定点从平面取消投影到球体。
-   [d3.geoProjection](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoProjection) - create a custom projection.创建自定义投影
-   [d3.geoProjectionMutator](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoProjectionMutator) - create a custom configurable projection.创建自定义的可配置投影

