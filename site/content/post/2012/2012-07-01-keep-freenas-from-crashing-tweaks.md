---
title: Keep FreeNAS From Crashing Tweaks
date: 2012-07-01
categories:
  - Computing and Tech
  - Geeky Stuff
tags:
  - bsd
  - crash
  - freebsd
  - freenas
  - freeze
  - io
  - loader.conf
---

I found these settings on another site.. reposting here for my future reference and to double the possibility of someone else not having to spend hours trying to figure this out.  My install of FreeNAS kept hanging under even moderate write loads… rendering it unusable until I applied these memory tweaks.  I don’t know nearly as much about BSD internals as I do linux.  You can apply these through the web GUI under System->Tunables.  When you do they get added to the file /boot/loader.conf.local but should also be backed up with the rest of your config.

Of course this assumes you have adequate memory… I used these values on a system with 6G total ram.

```
vm.kmem_size="1536M"
vm.kmem_size_max="2048M"
vfs.zfs.arc_min="256M"
vfs.zfs.arc_max="1024M"
vfs.zfs.txg.timeout="30"
vfs.zfs.vdev.max_pending="35"
vfs.zfs.vdev.min_pending="4"
vfs.zfs.txg.write_limit_override="1073741824"
```
