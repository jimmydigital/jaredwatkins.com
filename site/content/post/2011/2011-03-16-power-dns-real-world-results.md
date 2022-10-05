---
title: 'What I do: Power DNS Real World Results'
date: 2011-03-16
categories:
  - Computing and Tech
  - Geeky Stuff
  - My Code
  - Personal
  - Projects
tags:
  - debian
  - dns
  - linux
  - mysql
  - nagios
  - open source
  - pdns
  - performance
  - php
  - power dns
  - replication
  - resume
  - vmware
---

We have had a [Power DNS][1] recursing cacher deployed at one of our busiest sites for a few months now and I thought others might benefit from some real world performance info.  This is running on some older hardware.. dual Xenon 2.8Ghz system with 4G of ram and the only job it’s doing is running this recursor. These three graphs tell the tale.  The first shows that the system is handling peaks of about 3800 queries per second and that about 99% of those are being answered in a fraction of a millisecond.  The second shows that cache hits are averaging about 70-75% and the third shows that it’s doing this work while using at most one quarter of the CPU.  Add to those impressive performance levels that I’ve had zero issues since putting it in production six months ago.

 [1]: http://www.powerdns.com
<!--more-->

[![](/pics/inline_pdns1.png)](/pics/pdns1.png)
[![](/pics/inline_pdns2.png)](/pics/pdns2.png)
[![](/pics/inline_pdns3.png)](/pics/pdns3.png)


We plan to roll out a bunch of these cachers and and the [PDNS][1] authoritative servers as well with a replicated [MySQL][5] backend for the storage of records. When complete the new [DNS][6] infrastructure will require about 12 new [virtual servers][7] running in 5 different data centers to handle internal and external needs. These will be tied into a custom ip inventory database I’ve been working on and will update in real time with changes made there.  This is part of an ongoing larger effort to improve and automate the management of our global [VoIP][8] network and it’s all being done with [open source software and operating systems][9] which are my specialty.

 [5]: http://www.mysql.com/
 [6]: http://en.wikipedia.org/wiki/Domain_Name_System
 [7]: http://www.vmware.com/
 [8]: http://www.wikinvest.com/concept/Voip
 [9]: http://www.debian.org/
