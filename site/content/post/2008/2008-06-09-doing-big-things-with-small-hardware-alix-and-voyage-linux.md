---
title: Doing big things with small hardware, Alix and Voyage Linux
date: 2008-06-09
categories:
  - Computing and Tech
  - Projects
tags:
  - linux
  - alix
  - asterisk
  - voip
---

I’ve been interested in small embedded hardware systems for a while. Until recently I was using [OpenWRT][1] on a reflashed [Linksys][2] box for my router. That worked.. but had limitations and since it isn’t an intel based system that means you have to cross compile anything you can’t find a package for. So recently I’ve been playing around with the new [Alix boards from PC Engines][3].
<!--more-->
I ordered two model [2c3 boards][4] which have 3 10/100 network ports, serial, USB, CF, and a mini-pci slot. In the case.. the boards are slightly bigger than a double thick CD case and only pull about 5w which is fantastic for any sort of solar/battery system (ie for outdoor wifi mesh network nodes). These boards are only about $130 and are ideal for all sorts of network related uses. Noticably absent are: vga port, pci or other expansion slots, power headers for disk drives.

So if these are the ideal hardware platform for embedded network devices what about the other half.. the software? I have worked with a few different linux distros that are suitable for use in embedded systems. One I like is called Devil linux.. which is great if you can run from a bootable CD with flash storage for configs. I like how that distro is put together but it was not the best choice here… I needed something smaller and easier to add software to. After trying out a few different ones I found Voyage Linux. This is a small (25meg) debian based system that takes advantage of the apt package manager. This means it’s very easy to add software to the system and the base install is still small and supports most of the advanced network functions easily.

 [1]: http://openwrt.org/ "http://openwrt.org/"
 [2]: http://en.wikipedia.org/wiki/WRT54G "http://en.wikipedia.org/wiki/WRT54G"
 [3]: http://www.pcengines.ch/alix.htm "http://www.pcengines.ch/alix.htm"
 [4]: http://www.pcengines.ch/alix2c3.htm "http://www.pcengines.ch/alix2c3.htm"

The first prject I started with these boards is to build an Asterisk PBX for a Green Energy Company I’m helping out. Running on a 1G CF card I have about 650 meg free after getting all the needed software installed to support Asterisk, lightttp web server and a few other packages. If more space is needed.. say for voice mail or whatever.. I can always plug in a usb flash drive for expansion. The second board was just put into service as my new home router replacing the OpenWRT linksys box. This has worked out very well and I’ve noticed that big downloads are actually running faster. I believe this has to do with the faster bus speeds of this board. I’ve also been able to create a persistant cisco VPN connection from the router to my company which makes it much easier to interact with systems at HQ. This is in addition to the OpenVPN connections that already exist into my hosted server.. and the one I use from the laptop to connect back home when I’m on the road.

I see the combination of the Alix boards with Voyage linux to be a veritable swiss army knife of embedded linux foo.
