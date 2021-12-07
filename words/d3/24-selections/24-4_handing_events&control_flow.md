24-4.handing events & control flow 操作事件 控制流

### [](https://github.com/d3/d3/blob/main/API.md#handling-events)[Handling Events](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#handling-events)

-   [*selection*.on](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_on) - add or remove event listeners.添加或删除事件侦听器
-   [*selection*.dispatch](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_dispatch) - dispatch a custom event.指定自定义事件。
-   [d3.pointer](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#pointer) - get the pointer’s position of an event.获取事件的指针位置。
-   [d3.pointers](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#pointers) - get the pointers’ positions of an event.获取事件指针的位置。

### [](https://github.com/d3/d3/blob/main/API.md#control-flow)[Control Flow](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#control-flow)

-   [*selection*.each](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_each) - call a function for each element.为每个元素调用一个函数。
-   [*selection*.call](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_call) - call a function with this selection.使用此选项调用函数。
-   [*selection*.empty](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_empty) - returns true if this selection is empty.如果此选择为空，则返回true。
-   [*selection*.nodes](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_nodes) - returns an array of all selected elements.返回所有选定元素的数组。
-   [*selection*.node](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_node) - returns the first (non-null) element.返回第一个（非空）元素。
-   [*selection*.size](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_size) - returns the count of elements.返回元素的计数。
-   [*selection*[Symbol.iterator]](https://github.com/d3/d3-selection/blob/v3.0.0/README.md#selection_iterator) - iterate over the selection’s nodes.迭代选择的节点。