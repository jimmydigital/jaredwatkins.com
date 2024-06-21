---
title: OSX Mail App Using Tons of Memory and CPU?
date: 2012-01-07
categories:
  - Computing and Tech
  - Geeky Stuff
tags:
  - cpu
  - Entourage
  - fix
  - high cpu
  - high memory
  - isync
  - mail
  - memory
  - osx
  - resources
  - snow leopard
  - solution
  - troubleshoot
---

![](http://farm1.static.flickr.com/30/44074632_687cc920b9.jpg =320x)

I’ve been using a mac for a while now and I recently decided to dump Entourage and go to using the native Mail.app.  I noticed a problem though.. within minutes of starting up it would consume several hundred megs of ram and have frequent CPU spikes of 80 to 100%.  If Mail was left open, memory usage would climb above 2 gig with continued CPU spikes.  After much digging I finally found the problem and fixed it.<!--more-->

I’d been using iSync back before I got an iPhone..  and had never thought to disable it.  It looks like what was happening is that mail and other apps (ical, address book) had been building a huge database of stuff that needed to be synced to my old phone.  Once I went in and reset the sync history and disabled iSync.. everything calmed down and now a running instance of Mail.app with 3 imap accounts and an Exchange account is using about 60 MB of ram.. and it’s not steadily climbing as it had been before.  This may have also been the source of the problems I’d been having with Entourage.

