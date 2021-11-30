16-4.streams,transform,clipping 流,变形,剪裁

### [](https://github.com/d3/d3/blob/main/API.md#streams)[Streams](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#streams)

-   [d3.geoStream](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoStream) - convert a GeoJSON object to a geometry stream.
-   [*stream*.point](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_point) - indicates a point with the specified coordinates.
-   [*stream*.lineStart](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_lineStart) - indicates the start of a line or ring.
-   [*stream*.lineEnd](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_lineEnd) - indicates the end of a line or ring.
-   [*stream*.polygonStart](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_polygonStart) - indicates the start of a polygon.
-   [*stream*.polygonEnd](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_polygonEnd) - indicates the end of a polygon.
-   [*stream*.sphere](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#stream_sphere) - indicates the sphere.

### [](https://github.com/d3/d3/blob/main/API.md#transforms)[Transforms](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#transforms)

-   [d3.geoTransform](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoTransform) - define a custom geometry transform.
-   [d3.geoIdentity](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoIdentity) - scale, translate or clip planar geometry.

### [](https://github.com/d3/d3/blob/main/API.md#clipping)[Clipping](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#clipping)

-   [*preclip*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#preclip) - pre-clipping in geographic coordinates.
-   [*postclip*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#postclip) - post-clipping in planar coordinates.
-   [d3.geoClipAntimeridian](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoClipAntimeridian) - cuts spherical geometries that cross the antimeridian.
-   [d3.geoClipCircle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoClipCircle) - clips spherical geometries to a small circle.
-   [d3.geoClipRectangle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoClipRectangle) - clips planar geometries to a rectangular viewport.