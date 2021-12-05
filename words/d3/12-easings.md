12.Easings 缓动效果（淡入，淡出等）
## [](https://github.com/d3/d3/blob/main/API.md#easings-d3-ease)[Easings (d3-ease)](https://github.com/d3/d3-ease/tree/v3.0.1)

Easing functions for smooth animation.

-   [*ease*](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#_ease) - ease the given normalized time.使用指定的标准化事件初始化”缓动“对象
-   [d3.easeLinear](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeLinear) - linear easing; the identity function.线性缓动，匀加速
-   [d3.easePolyIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePolyIn) - polynomial easing; raises time to the given power.缓入; 多项式缓动
-   [d3.easePolyOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePolyOut) - reverse polynomial easing.缓出
-   [d3.easePoly](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePoly) - an alias for easePolyInOut.easePolyInOut的别名
-   [d3.easePolyInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easePolyInOut) - symmetric polynomial easing.对称多项式缓动
-   [*poly*.exponent](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#poly_exponent) - specify the polynomial exponent.设置多项式指数
-   [d3.easeQuadIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuadIn) - quadratic easing; squares time.二次方缓动（二次方缓入）
-   [d3.easeQuadOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuadOut) - reverse quadratic easing.反转二次方缓动 二次方缓出
-   [d3.easeQuad](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuad) - an alias for easeQuadInOut.easeQuadInOut 的别名
-   [d3.easeQuadInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeQuadInOut) - symmetric quadratic easing.对称二次方缓动
-   [d3.easeCubicIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubicIn) - cubic easing; cubes time.三次方缓动（缓入）
-   [d3.easeCubicOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubicOut) - reverse cubic easing.三次方缓动（缓出）
-   [d3.easeCubic](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubic) - an alias for easeCubicInOut. easeCubicInOut别名
-   [d3.easeCubicInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCubicInOut) - symmetric cubic easing.对称三次方缓动
-   [d3.easeSinIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSinIn) - sinusoidal easing.正弦缓动
-   [d3.easeSinOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSinOut) - reverse sinusoidal easing.反正弦缓动
-   [d3.easeSin](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSin) - an alias for easeSinInOut.easeSinInOut别名
-   [d3.easeSinInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeSinInOut) - symmetric sinusoidal easing.对称正弦缓动
-   [d3.easeExpIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExpIn) - exponential easing.指数缓动
-   [d3.easeExpOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExpOut) - reverse exponential easing.反指数缓动
-   [d3.easeExp](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExp) - an alias for easeExpInOut.easeExpInOut别名
-   [d3.easeExpInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeExpInOut) - symmetric exponential easing.对称指数缓动
-   [d3.easeCircleIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircleIn) - circular easing.环形缓动
-   [d3.easeCircleOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircleOut) - reverse circular easing.反环形缓动
-   [d3.easeCircle](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircle) - an alias for easeCircleInOut.easeCircleInOut别名
-   [d3.easeCircleInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeCircleInOut) - symmetric circular easing.对称环形缓动
-   [d3.easeElasticIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElasticIn) - elastic easing, like a rubber band.弹性缓动（橡皮筋）
-   [d3.easeElastic](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElastic) - an alias for easeElasticOut.easeElasticOut别名
-   [d3.easeElasticOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElasticOut) - reverse elastic easing.反弹性缓动
-   [d3.easeElasticInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeElasticInOut) - symmetric elastic easing.对称弹性缓动
-   [*elastic*.amplitude](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#elastic_amplitude) - specify the elastic amplitude.指定弹性震幅
-   [*elastic*.period](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#elastic_period) - specify the elastic period.指定弹性时间
-   [d3.easeBackIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBackIn) - anticipatory easing, like a dancer bending his knees before jumping.期望缓动 （像一个舞者有预备动作的起跳）
-   [d3.easeBackOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBackOut) - reverse anticipatory easing.反期望缓动
-   [d3.easeBack](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBack) - an alias for easeBackInOut. easeBackInOut别名
-   [d3.easeBackInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBackInOut) - symmetric anticipatory easing.对称期望缓动
-   [*back*.overshoot](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#back_overshoot) - specify the amount of overshoot.设置突破额
-   [d3.easeBounceIn](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounceIn) - bounce easing, like a rubber ball.反弹缓动
-   [d3.easeBounce](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounce) - an alias for easeBounceOut.easeBounceOut别名
-   [d3.easeBounceOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounceOut) - reverse bounce easing.反反弹缓动
-   [d3.easeBounceInOut](https://github.com/d3/d3-ease/blob/v3.0.1/README.md#easeBounceInOut) - symmetric bounce easing.对称反弹缓动