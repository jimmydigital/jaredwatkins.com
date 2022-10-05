---
title: 'What I do: Mysql Reporting Date Range Cheat Sheet'
date: 2010-12-17
categories:
  - Computing and Tech
  - Geeky Stuff
  - My Code
  - Personal
tags:
  - software
  - mysql
  - reporting
  - resume
  - sql
  - time
---

If you have to do any sort of reporting using mysql or other databases you will probably need to use relative date ranges that don’t depend on what day the report is being run. That is if you need a report for ‘last month’ that runs from the first to last day of the previous month.. or previous 3 months etc but not include any days in the current month.   Here is a small collection of queries...<!--more-->

that look back in time and help identify these boundary dates.

``` sql
-- Last day of previous month
SELECT date(now() - interval dayofmonth(now()) day);
-- First day of previous x month
CREATE FUNCTION firstday_x_monthsback (m INT(10))
returns datetime no sql
RETURN concat(date_format(LAST_DAY(now() - interval m month),'%Y-%m-'),'01 00:00:00');
-- Last day of previous x month
CREATE FUNCTION lastday_x_monthsback (m INT(10))
RETURNS DATETIME NO SQL
RETURN concat(last_day(concat(date_format(LAST_DAY(now() - interval m month),'%Y-%m-'),'01 00:00:00')),' 23:59:59')
-- Seconds in previous month
SELECT day(
last_day(
concat(
date_format(
LAST_DAY(now() - interval 1 month),'%Y-%m-'), '01 00:00:00'))) * 86400;
-- Seconds in previous x months
CREATE FUNCTION seconds_in_x_monthsback (s INT(3))
returns bigint no sql
RETURN (datediff(lastday_x_monthsback(1),firstday_x_monthsback(s)) + 1) * 86400;
```
