---
title: The Devil is in the Details
date: 2005-05-17
categories:
  - Computing and Tech
tags:
  - squid
  - linux
  - proxy
---

This past weekend I was down visiting our [Atlanta office][1] to install the first (of possibly many) linux based [squid web proxy][2] caching boxes. This in its self is nothing special.. what makes this interesting is the hardware/software combo I used to do it. This is a pilot project in Atlanta.. they are our biggest remote site and it’s not unusual for them to saturate their WAN circuit back to [central][3]. The goals were to have a local web cache to reduce internet traffic.. and to control / [rate limit p2p software][4] (that they shouldn’t have anyway!) To do this.. I used an older 900Mhz dell workstation that had been retired from desktop use… to get it ready for its new life I got a new 30G hard drive.. a 256 meg flash ram chip and two new 10/100 network cards. Total cost.. less than $100 from [Directron][5]. For the OS I chose a linux distribution called Devil Linux. The system boots and runs right from the CDROM drive.. with all the config (and some other programs) stored on the flash ram. The hard drive is only used for web cache data and associated logs. Since this is a nicely fleshed out linux box.. many other tasks are possible with this same simple setup. There are many applications that are already part of the distribution… and if it is lacking something you want.. they make a build environment available for you to customize the CD. In this case.. the site already had an older cisco router.. so to accomplish my task I made this into a bridge.. with a few iptables and ebtables rules to redirect the web traffic transparently through the cache… thus requiring no changes to client software.. you just drop this box in front of the existing router and it starts working.. we are looking at a similar approach but using a [cluster][6] of squid boxes for our central site to cache the internet behind our two [T3 connections][7]. You can read about the technique of [transparent redirection][8] in this [freshmeat][9] article.

 [1]: http://atlanta.bizjournals.com/atlanta/
 [2]: http://www.squid-cache.org/
 [3]: http://www.acbj.com/
 [4]: http://support.imagestream.com/Limiting_P2P_Traffic.html
 [5]: http://www.directron.com/
 [6]: http://www.linuxvirtualserver.org/
 [7]: http://support.summersault.com/bandwidth_chart.html
 [8]: http://freshmeat.net/articles/view/1433/
 [9]: http://freshmeat.net/

I’ve also used this dist to build a lab firewall that does bi directional NAT to replicate our internal network in a self contained environment. In addition to devil linux I am using a program called [FWBuilder][10] to manage the firewall rules. The two in combination make a very easy to use setup for managing a fleet of firewalls / routers.

 [10]: http://www.fwbuilder.org/
