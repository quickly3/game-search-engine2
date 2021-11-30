12.Easings 缓慢效果（淡入，淡出等）
## [](https://github.com/d3/d3/blob/main/API.md#easings-d3-ease)[Easings (d3-ease)](https://github.com/d3/d3-ease/tree/v3.0.1)

Easing functions for smooth animation.

-   [*ease*](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#_ease) - ease the given normalized time.
-   [d3.easeLinear](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeLinear) - linear easing; the identity function.
-   [d3.easePolyIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePolyIn) - polynomial easing; raises time to the given power.
-   [d3.easePolyOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePolyOut) - reverse polynomial easing.
-   [d3.easePoly](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePoly) - an alias for easePolyInOut.
-   [d3.easePolyInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePolyInOut) - symmetric polynomial easing.
-   [*poly*.exponent](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#poly_exponent) - specify the polynomial exponent.
-   [d3.easeQuadIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuadIn) - quadratic easing; squares time.
-   [d3.easeQuadOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuadOut) - reverse quadratic easing.
-   [d3.easeQuad](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuad) - an alias for easeQuadInOut.
-   [d3.easeQuadInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuadInOut) - symmetric quadratic easing.
-   [d3.easeCubicIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubicIn) - cubic easing; cubes time.
-   [d3.easeCubicOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubicOut) - reverse cubic easing.
-   [d3.easeCubic](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubic) - an alias for easeCubicInOut.
-   [d3.easeCubicInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubicInOut) - symmetric cubic easing.
-   [d3.easeSinIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSinIn) - sinusoidal easing.
-   [d3.easeSinOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSinOut) - reverse sinusoidal easing.
-   [d3.easeSin](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSin) - an alias for easeSinInOut.
-   [d3.easeSinInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSinInOut) - symmetric sinusoidal easing.
-   [d3.easeExpIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExpIn) - exponential easing.
-   [d3.easeExpOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExpOut) - reverse exponential easing.
-   [d3.easeExp](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExp) - an alias for easeExpInOut.
-   [d3.easeExpInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExpInOut) - symmetric exponential easing.
-   [d3.easeCircleIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircleIn) - circular easing.
-   [d3.easeCircleOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircleOut) - reverse circular easing.
-   [d3.easeCircle](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircle) - an alias for easeCircleInOut.
-   [d3.easeCircleInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircleInOut) - symmetric circular easing.
-   [d3.easeElasticIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElasticIn) - elastic easing, like a rubber band.
-   [d3.easeElastic](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElastic) - an alias for easeElasticOut.
-   [d3.easeElasticOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElasticOut) - reverse elastic easing.
-   [d3.easeElasticInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElasticInOut) - symmetric elastic easing.
-   [*elastic*.amplitude](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#elastic_amplitude) - specify the elastic amplitude.
-   [*elastic*.period](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#elastic_period) - specify the elastic period.
-   [d3.easeBackIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBackIn) - anticipatory easing, like a dancer bending his knees before jumping.
-   [d3.easeBackOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBackOut) - reverse anticipatory easing.
-   [d3.easeBack](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBack) - an alias for easeBackInOut.
-   [d3.easeBackInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBackInOut) - symmetric anticipatory easing.
-   [*back*.overshoot](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#back_overshoot) - specify the amount of overshoot.
-   [d3.easeBounceIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounceIn) - bounce easing, like a rubber ball.
-   [d3.easeBounce](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounce) - an alias for easeBounceOut.
-   [d3.easeBounceOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounceOut) - reverse bounce easing.
-   [d3.easeBounceInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounceInOut) - symmetric bounce easing.