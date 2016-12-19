---
date: 2013-02-25
title: "Blog Relaunch - All the Cool Kids Are Going Static"
categories:
  - Personal
  - Projects
  - My Code
tags:
  - octopress
  - blog
  - aws
  - cloudfront
  - amazon
  - ruby
  - jekyll
  - github
---

I've run my own hosted server for many years now. Originally it was just to have my own mail server
but later I decided to start the blog using [Wordpress][7].  It's great to have the control and
flexibility to do whatever you want with a server.. but there are definitely some downsides
as well.  Wordpress is great.. but there are constant security issues to worry about and
people attacking your server trying to hack it with automated tools. Customizing it has
also never exactly been easy.. and it's a huge code base that I don't really understand.

So this new version of the blog is far enough along that it was time to turn it lose.<!--more-->

It's built on a framework called [Octopress][5] / [Jekyll][6] which is written in [Ruby][8]. I don't know ruby
but it's similar to perl and this framework is very lightweight and fairly easy to understand.. which is nice.
The ruby code lives on my laptop at home.. far away from the barbarian hordes. It generates
the complete blog website as static html files that are then pushed out to remote web servers.
The web servers don't need to run any sort of dynamic code and so can be secured more easily
and the pages load much more quickly.

This change alone would have been enough to justify the migration.. but since I'm now working for Amazon Web Services
I decided to kick it up a notch.  So now I'm hosting this blog using [CloudFront][2] and [S3][1] storage.
The workflow goes like this... When I write a new posting the entire site is regenerated and pushed to a
test system I use to preview the results. Once I'm happy the files get pushed from my laptop
to [S3][1].. then CloudFront kicks in and distributes the
site from there to a fleet of Amazon servers all over the world. No matter where you are... you are
routed to the nearest server to you on the internet. That makes it fast and resilient and super cheap as it turns out
since you pay only for what you use... and a personal blog isn't ever going to use that much.
I expect this setup will cost about 20% of what I've been paying for the private server and it's 1000%
better way of doing things. If I had something really interesting to post and got linked from
a site like the drudgereport or slashdot.. my little blog could handle the crushing levels of traffic that would
flatten any single web server. They also deal with issues of redundancy and keeping it online and availiable.

I'm using a few plugins for [Octopress][5].. most of which are about a page or two of Ruby code
with a little [Liquid][10], [Markdown][9], and HTML mixed in. I also wrote some perl to automatically build image
thumbnails and watermark some of my full size images. The image gallery pages are semi-automated and
that's the last bit that needs more work. I plan to set those up with [Fancybox][3] to make
the gallery pages a little easier to use. I plan to release the perl scripts along with the rest
of the source for this blog on [github][4] when it's a little further along.

[1]: http://aws.amazon.com/cloudfront/
[2]: http://aws.amazon.com/s3/
[3]: http://http://fancybox.net/
[4]: https://github.com/
[5]: http://octopress.org/
[6]: http://jekyllrb.com/
[7]: http://wordpress.org/
[8]: http://www.ruby-lang.org/en/
[9]: http://daringfireball.net/projects/markdown/syntax
[10]: http://wiki.shopify.com/UsingLiquid
