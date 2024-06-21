---
title: 'Fraud System: Update 2'
date: 2012-06-02
categories:
  - Computing and Tech
  - My Code
tags:
  - broadsoft
  - carrier
  - fms
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

Progress has slowed a bit on the fraud management system… other priorities have come up over the last month or so but here’s a new walk though.  The backend hasn’t changed much.  What has changed is the hardware requirements.  When I started this project I had no idea how much processing power or space or IO was going to be required so I built the system in such a way that it could be easily scaled at several points.  As it turns out.. for this size of a network (about 250k customers) that was unnecessary.<!--more-->

It’s currently running quite happily on 2 VMs on the same IBM blade (that is also running a half dozen other things) and using about 2.5G of ram with an 18G database on a mirrored pair of SAS  drives.   The only observed bottleneck at this point is the radius server since it is single threaded.  I’m doing a lot of processing to normalize and enrich every CDR that comes in at that level so this is not unexpected.  In using the [file2radius][1] daemon (which you can get here from my projects section) I support a primary and secondary radius server so this allows me to split that workload up by each cluster pair of broadsoft servers. The use of automated daily table partitions in postgres has also made management of the data much easier.  You can also get the script that does that here in my projects section under [pgDynamicPartitions][2].

 [1]: /projects/file2radius/ "file2radius"
 [2]: /projects/pgdynamicpartitions/ "pgDynamicPartitions"

This shows a progression of the interface during a normal day when nothing unusual was going on.  It’s not obvious.. but many elements in the data are clickable to pull up different views centered around certain elements like a specific caller or specific country.. or activity between a specific pair of countries. The time scale can also be adjusted from the default of 30 minutes out to all data we have in the database which currently goes back 45 days.

This system does a sort of dynamic baselining of both ends of every call to determine a score value that represents how far from normal the current behavior is for that caller.

 

[![](/pics/inline_Big-Score-2012-06-01.png 'Overview' '10k Foot Overview')](/pics/Big-Score-2012-06-01.png)

10k Foot Overview


[![](/pics/inline_Current-Detail-2012-06-01.png)](/pics/Current-Detail-2012-06-01.png)


Detailed overview of current highest scoring callers or groups.

[![](/pics/inline_Caller-Detail-2012-06-01.png)](/pics/Caller-Detail-2012-06-01.png)


Call detail screen showing past 30 minutes of activity.

[![](/pics/inline_Country-Detail-2012-06-01.png)](/pics/Country-Detail-2012-06-01.png)


Country specific detail screen of recent activity. Graph shows 10 day trends

[![](/pics/inline_Between-Countries-2012-06-01.png)](/pics/Between-Countries-2012-06-01.png)


Inter-Country Graphical View

[![](/pics/inline_Threshold-Violations-2012-05-29.png)](/pics/Threshold-Violations-2012-05-29.png)


Record of Threshold Violations - This recorded some actual abuse that was going on while the system is still under development.

[![](/pics/inline_User-Management-2012-06-01.png)](/pics/User-Management-2012-06-01.png)


User / Group / Tag Management

[![](/pics/inline_List-Management-2012-06-01.png)](/pics/List-Management-2012-06-01.png)


Rate deck management screen

[![](/pics/inline_Threshold-Management-2012-06-01.png)](/pics/Threshold-Management-2012-06-01.png)


Threshold Management Screen

