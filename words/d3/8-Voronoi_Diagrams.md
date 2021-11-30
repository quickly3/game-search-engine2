8.Voronoi Diagrams 沃罗诺伊图
## [](https://github.com/d3/d3/blob/main/API.md#voronoi-diagrams-d3-delaunay)[Voronoi Diagrams (d3-delaunay)](https://github.com/d3/d3-delaunay/tree/v6.0.2)

Compute the Voronoi diagram of a set of two-dimensional points.
使用二维点计算沃罗诺伊图

-   [new Delaunay](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#new_Delaunay) - create a delaunay triangulation for an array of point coordinates.
-   [Delaunay.from](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_from) - create a delaunay triangulation for an iterable of points.
-   [*delaunay*.points](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_points) - the coordinates of the points.
-   [*delaunay*.halfedges](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_halfedges) - the delaunay halfedges.
-   [*delaunay*.hull](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_hull) - the convex hull as point indices.
-   [*delaunay*.triangles](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_triangles) - the delaunay triangles.
-   [*delaunay*.inedges](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_inedges) - the delaunay inedges
-   [*delaunay*.find](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_find) - find the closest point in the delaunay triangulation.
-   [*delaunay*.neighbors](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_neighbors) - the neighbors of a point in the delaunay triangulation.
-   [*delaunay*.render](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_render) - render the edges of the delaunay triangulation.
-   [*delaunay*.renderHull](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_renderHull) - render the convex hull.
-   [*delaunay*.renderTriangle](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_renderTriangle) - render a triangle.
-   [*delaunay*.renderPoints](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_renderPoints) - render the points.
-   [*delaunay*.hullPolygon](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_hullPolygon) - the closed convex hull as point coordinates.
-   [*delaunay*.trianglePolygons](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_trianglePolygons) - iterate over all the triangles as polygons.
-   [*delaunay*.trianglePolygon](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_trianglePolygon) - return a triangle as a polygon.
-   [*delaunay*.update](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_update) - update a delaunay triangulation in place.
-   [*delaunay*.voronoi](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#delaunay_voronoi) - compute the voronoi diagram associated with a delaunay triangulation.
-   [*voronoi*.delaunay](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_delaunay) - the voronoi diagram’s source delaunay triangulation.
-   [*voronoi*.circumcenters](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_circumcenters) - the triangles’ circumcenters.
-   [*voronoi*.vectors](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_vectors) - directions for the outer (infinite) cells of the voronoi diagram.
-   [*voronoi*.xmin](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_xmin) - set the *xmin* bound of the extent.
-   [*voronoi*.ymin](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_ymin) - set the *ymin* bound of the extent.
-   [*voronoi*.xmax](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_xmax) - set the *xmax* bound of the extent.
-   [*voronoi*.ymax](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_ymax) - set the *ymax* bound of the extent.
-   [*voronoi*.contains](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_contains) - test whether a point is inside a voronoi cell.
-   [*voronoi*.neighbors](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_neighbors) - the neighbors of a point in the voronoi diagram.
-   [*voronoi*.render](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_render) - render the mesh of voronoi cells.
-   [*voronoi*.renderBounds](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_renderBounds) - render the extent.
-   [*voronoi*.renderCell](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_renderCell) - render a voronoi cell.
-   [*voronoi*.cellPolygons](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_cellPolygons) - iterate over all the cells as polygons.
-   [*voronoi*.cellPolygon](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_cellPolygon) - return a cell as a polygon.
-   [*voronoi*.update](https://github.com/d3/d3-delaunay/blob/v6.0.2/README.md#voronoi_update) - update a voronoi diagram in place.