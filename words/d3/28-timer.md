28.timer 定时器

## [](https://github.com/d3/d3/blob/main/API.md#timers-d3-timer)[Timers (d3-timer)](https://github.com/d3/d3-timer/tree/v3.0.1)

An efficient queue for managing thousands of concurrent animations.

-   [d3.now](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#now) - get the current high-resolution time.
-   [d3.timer](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timer) - schedule a new timer.
-   [*timer*.restart](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timer_restart) - reset the timer’s start time and callback.
-   [*timer*.stop](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timer_stop) - stop the timer.
-   [d3.timerFlush](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timerFlush) - immediately execute any eligible timers.
-   [d3.timeout](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#timeout) - schedule a timer that stops on its first callback.
-   [d3.interval](https://github.com/d3/d3-timer/blob/v3.0.1/README.md#interval) - schedule a timer that is called with a configurable period.