16-3.spherical 球形相关

### [](https://github.com/d3/d3/blob/main/API.md#spherical-math)[Spherical Math](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#spherical-math)

-   [d3.geoArea](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoArea) - compute the spherical area of a given feature.
-   [d3.geoBounds](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoBounds) - compute the latitude-longitude bounding box for a given feature.
-   [d3.geoCentroid](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoCentroid) - compute the spherical centroid of a given feature.
-   [d3.geoDistance](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoDistance) - compute the great-arc distance between two points.
-   [d3.geoLength](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoLength) - compute the length of a line string or the perimeter of a polygon.
-   [d3.geoInterpolate](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoInterpolate) - interpolate between two points along a great arc.
-   [d3.geoContains](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoContains) - test whether a point is inside a given feature.
-   [d3.geoRotation](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoRotation) - create a rotation function for the specified angles.
-   [*rotation*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_rotation) - rotate the given point around the sphere.
-   [*rotation*.invert](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#rotation_invert) - unrotate the given point around the sphere.

### [](https://github.com/d3/d3/blob/main/API.md#spherical-shapes)[Spherical Shapes](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#spherical-shapes)

-   [d3.geoCircle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoCircle) - create a circle generator.
-   [*circle*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_circle) - generate a piecewise circle as a Polygon.
-   [*circle*.center](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#circle_center) - specify the circle center in latitude and longitude.
-   [*circle*.radius](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#circle_radius) - specify the angular radius in degrees.
-   [*circle*.precision](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#circle_precision) - specify the precision of the piecewise circle.
-   [d3.geoGraticule](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGraticule) - create a graticule generator.
-   [*graticule*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_graticule) - generate a MultiLineString of meridians and parallels.
-   [*graticule*.lines](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_lines) - generate an array of LineStrings of meridians and parallels.
-   [*graticule*.outline](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_outline) - generate a Polygon of the graticule’s extent.
-   [*graticule*.extent](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_extent) - get or set the major & minor extents.
-   [*graticule*.extentMajor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_extentMajor) - get or set the major extent.
-   [*graticule*.extentMinor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_extentMinor) - get or set the minor extent.
-   [*graticule*.step](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_step) - get or set the major & minor step intervals.
-   [*graticule*.stepMajor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_stepMajor) - get or set the major step intervals.
-   [*graticule*.stepMinor](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_stepMinor) - get or set the minor step intervals.
-   [*graticule*.precision](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#graticule_precision) - get or set the latitudinal precision.
-   [d3.geoGraticule10](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGraticule10) - generate the default 10° global graticule.