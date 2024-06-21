---
title: 'What I Do: Fraud Detection System Initial Overview'
date: 2012-03-02
categories:
  - Geeky Stuff
  - My Code
  - Personal
  - Projects
tags:
  - broadsoft
  - carrier
  - fraud
  - memcached
  - perl
  - postgres
  - radiator
  - radius
  - resume
  - telecom
  - toll fraud
  - voip
---

![](/pics/inline_capn-crunch-bosun-whistle.jpg)

I’ve been working on a big new project since just before the new year and it’s starting to take shape and generate useful results.   I can’t give away too many details on how exactly it works but I wanted to share this with some of you who are also working in telecom.  I was asked to develop a real-time system to identify toll fraud that would work for our entire voip carrier network that currently originates calls from 19 different countries for both residential, SMB, and wireless.  For those who don’t know.. I spent a year working for another telecom software company helping to run and debug a call mediation and rating platform for a tier2 carrier.  This experience was useful in that I was able to quickly develop a scalable, distributed processing framework while avoiding the cumbersome overhead I’ve observed in other systems.  Continue after the jump for more details…<!--more-->

For starters.. the whole platform is written in perl using a forking model with a Postgres database backend.  So far all the development has been with CDRs coming from Broadsoft but records from ACME Packet are next to be incorporated.  The CDR files are tailed by [another program I’ve already released here][2] and it generates radius records on the wire back to a pair of redundant Radiator radius servers.  This is an excellent [commercial radius server][3] that is also written in perl and is extensible through the use of various code hooks.  In those hooks I do about dozen different things to the incoming records.. enriching them.. normalizing.. filtering.. and finally sorting and storing as either ‘interesting’ call traffic or not. For performance.. the only time radiator touches the database is to store the records that are going to be kept.

 [2]: /projects/file2radius/ "file2radius"
 [3]: http://www.open.com.au/radiator/

Radiator is an independent process..  but it is controlled through a daemonized network listener that runs on every node of this system.  The listener provides both an interactive network command interface as well as a remote API of sorts.  Nodes can use this telnet like protocol to talk to other nodes and exchange more complex data using [Memcached][4] when needed.  Code changes can be verified and deployed to the entire cluster with a single command through this interface and all remote processes can be queried for status and started and stopped gracefully with minimal interruption.

 [4]: http://memcached.org/

Each node can run one or more collector processes that are tied back to a specific source of call data… like the AS cluster on the west coast for example… so that calls from the same set of customers are always handled within the same process.  Interesting calls are analyzed seconds after they come in and are scored through a somewhat complex process (secret sauce) that uses dynamic baselining for both ends of the call. When this scored traffic is further analyzed… fraudulent activity becomes easy to spot.

That’s the theory anyway.  There is still plenty to do before this is a complete system that’s ready to play well with others.. but the basics are in place and have been scoring calls for several weeks now with only a few minor tweaks as I find corner cases in the traffic patterns.  I’ve also got the start of the web interface.. not nearly complete.. but good enough to be useful.

[Continued in Part Two][7]

 [5]: http://www.macromedia.com/go/getflashplayer
 [6]: http://www.mozilla.com/firefox/
 [7]: /2012/04/what-i-do-fraud-management-system--update1/ "What I do – Fraud Management System -Update1"

