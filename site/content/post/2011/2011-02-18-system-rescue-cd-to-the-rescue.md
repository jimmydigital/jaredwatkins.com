---
title: System Rescue CD to the.. rescue!
date: 2011-02-18
categories:
  - Computing and Tech
  - Geeky Stuff
  - Personal
tags:
  - broken
  - equinix
  - grub
  - linux
  - mbr
  - raid
  - rescue cd
  - resume
  - server
---

![](http://farm6.static.flickr.com/5211/5421694137_c92bd1b195.jpg =160x)

Here’s the scenario..  It’s 1 am and I have to shut down a critical linux server to relocate it in a rack to make room for new equipment. It should have been a 5 minute job.. but on powering up the server it refused to boot past printing the word ‘[Grub][2]‘ on the screen.  This isn’t good..  this server is needed by a couple hundred thousand customers and rebuilding it wasn’t planned or scheduled.  On closer examination 3 of the 16 hard drive power lights are not on. It’s extremely unlikely that 3 drives would die like that on a server that isn’t even two years old.  Unfortunately I didn’t have a copy of the the [System Rescue CD][3] so the fix attempt would have to wait until morning.

 [2]: http://en.wikipedia.org/wiki/GNU_GRUB
 [3]: http://www.sysresccd.org

I had the [CoLo][4] staff burn me a copy which I used to boot the damaged server the next morning.  It booted into a live linux environment and correctly detected all the server hardware.. including the raid controller.  I was able to check the status of the 3 raid arrays and found them to be all in working order.. the 3 dark drive lights were unrelated.  I was then able to [chroot][5] into the broken system and [reinstall grub][6] onto the primary disk. The server then booted normally and all was well. I still don’t know how or when the [MBR][7] got corrupted.. but thanks to the utility of the [RescueCD][3] this was an easy fix.

 [4]: http://www.equinix.com/
 [5]: http://en.wikipedia.org/wiki/Chroot
 [6]: http://www.sysresccd.org/Sysresccd-Partitioning-EN-Repairing-a-damaged-Grub
 [7]: http://en.wikipedia.org/wiki/Master_boot_record
