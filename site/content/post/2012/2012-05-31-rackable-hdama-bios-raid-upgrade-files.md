---
title: Rackable HDAMA Bios Raid Upgrade Files
date: 2012-05-31
categories:
  - Computing and Tech
tags:
  - arima
  - bios
  - bootable
  - dos
  - firmware
  - flash
  - freedos
  - hdama
  - phoenix
  - rackable
  - raid
  - update
  - usb
  - utility
---

I picked up an inexpensive server last year from [unixsurplus.com][1] which I now want to re purpose as a [FreeNas][2] file server.  This is all fine and good.. but the bios and embedded sata raid drivers were out of date and didn’t support the 2TB drives I wanted to use.  I spent many hours trying to track down the right bios files and Phoenix flash utility to do this update and was finally able to get it done.  The original download sites for most of these are long gone.. so it was a real chore to find the right stuff.  So for those who have this board here are all the required files in one place.<!--more-->

 [1]: http://unixsurplus.com/
 [2]: http://www.freenas.org/

I’ve got several flash update utilities.. and ALL the firmware for the Arima motherboard models HDAMA rev G and rev I as well as HDAMB.  I’ve also included a windows utility for making a freedos bootable USB key which even works through vmware (fusion in my case).  More info on this board can also be found in[ this forum post][3].  My board was using phoenix bios and that’s the only flash utility I could get to do the job properly.  Enjoy!

 [3]: http://forums.mydigitallife.info/threads/20603-Arima-HDAMA-and-HDAMB-Motherboard-BIOS-Fixes

[Download HDAMA.zip][4] (42M)

 [4]: /downloads/HDAMA.zip
