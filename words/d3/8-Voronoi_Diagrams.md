8.Voronoi Diagrams 沃罗诺伊图
## [](https://github.com/d3/d3/blob/main/API.md#voronoi-diagrams-d3-delaunay)[Voronoi Diagrams (d3-delaunay)](https://github.com/d3/d3-delaunay/tree/v6.0.2)

Compute the Voronoi diagram of a set of two-dimensional points.
使用二维点计算沃罗诺伊图

-   [new Delaunay](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#new_Delaunay) - create a delaunay triangulation for an array of point coordinates.为一组坐标数组创建一个劳德三角剖分
-   [Delaunay.from](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_from) - create a delaunay triangulation for an iterable of points. 为一组可迭代点创建劳德三角剖分
-   [*delaunay*.points](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_points) - the coordinates of the points. 获取delaunay内的点坐标
-   [*delaunay*.halfedges](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_halfedges) - the delaunay halfedges.获得delaunay 半边数据结构
-   [*delaunay*.hull](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_hull) - the convex hull as point indices. 获得作为点索引的凸包
-   [*delaunay*.triangles](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_triangles) - the delaunay triangles.获得delaunay三角
-   [*delaunay*.inedges](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_inedges) - the delaunay inedges 获取delaunay内边
-   [*delaunay*.find](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_find) - find the closest point in the delaunay triangulation.查找delaunay三角上最近的点
-   [*delaunay*.neighbors](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_neighbors) - the neighbors of a point in the delaunay triangulation.获得delaunay上某点附近的点
-   [*delaunay*.render](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_render) - render the edges of the delaunay triangulation.渲染delaunay三角的边
-   [*delaunay*.renderHull](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_renderHull) - render the convex hull.渲染delaunay三角的的凸包
-   [*delaunay*.renderTriangle](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_renderTriangle) - render a triangle.渲染一个三角形
-   [*delaunay*.renderPoints](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_renderPoints) - render the points.渲染点
-   [*delaunay*.hullPolygon](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_hullPolygon) - the closed convex hull as point coordinates.作为点坐标的闭凸包
-   [*delaunay*.trianglePolygons](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_trianglePolygons) - iterate over all the triangles as polygons.迭代所有三角形作为一个多边形
-   [*delaunay*.trianglePolygon](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_trianglePolygon) - return a triangle as a polygon.将三角形返回为多边形 
-   [*delaunay*.update](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_update) - update a delaunay triangulation in place.平稳的更新德劳内三角
-   [*delaunay*.voronoi](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_voronoi) - compute the voronoi diagram associated with a delaunay triangulation.计算出delaunay三角相关的沃罗诺伊图
-   [*voronoi*.delaunay](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_delaunay) - the voronoi diagram’s source delaunay triangulation.获得沃罗诺伊图相关的dalaunay三角
-   [*voronoi*.circumcenters](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_circumcenters) - the triangles’ circumcenters.三角外心
-   [*voronoi*.vectors](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_vectors) - directions for the outer (infinite) cells of the voronoi diagram.沃罗诺伊图外部空间方向
-   [*voronoi*.xmin](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_xmin) - set the *xmin* bound of the extent.设置x轴方向上的区域最小边界
-   [*voronoi*.ymin](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_ymin) - set the *ymin* bound of the extent.设置y轴方向上的区域最小边界
-   [*voronoi*.xmax](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_xmax) - set the *xmax* bound of the extent.设置x轴方向上的区域最大边界
-   [*voronoi*.ymax](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_ymax) - set the *ymax* bound of the extent.设置y轴方向上的区域最大边界
-   [*voronoi*.contains](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_contains) - test whether a point is inside a voronoi cell.测试一个点是否在一个沃罗诺伊单位内
-   [*voronoi*.neighbors](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_neighbors) - the neighbors of a point in the voronoi diagram.获得沃罗诺伊图中一个点附近的
-   [*voronoi*.render](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_render) - render the mesh of voronoi cells.渲染沃罗诺伊单位组成的网
-   [*voronoi*.renderBounds](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_renderBounds) - render the extent.渲染区域
-   [*voronoi*.renderCell](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_renderCell) - render a voronoi cell.渲染一个沃罗诺伊单位
-   [*voronoi*.cellPolygons](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_cellPolygons) - iterate over all the cells as polygons.迭代所有单位作为一个多边形
-   [*voronoi*.cellPolygon](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_cellPolygon) - return a cell as a polygon.返回一个多变形细胞
-   [*voronoi*.update](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_update) - update a voronoi diagram in place.平和的更新一个沃罗诺伊图