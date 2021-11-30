29.transitions 过渡效果

## [](https://github.com/d3/d3/blob/main/API.md#transitions-d3-transition)[Transitions (d3-transition)](https://github.com/d3/d3-transition/tree/v3.0.1)

Animated transitions for [selections](https://github.com/d3/d3/blob/main/API.md#selections).

-   [*selection*.transition](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#selection_transition) - schedule a transition for the selected elements.
-   [*selection*.interrupt](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#selection_interrupt) - interrupt and cancel transitions on the selected elements.
-   [d3.interrupt](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#interrupt) - interrupt the active transition for a given node.
-   [d3.transition](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition) - schedule a transition on the root document element.
-   [*transition*.select](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_select) - schedule a transition on the selected elements.
-   [*transition*.selectAll](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selectAll) - schedule a transition on the selected elements.
-   [*transition*.selectChild](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selectChild) - select a child element for each selected element.
-   [*transition*.selectChildren](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selectChildren) - select the children elements for each selected element.
-   [*transition*.selection](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_selection) - returns a selection for this transition.
-   [*transition*.filter](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_filter) - filter elements based on data.
-   [*transition*.merge](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_merge) - merge this transition with another.
-   [*transition*.transition](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_transition) - schedule a new transition following this one.
-   [d3.active](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#active) - select the active transition for a given node.
-   [*transition*.attr](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_attr) - tween the given attribute using the default interpolator.
-   [*transition*.attrTween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_attrTween) - tween the given attribute using a custom interpolator.
-   [*transition*.style](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_style) - tween the given style property using the default interpolator.
-   [*transition*.styleTween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_styleTween) - tween the given style property using a custom interpolator.
-   [*transition*.text](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_text) - set the text content when the transition starts.
-   [*transition*.textTween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_textTween) - tween the text using a custom interpolator.
-   [*transition*.remove](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_remove) - remove the selected elements when the transition ends.
-   [*transition*.tween](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_tween) - run custom code during the transition.
-   [*transition*.delay](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_delay) - specify per-element delay in milliseconds.
-   [*transition*.duration](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_duration) - specify per-element duration in milliseconds.
-   [*transition*.ease](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_ease) - specify the easing function.
-   [*transition*.easeVarying](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_easeVarying) - specify an easing function factory.
-   [*transition*.end](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_end) - a promise that resolves when a transition ends.
-   [*transition*.on](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_on) - await the end of a transition.
-   [*transition*.each](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_each) - call a function for each element.
-   [*transition*.call](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_call) - call a function with this transition.
-   [*transition*.empty](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_empty) - returns true if this transition is empty.
-   [*transition*.nodes](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_nodes) - returns an array of all selected elements.
-   [*transition*.node](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_node) - returns the first (non-null) element.
-   [*transition*.size](https://github.com/d3/d3-transition/blob/v3.0.0/README.md#transition_size) - returns the count of elements.