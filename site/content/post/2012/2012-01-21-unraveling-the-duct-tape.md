---
title: Unraveling the Duct Tape
date: 2012-01-21
categories:
  - Computing and Tech
  - Security/Insecurity Insanity
  - Skepticism
tags:
  - arduino
  - duct tape
  - ethical hacking
  - Joshua Wright
  - SANS
  - SCADA
  - security
  - smart grid
---

![](http://farm8.static.flickr.com/7016/6486021333_9c6e3d86bd.jpg =320x)

I’ve written before about [the world being held together by duct tape][2]… and it seems there are more people lately who have decided to rip off the covers and go looking for some duct tape.  The latest headline comes from the world of SCADA systems.<!--more-->

[Researchers Lay Bare Woeful SCADA Security][3].  SCADA systems are small embedded computers that help guide various kinds of industrial processes..manufacturing, power plants and water systems. Basically anything where you have sensors, motors, pumps etc that have to be monitored and controlled.  [Iran learned all about lax SCADA security][4] over the last couple years and now everyone else is finding out about it too.  The dirty little secret is that most of these systems haven’t fundamentally changed in the last 20 years… despite huge improvements in the level of sophistication of what’s out there now even for hobbyists.  Things like the [Arduino platform][5] costs an order of magnitude less than commercial systems and can perform many of the same jobs.  Actually that’s not true though.. SCADA systems have changed in one very important way.. people started plugging them into a network.  Once you do that.. you are opening yourself up for a world of hurt if those systems were not designed to operate in a hostile environment.  As the researches in the linked story found out.. some of them can’t even be probed without crashing.. never mind standing up to direct attacks.

 [2]: /2010/09/the-world-is-held-together-by-duct-tape/ "The world is held together by duct tape"
 [3]: https://threatpost.com/en_us/blogs/looking-firesheep-moment-researchers-lay-bare-woeful-scada-security-012012
 [4]: http://en.wikipedia.org/wiki/Stuxnet
 [5]: http://www.makershed.com/Arduinos_Accessories_s/43.htm

I was fortunate enough to take the SANS security course on [Wireless Ethical Hacking, Penetration Testing, and Defenses][6] a few years ago. While I totally recommend the SANS courses.. they are really top notch in the world of tech training.. one of the things I learned as a result of that course is that very few people/organizations take security seriously.   Security should be thought of as existing on a continuum along with ease of use.  That is.. something could be totally secure and totally unusable or very easy to use and totally insecure.  SCADA systems have been operating at that end of the scale for decades now and I doubt very seriously that’s going to change anytime soon.  If the customers who buy these systems cared at all about security they would demand the systems actually be more secure.  That doesn’t happen though.. and I blame human nature.

 [6]: https://www.sans.org/security-training/wireless-ethical-hacking-penetration-testing-defenses-3-mid

Incidentally… you may think your world isn’t personally touched by these systems but you would be wrong.  In fact.. in some areas you may already have a [vulnerable SCADA component ][7]bolted right on your own home.  Heard of the SmartGrid?  The very same researcher who taught my wireless hacking class has [found some serious issues ][8]with the power meters used in smart grid systems.  Imagine a worm that could infect a network of power company smart meters.. giving control over the power they regulate to some 3rd party.  At that point it would be trivial to crash the regional electrical grid on demand.. and we know from what happened accidentally in the north east a few years ago that can take days to recover from. Sleep tight!

 [7]: http://gigaom.com/cleantech/smart-meter-worm-could-spread-like-a-virus/
 [8]: http://www.msnbc.msn.com/id/36055667/ns/technology_and_science-security/t/smart-meters-have-security-holes/#.TxuBaSOZNCI
