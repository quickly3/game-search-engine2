30.zooming 缩放 

## [](https://github.com/d3/d3/blob/main/API.md#zooming-d3-zoom)[Zooming (d3-zoom)](https://github.com/d3/d3-zoom/tree/v3.0.0)

Pan and zoom SVG, HTML or Canvas using mouse or touch input.

-   [d3.zoom](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom) - create a zoom behavior.
-   [*zoom*](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#_zoom) - apply the zoom behavior to the selected elements.
-   [*zoom*.transform](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_transform) - change the transform for the selected elements.
-   [*zoom*.translateBy](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_translateBy) - translate the transform for the selected elements.
-   [*zoom*.translateTo](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_translateTo) - translate the transform for the selected elements.
-   [*zoom*.scaleBy](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_scaleBy) - scale the transform for the selected elements.
-   [*zoom*.scaleTo](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_scaleTo) - scale the transform for the selected elements.
-   [*zoom*.constrain](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_constrain) - override the transform constraint logic.
-   [*zoom*.filter](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_filter) - control which input events initiate zooming.
-   [*zoom*.touchable](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_touchable) - set the touch support detector.
-   [*zoom*.wheelDelta](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_wheelDelta) - override scaling for wheel events.
-   [*zoom*.extent](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_extent) - set the extent of the viewport.
-   [*zoom*.scaleExtent](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_scaleExtent) - set the allowed scale range.
-   [*zoom*.translateExtent](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_translateExtent) - set the extent of the zoomable world.
-   [*zoom*.clickDistance](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_clickDistance) - set the click distance threshold.
-   [*zoom*.tapDistance](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_tapDistance) - set the tap distance threshold.
-   [*zoom*.duration](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_duration) - set the duration of zoom transitions.
-   [*zoom*.interpolate](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_interpolate) - control the interpolation of zoom transitions.
-   [*zoom*.on](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_on) - listen for zoom events.
-   [d3.zoomTransform](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoomTransform) - get the zoom transform for a given element.
-   [*transform*.scale](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_scale) - scale a transform by the specified amount.
-   [*transform*.translate](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_translate) - translate a transform by the specified amount.
-   [*transform*.apply](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_apply) - apply the transform to the given point.
-   [*transform*.applyX](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_applyX) - apply the transform to the given *x*-coordinate.
-   [*transform*.applyY](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_applyY) - apply the transform to the given *y*-coordinate.
-   [*transform*.invert](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_invert) - unapply the transform to the given point.
-   [*transform*.invertX](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_invertX) - unapply the transform to the given *x*-coordinate.
-   [*transform*.invertY](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_invertY) - unapply the transform to the given *y*-coordinate.
-   [*transform*.rescaleX](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_rescaleX) - apply the transform to an *x*-scale’s domain.
-   [*transform*.rescaleY](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_rescaleY) - apply the transform to a *y*-scale’s domain.
-   [*transform*.toString](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_toString) - format the transform as an SVG transform string.
-   [d3.zoomIdentity](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoomIdentity) - the identity transform.