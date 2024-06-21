---
title: file2radius
layout: page
shortdesc: Daemon to generate radius records on the network by following CDR log files.
---
Daemon to generate radius records on the network by following CDR log files.<!--more-->

# Overview

This is a daemonized perl script that will tail a CDR accounting log file and generate radius accounting records on the wire from it.  I wrote this for use with the Broadsoft soft switch but with a little work it could be (and probably will be) adapted for use with other sources of CDR data.  It supports sending to a primary and backup radius server and automatically follows the new files as they get rotated out.   The script assumes you are doing duplicate checking on the radius server backend.   In my case I’m using [Radiator from OSC Software][1] (which I highly recommend) with custom hook code to normalize, filter and load into a [Postgresql][2] database.  Radiator is the swiss army knife of radius servers.

 [1]: http://www.open.com.au/radiator/
 [2]: http://www.postgresql.org/

## Features

*   Written in perl using standard modules from CPAN
*   Supports primary and backup radius servers with auto-fallback to the primary.
*   Auto mapping of CDR fields to radius attribs for Broadsoft
*   Logs to local syslog
*   Supports bulk loading of CDR files
*   Supports ignoring Terminating calls
*   Simple and lightweight
*   Easily extended or modified

## Download

*   [file2radius-1.1-2012-02-14.tar][4]

 [4]: /downloads/file2radius-1.1-2012-02-14.tar.gz

