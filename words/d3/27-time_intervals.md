27.Time Intervals 时间间隔操作

## [](https://github.com/d3/d3/blob/main/API.md#time-intervals-d3-time)[Time Intervals (d3-time)](https://github.com/d3/d3-time/tree/v3.0.0)

A calculator for humanity’s peculiar conventions of time.一个计算人类特殊时间惯例的计算器。

-   [d3.timeInterval](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeInterval) - implement a new custom time interval.执行新的自定义时间间隔。
-   [*interval*](https://github.com/d3/d3-time/blob/v3.0.0/README.md#_interval) - alias for *interval*.floor.*interval*.floor的别名。
-   [*interval*.floor](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_floor) - round down to the nearest boundary.四舍五入到最近的边界。
-   [*interval*.round](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_round) - round to the nearest boundary.绕到最近的边界。
-   [*interval*.ceil](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_ceil) - round up to the nearest boundary.四舍五入到最近的边界
-   [*interval*.offset](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_offset) - offset a date by some number of intervals.用一定数量的间隔来抵消日期
-   [*interval*.range](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_range) - generate a range of dates at interval boundaries.在间隔边界生成一系列日期。
-   [*interval*.filter](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_filter) - create a filtered subset of this interval.创建此间隔的筛选子集。
-   [*interval*.every](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_every) - create a filtered subset of this interval.创建此间隔的筛选子集。
-   [*interval*.count](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_count) - count interval boundaries between two dates.计算两个日期之间的间隔边界。
-   [d3.timeMillisecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond), [d3.utcMillisecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond) - the millisecond interval.毫秒间隔。
-   [d3.timeMilliseconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond), [d3.utcMilliseconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond) - aliases for millisecond.range.毫秒范围的别名
-   [d3.timeSecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond), [d3.utcSecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond) - the second interval.第二次间歇。
-   [d3.timeSeconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond), [d3.utcSeconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond) - aliases for second.range.second.range的别名。
-   [d3.timeMinute](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute), [d3.utcMinute](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute) - the minute interval.一分钟的间隔。
-   [d3.timeMinutes](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute), [d3.utcMinutes](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute) - aliases for minute.range.minute.range的别名。
-   [d3.timeHour](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour), [d3.utcHour](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour) - the hour interval.小时间隔。
-   [d3.timeHours](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour), [d3.utcHours](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour) - aliases for hour.range.hour.range的别名。
-   [d3.timeDay](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay), [d3.utcDay](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay) - the day interval.日间隔
-   [d3.timeDays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay), [d3.utcDays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay) - aliases for day.range.day.range的别名。
-   [d3.timeWeek](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek), [d3.utcWeek](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek) - aliases for sunday.星期天的别名
-   [d3.timeWeeks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek), [d3.utcWeeks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek) - aliases for week.range.week.range的别名。
-   [d3.timeSunday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday), [d3.utcSunday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday) - the week interval, starting on Sunday.从周日开始的一周间隔。
-   [d3.timeSundays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday), [d3.utcSundays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday) - aliases for sunday.range.sunday.range的别名
-   [d3.timeMonday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday), [d3.utcMonday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday) - the week interval, starting on Monday.从周一开始的一周间隔
-   [d3.timeMondays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday), [d3.utcMondays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday) - aliases for monday.range.monday.range的别名
-   [d3.timeTuesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday), [d3.utcTuesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday) - the week interval, starting on Tuesday.从星期二开始的一周间隔。
-   [d3.timeTuesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday), [d3.utcTuesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday) - aliases for tuesday.range.tuesday.range的别名。
-   [d3.timeWednesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday), [d3.utcWednesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday) - the week interval, starting on Wednesday.从周三开始的一周间隔
-   [d3.timeWednesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday), [d3.utcWednesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday) - aliases for wednesday.range.wednesday.range.的别名
-   [d3.timeThursday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday), [d3.utcThursday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday) - the week interval, starting on Thursday.从星期四开始的一周间隔
-   [d3.timeThursdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday), [d3.utcThursdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday) - aliases for thursday.range.thursday.range的别名
-   [d3.timeFriday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday), [d3.utcFriday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday) - the week interval, starting on Friday.从周五开始的一周间隔。
-   [d3.timeFridays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday), [d3.utcFridays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday) - aliases for friday.range.friday.range的别名
-   [d3.timeSaturday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday), [d3.utcSaturday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday) - the week interval, starting on Saturday.从星期六开始的一周休息。
-   [d3.timeSaturdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday), [d3.utcSaturdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday) - aliases for saturday.range.saturday.range的别名
-   [d3.timeMonth](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth), [d3.utcMonth](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth) - the month interval.月份间隔。
-   [d3.timeMonths](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth), [d3.utcMonths](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth) - aliases for month.range.month.range的别名
-   [d3.timeYear](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear), [d3.utcYear](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear) - the year interval.年间隔
-   [d3.timeYears](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear), [d3.utcYears](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear) - aliases for year.range.  year.range的别名
-   [d3.timeTicks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTicks), [d3.utcTicks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#utcTicks) -
-   [d3.timeTickInterval](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTickInterval), [d3.utcTickInterval](https://github.com/d3/d3-time/blob/v3.0.0/README.md#utcTickInterval) -