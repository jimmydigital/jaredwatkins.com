---
title: 'What I Do: Broadsoft CDR Files to Radius Accounting Records'
date: 2012-02-02
categories:
  - Computing and Tech
  - My Code
tags:
  - broadsoft
  - cdr
  - perl
  - postgresql
  - radius
  - resume
  - soft switch.radiator
---

As part of a larger project I needed to generate real time [radius][2] records from the CDR accounting files of several cluster pairs of [Broadsoft][3] [application servers][4]. So I wrote a perl script to do just that. It maps the CDR fields to radius attribs and encodes the accounting packet using the [Net::Radius::Packet][5] CPAN module.  In my case I’m using the [Radiator radius server][6]  from [OSC Software][7] on the other end with lots of custom ‘hook code’ to clean up and store the call data coming off our network into a [Postgresql][8] database.  This is my first time doing any development with radius.. but I’ve been running this script on several servers for a few weeks now and it appears to be quite stable.

 [2]: http://en.wikipedia.org/wiki/RADIUS
 [3]: http://www.broadsoft.com/
 [4]: http://www.broadsoft.com/products/broadworks/platform/
 [5]: http://search.cpan.org/~luismunoz/Net-Radius-2.103/Radius/Packet.pm
 [6]: http://www.open.com.au/radiator/
 [7]: http://www.open.com.au/
 [8]: http://www.postgresql.org/

*   Get it on the [Project Page][9]

 [9]: /projects/file2radius/
