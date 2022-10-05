---
title: 'What I do: Interviewing for Linux Engineers'
date: 2011-12-11
categories:
  - Computing and Tech
  - Geeky Stuff
  - Personal
  - Projects
tags:
  - engineering
  - interview
  - interview questions
  - linux
  - load average
  - resume
---

Now and then I’m called on to help interview candidates for linux admin/engineer slots and as I’ve been doing some of that lately I thought I’d share the way I go about doing a technical interview. This approach seems to work equally well over the phone or in person. <!--more-->

I’m big on understanding the fundamentals of linux. If someone comes to me with a resume showing 10 years of experience building and managing production unix/linux systems there are certain things I’d expect them to know.. and to a certain depth. If they obviously don’t.. then I have to question the validity of what’s on the resume. So what I’ll usually do is pick a few key areas and start off with some general (easy) questions and then drill down a bit to discover the level of understanding on that particular topic. As an example.. I’ll share one of my favorites and lay it out the way I might do it during an interview.

Q: If I wanted to know who was logged in, how busy a system was and how long it had been up what command would tell me all that?

(Assuming they get that I’m looking for the ‘w’ command and mention the system load)

Q: Why are there three numbers for the system load?

(Assuming they know about the 3 time periods)

Q: What is the system load.. what do those averages actually represent?

(This usually starts to trip up the junior people but assuming they know it’s the run queue length)

Q: How does a multi-cpu system affect your interpretation of system load?

(Assuming they say something about dividing load by CPU count)

Q: Describe the relationship between the load average measurement and the percentage busy you might get from ‘top’.

This is usually about as far as I’ll take something like this.. but it can lead to a discussion about things like different kernel schedulers and how they can be tweaked etc. If a person can answer these and have that sort of discussion it tells me they have the right depth of understanding a senior person should have… at least on this area. Someone who has been an admin (but not what I’d classify as an engineer) should be able to answer at least the first 2 questions.
