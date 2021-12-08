29.transitions 过渡效果

## [](https://github.com/d3/d3/blob/main/API.md#transitions-d3-transition)[Transitions (d3-transition)](https://github.com/d3/d3-transition/tree/v3.0.1)

Animated transitions for [selections](https://github.com/d3/d3/blob/main/API.md#selections).选择的动画过渡。

-   [*selection*.transition](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#selection_transition) - schedule a transition for the selected elements.为选定图元安排过渡。
-   [*selection*.interrupt](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#selection_interrupt) - interrupt and cancel transitions on the selected elements.中断和取消选定元素上的转换。
-   [d3.interrupt](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#interrupt) - interrupt the active transition for a given node.中断给定节点的活动转换。
-   [d3.transition](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition) - schedule a transition on the root document element.在根文档元素上安排转换。
-   [*transition*.select](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_select) - schedule a transition on the selected elements.在选定图元上计划过渡。
-   [*transition*.selectAll](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selectAll) - schedule a transition on the selected elements.在选定图元上计划过渡。
-   [*transition*.selectChild](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selectChild) - select a child element for each selected element.为每个选定元素选择一个子元素。
-   [*transition*.selectChildren](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selectChildren) - select the children elements for each selected element.为每个选定元素选择子元素。
-   [*transition*.selection](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selection) - returns a selection for this transition.返回此转换的选择。
-   [*transition*.filter](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_filter) - filter elements based on data.基于数据的过滤器元件。
-   [*transition*.merge](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_merge) - merge this transition with another.将此转换与另一个转换合并。
-   [*transition*.transition](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_transition) - schedule a new transition following this one.在此之后安排一个新的过渡。
-   [d3.active](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#active) - select the active transition for a given node.为给定节点选择活动转换。
-   [*transition*.attr](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_attr) - tween the given attribute using the default interpolator.使用默认插值器在给定属性之间进行插值。
-   [*transition*.attrTween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_attrTween) - tween the given attribute using a custom interpolator.使用自定义插值器在给定属性之间进行插值。
-   [*transition*.style](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_style) - tween the given style property using the default interpolator.使用默认插值器在给定样式特性之间切换。
-   [*transition*.styleTween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_styleTween) - tween the given style property using a custom interpolator.使用自定义插值器在给定样式特性之间切换。
-   [*transition*.text](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_text) - set the text content when the transition starts.设置转换开始时的文本内容。
-   [*transition*.textTween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_textTween) - tween the text using a custom interpolator.使用自定义插值器在文本之间进行插值。
-   [*transition*.remove](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_remove) - remove the selected elements when the transition ends.过渡结束时删除选定的图元。
-   [*transition*.tween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_tween) - run custom code during the transition.在转换期间运行自定义代码。
-   [*transition*.delay](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_delay) - specify per-element delay in milliseconds.以毫秒为单位指定每个元素的延迟。
-   [*transition*.duration](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_duration) - specify per-element duration in milliseconds.以毫秒为单位指定每个元素的持续时间。
-   [*transition*.ease](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_ease) - specify the easing function.指定缓动函数。
-   [*transition*.easeVarying](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_easeVarying) - specify an easing function factory.指定缓动函数工厂
-   [*transition*.end](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_end) - a promise that resolves when a transition ends.在转换结束时解决的承诺。
-   [*transition*.on](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_on) - await the end of a transition.等待过渡的结束。
-   [*transition*.each](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_each) - call a function for each element.为每个元素调用一个函数。
-   [*transition*.call](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_call) - call a function with this transition.使用此转换调用函数。
-   [*transition*.empty](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_empty) - returns true if this transition is empty.如果此转换为空，则返回true。
-   [*transition*.nodes](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_nodes) - returns an array of all selected elements.返回所有选定元素的数组。
-   [*transition*.node](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_node) - returns the first (non-null) element.返回第一个（非空）元素。
-   [*transition*.size](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_size) - returns the count of elements.返回元素的计数。