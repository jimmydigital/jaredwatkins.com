---
title: pgDynamicPartitions
layout: page
shortdesc: Cron script to maintain rolling windows of daily table partitions with PostgreSQL.
---
Cron script to maintain rolling windows of daily table partitions with PostgreSQL.<!--more-->

## Download

*   (version 1.3.20120206) [pgDynamicPartitions.pl.1.3.20120206][6]

 [6]: /downloads/pgDynamicPartitions.pl_.1.3.20120206.gz

# Overview

This perl script will allow you to maintain a rolling window of daily table partitions under Postgresql.  That is.. when called daily via cron it will create x empty partitions into the future and keep only n partitions into the past.. say 30 days… and drop any that are older.

To use it you will need to define all the steps necessary to properly create each child table.  In my example the table is named ‘intake’ and after it’s created it has a constraint and a few indexes created on it.  Under Postgres partitions are actually treated as separate tables that need to have their own indexes but inherit the column structure from the parent table. An insert trigger is defined which calls a dynamic function to insert records into the correct table partition.  In my example case that’s keyed off a timestamp column named ‘callstart’.

The way I organize the insert function.. the most efficient use will be to call this script shortly after midnight which will update the stored function so that the current day is always the first check performed by the insert sorting routine.

## Syntax

    ./pgDynamicPartitions.pl    [-h dbhost] [-d database] [-t table] [-p past] [-f future]



        -h [host]        DB Host to operate on

        -d [database]    Database to connect to

        -t [table]       Parent table name to partition

        -p [days]        How many daily partitions to keep into the past

                         Ones older than this will be dropped.

        -f [days]        How many empty daily partitions to be created into the future.

        -n               Don't make changes just show what would be done.

        -r [days]        Used for creating missing historical partition tables. Format is

                         days into the past from today.

