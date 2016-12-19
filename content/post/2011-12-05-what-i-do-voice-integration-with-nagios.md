---
title: 'What I do: Voice Integration With Nagios and Asterisk'
date: 2011-12-05
categories:
  - Computing and Tech
  - Geeky Stuff
  - My Code
  - Projects
tags:
  - asterisk
  - broadsoft
  - festival
  - linux
  - nagios
  - perl
  - resume
  - tts
  - voip
---

![](/pics/inline_asterisk_logo.png)

I was called on to provide a method of alerting from within [nagios][2] that was more active and direct than the usual use of email or SMS messages.  So I came up with a simple way to have a nagios notification place a phone call to our off hours tier3 support line to report certain very rare but serious problems.<!--more-->

This was actually a two part solution.  We were interested in looking for certain things coming out of the [Broadsoft][3] audit log that were important enough to wake someone up in the middle of the night.  So I wrote a daemonized script that tails the Broadsoft audit log and interprets it looking for these config changes and then reports this to a special [RT3][4] queue.  It also notifies nagios (a push notification to a passive service check) over a socket connection. A listener script on the nagios box (using [net::server][5]) validates the syntax of the alert and lets nagios know.. which in turn triggers (and manages the scheduling) of the outgoing phone call(s) through [asterisk][6].

 [2]: http://nagios.org/ "Nagios NMS"
 [3]: http://www.broadsoft.com/
 [4]: http://bestpractical.com/rt/
 [5]: http://search.cpan.org/~rhandom/Net-Server-0.99/lib/Net/Server.pod "Net::Server Perl Module"
 [6]: http://www.asterisk.org/

I used the [google TTS][7] engine to record certain fixed statements that would be common across calls.. converting the audio to the proper format for asterisk (SLN16) with sox.  For the specific alert text I’m using a simplified version of [festival][8] from the command line called ‘flite’.   The asterisk part is done entirely in a [perl agi][9] script and allows the called person to repeat the alert or acknowledge it within nagios. If they don’t answer or don’t ack the alert nagios will initiate another call in a few minutes.. and I’m able to use service escalations to notify different people if it goes too long without a response.

 [7]: http://techcrunch.com/2009/12/14/the-unofficial-google-text-to-speech-api/ "Google TTS"
 [8]: http://www.cstr.ed.ac.uk/projects/festival/ "Festival Speech Engine"
 [9]: http://www.voip-info.org/wiki/view/Asterisk+AGI "Asterisk AGI"

This project has more moving pieces than I usually like to use but it was interesting in just how easy it was to get working.  It’s gotten me thinking about doing a more full featured voice fronted to nagios that I could release.

[Download](/downloads/nagiosVoiceNotify.tgz) the scripts here.

