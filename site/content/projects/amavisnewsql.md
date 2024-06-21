---
title: AmavisNewSQL Plugin
layout: page
shortdesc: Squirrelmail plugin interfaces to amavis-new-sql and provides a quarantine system
---
<script src="https://code.jquery.com/jquery-3.1.1.min.js" charset="utf-8"></script>
<script type="text/javascript" src="/js/jquery.githubRepoWidget.min.js"></script>
Squirrelmail plugin interfaces to amavis-new-sql and provides a quarantine system<!--more-->

> This plugin for [Squirrel Mail][1] lets users change a pre-defined set of SpamAssassin settings when those settings are stored in a SQL DB rather than a config file. It also allows you to use a quarantine database for questionable mail. This plugin was designed with enterprise use in mind, and differs from other plugins in that it works with amavis-new rather than SpamAssassin directly. Most of the code lives in an external class for you to reuse in your own admin tools.. and even has support for SOAP calls to perform common tasks.

 [1]: http://squirrelmail.org

This is a placeholder page for a Squirrel Mail plugin I wrote many years ago when I was the mail admin for a 4k employee publishing company.  The last update (until recently) was 2005.   It proved to be more popular than I expected… having about 25k downloads.  Recently I’ve heard from a couple people who wanted some fixes done to make it work with the latest versions of SQM and php and so after all these years I decided to fix it up and re-release it.

The source is now [hosted at Github][2] and I’ve been using this plugin as an excuse to learn and start using Git.. and Git flow.  The actual download page is on the [Squirrel Mail site][3].

<div class="github-widget" data-repo="jimmydigital/amavisnewsql"></div>

 [2]: https://github.com/jimmydigital/amavisnewsql
 [3]: http://squirrelmail.org/plugin_view.php?id=224
