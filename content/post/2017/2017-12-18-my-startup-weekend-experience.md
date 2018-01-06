---
categories:
- "Seattle"
- "Projects"
- "Personal"
date: 2017-12-18T12:15:56-06:00
description: "My 2014 StartupWeekend experience where I mostly learned about team leadership and how important it is to be able to simplify complex ideas and find their essense."
draft: false
tags:
- "Seattle"
- "Startup"
- "traffic"
- "traffic wave"
- "car technology"
- "automated driving"
- "sensor fusion"
- "behavior modification"

title: My StartupWeekend Experience
---
One of the more fun things I did in Seattle back in 2014 was to participate in a [StartupWeekend][1]
event with another guy from Amazon. I'd never heard of these events and he described it
as being like a hackathon. So I was in and joined him on at the start of the event that Friday night
at the Google campus in Kirkland. We quickly discovered that this wasn't anything like a hackathon.<!--more-->
We were expected to write a business and marketing plan, do a customer analysis etc. so what we brought to work on wasn't the right choice.
So.. with minimal prep I pitched an idea to a room of about 200 people and managed to convince two others to join our team.
One was a web developer and the other a business development person from another big tech company.

## The Idea

The idea was to build a system to help eliminate [traffic waves][2] on busy roads which we called SmartCruize. If
fully implemented it could also do things like have car [Platoons][3] and coordinated movement around traffic lights.
It was a basically an implementation of a car-to-car communication network that could identify and track the movements
of the cars around you and communicate your actions and intentions to the cars behind you. With such a network in place
it would be possible to coordinate the speed and relative movements of cars in a very efficient way to increase the
capacity of the existing roads and eliminate the most common causes of traffic jams.

It was ambitious to be sure.. but after a few rounds of simplifying the idea we decided to build an app that
could roughly track the movements of a car and would gameify the driving experience to encourage good habits.
For example using GPS we can identify what road you are on and the speed limit
and you are going slower than that monitor how frequently you are using your brakes.. changing speeds etc. to
encourage increased following distance and less braking.

At the time our thoughts on a full hardware implementation involved a mix of short range radio (mesh networking) combined
with rear-facing infrared beacons that would broadcast a unique car ID to the vehicle directly behind you and a forward facing
distance sensor to monitor forward car spacing and relative movements.  If I were doing this project today I might replace some of
sensors with a camera with some onboard video processing.

## Failure is Always an Option

The idea with StartupWeekend is that by Sunday night, when the results are shared, you have a viable shell of a company which includes
a business plan, market/customer analysis, and at least one paying customer. Our team was doing well until Saturday night.  We had a
website that did a walk through of how it was supposed to work with a mock up of the app. We had a customer survey written with some
responses that helped shape the business plan. We also knew what we wanted the app to do.. but that's where we hit a snag. Our two
developers were not happy with the greatly reduced scope of what we were trying to deliver that weekend and they bailed on us.

Though we produced nothing of value I think it was a still a worthwhile experience.  It was fun pulling together this group
of strangers to try to build something and the experience of iterating to simplify a complex project was
challenging and a useful exercise. Simple solutions are almost always better than complicated ones and fighting complexity
should be one of the core missions of any engineer.

I've been asked if I would do one of these events again. I would.. but knowing now what I'm signing up for I'd be better
prepared and not starting from scratch on a busy Friday night.

[1]: https://startupweekend.org/
[2]: http://trafficwaves.org/
[3]: https://en.wikipedia.org/wiki/Platoon_(automobile)

