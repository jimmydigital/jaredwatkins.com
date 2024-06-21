---
title: 'What I do: Dynamic Daily Table Partitions With Postgres'
date: 2012-01-19
categories:
  - Computing and Tech
  - Geeky Stuff
  - My Code
  - Personal
tags:
  - dynamic
  - oracle
  - partitions
  - perl
  - postgres
  - postgresql
  - resume
  - rolling
  - sliding
  - table
  - window
---

As part of a new and fairly large project I have a need to partition a few postgres tables and have a rolling daily window.  That is.. I want to organize data by a timestamp storing each day in its own partition and maintain 90 days of historical data.  Doing this is possible in Postgresql but it’s not pretty or very clean to set it up.  To simplify the process I wrote this perl script that (when run daily) will pre-create a certain number of empty partitions into the future and remove the oldest partitions from your window.<!--more-->

The script is generalized so as to be easy to modify and there isn’t much here that’s specific to postgres.. so it could easily be adapted for use with other systems like Oracle. You will need to put in the DDL for the child tables you will create but otherwise it’s pretty straight forward.  Please let me know if you find this useful as I couldn’t find anything else out there like it.

Visit the **[project page][2]** for details and the download.

 [2]: /projects/pgdynamicpartitions/ "pgDynamicPartitions"

Update: Several important updates to the code and my examples since I first published this.  Be sure to grab the latest version which is starting to behave reasonably now.
