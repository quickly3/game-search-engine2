16-4.streams,transform,clipping 流,变形,剪裁

### [](https://github.com/d3/d3/blob/main/API.md#streams)[Streams](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#streams)

-   [d3.geoStream](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoStream) - convert a GeoJSON object to a geometry stream.将 GeoJSON 对象转换为几何流
-   [*stream*.point](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_point) - indicates a point with the specified coordinates.表示具有指定坐标的点
-   [*stream*.lineStart](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_lineStart) - indicates the start of a line or ring.表示线路或环的开始
-   [*stream*.lineEnd](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_lineEnd) - indicates the end of a line or ring.表示线路或环的结束
-   [*stream*.polygonStart](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_polygonStart) - indicates the start of a polygon.表示多边形的开始
-   [*stream*.polygonEnd](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_polygonEnd) - indicates the end of a polygon.表示多边形的结束
-   [*stream*.sphere](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_sphere) - indicates the sphere.表示球体

### [](https://github.com/d3/d3/blob/main/API.md#transforms)[Transforms](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#transforms)

-   [d3.geoTransform](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoTransform) - define a custom geometry transform.定义自定义几何变换
-   [d3.geoIdentity](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoIdentity) - scale, translate or clip planar geometry.缩放、平移或裁剪平面几何图形

### [](https://github.com/d3/d3/blob/main/API.md#clipping)[Clipping](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#clipping)

-   [*preclip*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#preclip) - pre-clipping in geographic coordinates.地理坐标中的预剪裁
-   [*postclip*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#postclip) - post-clipping in planar coordinates.平面坐标中的后裁剪
-   [d3.geoClipAntimeridian](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoClipAntimeridian) - cuts spherical geometries that cross the antimeridian.切割穿过反子午线的球形几何图形
-   [d3.geoClipCircle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoClipCircle) - clips spherical geometries to a small circle.将球形几何图形剪裁成一个小圆圈
-   [d3.geoClipRectangle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoClipRectangle) - clips planar geometries to a rectangular viewport.将平面几何图形剪辑到矩形视口