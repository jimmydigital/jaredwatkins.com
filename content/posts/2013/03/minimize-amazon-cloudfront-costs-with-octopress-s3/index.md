---
date: 2013-03-05
title: "Minimize Amazon Cloudfront Costs With Octopress and S3"
comments: true
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
  - frugal
  - cheapbastard
  - S3
  - EC2
  - t1.micro
  - m1.small
  - server
  - virt
  - s3cmd
---
I learned an important tip that I thought I should share with others who are considering Octopress
with publishing to S3/Cloudfront.  If the S3 deployment line in your Rakefile includes the s3cmd
option for "--cf-invalidate" you should be aware that this will drive up your costs quite a bit.
(3 guesses how I know this) I had about a years worth of expected CF costs in my first month because
I didn't understand what that was doing.<!--more-->

This isn't as bad as it sounds.. as my expected yearly
bill should be less than $30 for S3 and CF assuming I don't get super famous in the next year.

When setting up your CloudFront deployment you tell it what you want the ttl to be for caching
your content.  12 or 24 hours is typical.. so that means if you publish an update it could take
up to that long to be visible everywhere.  Using the "--cf-invalidate" option tells amazon
that you want to expire all your pushed content early and force their system to globally
redeploy it ahead of the expected schedule. They charge for that... for every URL you expire you
get hit with extra costs.  For me.. that meant while I was in the dev phase and doing frequent
pushes of some 800 or so files every time... I racked up a lot of extra charges.  So I've taken
that out of my rakefile.

Of course all the Rakefile does is run the s3cmd command to sync all your content under /public.
If you really need to expire a file or two early you can still do it... just run the command by hand.

Another cost saving tip for working with EC2 servers.  If you need a very small server that's
always up.. don't buy a spot instance... buy a t1.micro reserved instance for 'heavy usage'.
You can use their pricing tool to see how cheap this is.. much cheaper than an m1.small which
is their default ec2 server type. Current numbers put it at about $45/yr verses about $250/yr.

