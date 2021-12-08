28.timer 定时器

## [](https://github.com/d3/d3/blob/main/API.md#timers-d3-timer)[Timers (d3-timer)](https://github.com/d3/d3-timer/tree/v3.0.1)

An efficient queue for managing thousands of concurrent animations.用于管理数千个并发动画的高效队列

-   [d3.now](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#now) - get the current high-resolution time.获取当前的高分辨率时间
-   [d3.timer](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timer) - schedule a new timer.安排一个新的计时器。
-   [*timer*.restart](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timer_restart) - reset the timer’s start time and callback.重置计时器的开始时间和回调
-   [*timer*.stop](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timer_stop) - stop the timer.停止计时。
-   [d3.timerFlush](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timerFlush) - immediately execute any eligible timers.立即执行任何符合条件的计时器。
-   [d3.timeout](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timeout) - schedule a timer that stops on its first callback.安排在第一次回调时停止的计时器。
-   [d3.interval](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#interval) - schedule a timer that is called with a configurable period.安排使用可配置时段调用的计时器。