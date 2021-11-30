27.Time Intervals 时间间隔操作

## [](https://github.com/d3/d3/blob/main/API.md#time-intervals-d3-time)[Time Intervals (d3-time)](https://github.com/d3/d3-time/tree/v3.0.0)

A calculator for humanity’s peculiar conventions of time.

-   [d3.timeInterval](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeInterval) - implement a new custom time interval.
-   [*interval*](https://github.com/d3/d3-time/blob/v3.0.0/README.md#_interval) - alias for *interval*.floor.
-   [*interval*.floor](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_floor) - round down to the nearest boundary.
-   [*interval*.round](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_round) - round to the nearest boundary.
-   [*interval*.ceil](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_ceil) - round up to the nearest boundary.
-   [*interval*.offset](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_offset) - offset a date by some number of intervals.
-   [*interval*.range](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_range) - generate a range of dates at interval boundaries.
-   [*interval*.filter](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_filter) - create a filtered subset of this interval.
-   [*interval*.every](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_every) - create a filtered subset of this interval.
-   [*interval*.count](https://github.com/d3/d3-time/blob/v3.0.0/README.md#interval_count) - count interval boundaries between two dates.
-   [d3.timeMillisecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond), [d3.utcMillisecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond) - the millisecond interval.
-   [d3.timeMilliseconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond), [d3.utcMilliseconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMillisecond) - aliases for millisecond.range.
-   [d3.timeSecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond), [d3.utcSecond](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond) - the second interval.
-   [d3.timeSeconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond), [d3.utcSeconds](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSecond) - aliases for second.range.
-   [d3.timeMinute](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute), [d3.utcMinute](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute) - the minute interval.
-   [d3.timeMinutes](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute), [d3.utcMinutes](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMinute) - aliases for minute.range.
-   [d3.timeHour](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour), [d3.utcHour](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour) - the hour interval.
-   [d3.timeHours](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour), [d3.utcHours](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeHour) - aliases for hour.range.
-   [d3.timeDay](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay), [d3.utcDay](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay) - the day interval.
-   [d3.timeDays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay), [d3.utcDays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeDay) - aliases for day.range.
-   [d3.timeWeek](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek), [d3.utcWeek](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek) - aliases for sunday.
-   [d3.timeWeeks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek), [d3.utcWeeks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWeek) - aliases for week.range.
-   [d3.timeSunday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday), [d3.utcSunday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday) - the week interval, starting on Sunday.
-   [d3.timeSundays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday), [d3.utcSundays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSunday) - aliases for sunday.range.
-   [d3.timeMonday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday), [d3.utcMonday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday) - the week interval, starting on Monday.
-   [d3.timeMondays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday), [d3.utcMondays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonday) - aliases for monday.range.
-   [d3.timeTuesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday), [d3.utcTuesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday) - the week interval, starting on Tuesday.
-   [d3.timeTuesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday), [d3.utcTuesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTuesday) - aliases for tuesday.range.
-   [d3.timeWednesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday), [d3.utcWednesday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday) - the week interval, starting on Wednesday.
-   [d3.timeWednesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday), [d3.utcWednesdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeWednesday) - aliases for wednesday.range.
-   [d3.timeThursday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday), [d3.utcThursday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday) - the week interval, starting on Thursday.
-   [d3.timeThursdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday), [d3.utcThursdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeThursday) - aliases for thursday.range.
-   [d3.timeFriday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday), [d3.utcFriday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday) - the week interval, starting on Friday.
-   [d3.timeFridays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday), [d3.utcFridays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeFriday) - aliases for friday.range.
-   [d3.timeSaturday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday), [d3.utcSaturday](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday) - the week interval, starting on Saturday.
-   [d3.timeSaturdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday), [d3.utcSaturdays](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeSaturday) - aliases for saturday.range.
-   [d3.timeMonth](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth), [d3.utcMonth](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth) - the month interval.
-   [d3.timeMonths](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth), [d3.utcMonths](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeMonth) - aliases for month.range.
-   [d3.timeYear](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear), [d3.utcYear](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear) - the year interval.
-   [d3.timeYears](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear), [d3.utcYears](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeYear) - aliases for year.range.
-   [d3.timeTicks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTicks), [d3.utcTicks](https://github.com/d3/d3-time/blob/v3.0.0/README.md#utcTicks) -
-   [d3.timeTickInterval](https://github.com/d3/d3-time/blob/v3.0.0/README.md#timeTickInterval), [d3.utcTickInterval](https://github.com/d3/d3-time/blob/v3.0.0/README.md#utcTickInterval) -