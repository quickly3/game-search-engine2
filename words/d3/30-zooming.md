30.zooming 缩放 

## [](https://github.com/d3/d3/blob/main/API.md#zooming-d3-zoom)[Zooming (d3-zoom)](https://github.com/d3/d3-zoom/tree/v3.0.0)

Pan and zoom SVG, HTML or Canvas using mouse or touch input.使用鼠标或触摸输入平移和缩放SVG、HTML或画布。

-   [d3.zoom](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom) - create a zoom behavior.创建缩放行为。
-   [*zoom*](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#_zoom) - apply the zoom behavior to the selected elements.将缩放行为应用于选定图元。
-   [*zoom*.transform](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_transform) - change the transform for the selected elements.更改选定元素的变换。
-   [*zoom*.translateBy](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_translateBy) - translate the transform for the selected elements.平移选定元素的变换。
-   [*zoom*.translateTo](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_translateTo) - translate the transform for the selected elements.平移选定元素的变换。
-   [*zoom*.scaleBy](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_scaleBy) - scale the transform for the selected elements.缩放选定元素的变换。
-   [*zoom*.scaleTo](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_scaleTo) - scale the transform for the selected elements.缩放选定元素的变换。
-   [*zoom*.constrain](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_constrain) - override the transform constraint logic.覆盖变换约束逻辑。
-   [*zoom*.filter](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_filter) - control which input events initiate zooming.控制哪些输入事件启动缩放。
-   [*zoom*.touchable](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_touchable) - set the touch support detector.设置触摸支持检测器。
-   [*zoom*.wheelDelta](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_wheelDelta) - override scaling for wheel events.覆盖控制盘事件的缩放。
-   [*zoom*.extent](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_extent) - set the extent of the viewport.设置视口的范围。
-   [*zoom*.scaleExtent](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_scaleExtent) - set the allowed scale range.设置允许的刻度范围。
-   [*zoom*.translateExtent](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_translateExtent) - set the extent of the zoomable world.设置可缩放世界的范围。
-   [*zoom*.clickDistance](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_clickDistance) - set the click distance threshold.设置“单击距离”阈值。
-   [*zoom*.tapDistance](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_tapDistance) - set the tap distance threshold.设置分接距离阈值。
-   [*zoom*.duration](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_duration) - set the duration of zoom transitions.设置缩放变换的持续时间
-   [*zoom*.interpolate](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_interpolate) - control the interpolation of zoom transitions.控制缩放变换的插值。
-   [*zoom*.on](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoom_on) - listen for zoom events.收听缩放事件。
-   [d3.zoomTransform](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoomTransform) - get the zoom transform for a given element.获取给定元素的缩放变换。
-   [*transform*.scale](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_scale) - scale a transform by the specified amount.按指定的量缩放变换。
-   [*transform*.translate](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_translate) - translate a transform by the specified amount.按指定的量转换变换。
-   [*transform*.apply](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_apply) - apply the transform to the given point.将变换应用于给定点。
-   [*transform*.applyX](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_applyX) - apply the transform to the given *x*-coordinate.将变换应用于给定的*x*-坐标
-   [*transform*.applyY](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_applyY) - apply the transform to the given *y*-coordinate.将变换应用于给定的*y*-坐标。
-   [*transform*.invert](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_invert) - unapply the transform to the given point.将变换取消应用到给定点。
-   [*transform*.invertX](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_invertX) - unapply the transform to the given *x*-coordinate.将变换取消应用到给定的*x*-坐标。
-   [*transform*.invertY](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_invertY) - unapply the transform to the given *y*-coordinate.将变换取消应用到给定的*y*-坐标。
-   [*transform*.rescaleX](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_rescaleX) - apply the transform to an *x*-scale’s domain.将变换应用于*x*比例的域。
-   [*transform*.rescaleY](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_rescaleY) - apply the transform to a *y*-scale’s domain.将变换应用于*y*-比例的域。
-   [*transform*.toString](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#transform_toString) - format the transform as an SVG transform string.将转换格式化为SVG转换字符串。
-   [d3.zoomIdentity](https://github.com/d3/d3-zoom/blob/v3.0.0/README.md#zoomIdentity) - the identity transform.标识符转换。