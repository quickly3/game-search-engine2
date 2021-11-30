16-2.Projections 投影
### [](https://github.com/d3/d3/blob/main/API.md#projections)[Projections](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projections)

-   [*projection*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_projection) - project the specified point from the sphere to the plane.
-   [*projection*.invert](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_invert) - unproject the specified point from the plane to the sphere.
-   [*projection*.stream](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_stream) - wrap the specified stream to project geometry.
-   [*projection*.preclip](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_preclip) - set the projection’s spherical clipping function.
-   [*projection*.postclip](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_postclip) - set the projection’s cartesian clipping function.
-   [*projection*.clipAngle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_clipAngle) - set the radius of the clip circle.
-   [*projection*.clipExtent](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_clipExtent) - set the viewport clip extent, in pixels.
-   [*projection*.scale](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_scale) - set the scale factor.
-   [*projection*.translate](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_translate) - set the translation offset.
-   [*projection*.center](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_center) - set the center point.
-   [*projection*.angle](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_angle) - set the post-projection rotation.
-   [*projection*.reflectX](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_reflectX) - reflect the *x*-dimension.
-   [*projection*.reflectY](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_reflectY) - reflect the *y*-dimension.
-   [*projection*.rotate](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_rotate) - set the three-axis spherical rotation angles.
-   [*projection*.precision](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_precision) - set the precision threshold for adaptive sampling.
-   [*projection*.fitExtent](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitExtent) - set the scale and translate to fit a GeoJSON object.
-   [*projection*.fitSize](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitSize) - set the scale and translate to fit a GeoJSON object.
-   [*projection*.fitWidth](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitWidth) - set the scale and translate to fit a GeoJSON object.
-   [*projection*.fitHeight](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#projection_fitHeight) - set the scale and translate to fit a GeoJSON object.
-   [d3.geoAzimuthalEqualArea](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEqualArea) - the azimuthal equal-area projection.
-   [d3.geoAzimuthalEqualAreaRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEqualAreaRaw) - the raw azimuthal equal-area projection.
-   [d3.geoAzimuthalEquidistant](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEquidistant) - the azimuthal equidistant projection.
-   [d3.geoAzimuthalEquidistantRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAzimuthalEquidistantRaw) - the raw azimuthal equidistant projection.
-   [d3.geoGnomonic](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGnomonic) - the gnomonic projection.
-   [d3.geoGnomonicRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoGnomonicRaw) - the raw gnomonic projection.
-   [d3.geoOrthographic](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoOrthographic) - the azimuthal orthographic projection.
-   [d3.geoOrthographicRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoOrthographicRaw) - the raw azimuthal orthographic projection.
-   [d3.geoStereographic](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoStereographic) - the azimuthal stereographic projection.
-   [d3.geoStereographicRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoStereographicRaw) - the raw azimuthal stereographic projection.
-   [d3.geoEqualEarth](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEqualEarth) - the Equal Earth projection.
-   [d3.geoEqualEarthRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEqualEarthRaw) - the raw Equal Earth projection.
-   [d3.geoAlbersUsa](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAlbersUsa) - a composite Albers projection for the United States.
-   [*conic*.parallels](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#conic_parallels) - set the two standard parallels.
-   [d3.geoAlbers](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoAlbers) - the Albers equal-area conic projection.
-   [d3.geoConicConformal](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicConformal) - the conic conformal projection.
-   [d3.geoConicConformalRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicConformalRaw) - the raw conic conformal projection.
-   [d3.geoConicEqualArea](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEqualArea) - the conic equal-area (Albers) projection.
-   [d3.geoConicEqualAreaRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEqualAreaRaw) - the raw conic equal-area (Albers) projection.
-   [d3.geoConicEquidistant](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEquidistant) - the conic equidistant projection.
-   [d3.geoConicEquidistantRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoConicEquidistantRaw) - the raw conic equidistant projection.
-   [d3.geoEquirectangular](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEquirectangular) - the equirectangular (plate carreé) projection.
-   [d3.geoEquirectangularRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoEquirectangularRaw) - the raw equirectangular (plate carreé) projection.
-   [d3.geoMercator](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoMercator) - the spherical Mercator projection.
-   [d3.geoMercatorRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoMercatorRaw) - the raw Mercator projection.
-   [d3.geoTransverseMercator](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoTransverseMercator) - the transverse spherical Mercator projection.
-   [d3.geoTransverseMercatorRaw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoTransverseMercatorRaw) - the raw transverse spherical Mercator projection.
-   [d3.geoNaturalEarth1](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoNaturalEarth1) - the Equal Earth projection, version 1.
-   [d3.geoNaturalEarth1Raw](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoNaturalEarth1Raw) - the raw Equal Earth projection, version 1

### [](https://github.com/d3/d3/blob/main/API.md#raw-projections)[Raw projections](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#raw-projections)

-   [*project*](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#_project) - project the specified point from the sphere to the plane.
-   [*project*.invert](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#project_invert) - unproject the specified point from the plane to the sphere.
-   [d3.geoProjection](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoProjection) - create a custom projection.
-   [d3.geoProjectionMutator](https://github.com/d3/d3-geo/blob/v3.0.1/README.md#geoProjectionMutator) - create a custom configurable projection.

