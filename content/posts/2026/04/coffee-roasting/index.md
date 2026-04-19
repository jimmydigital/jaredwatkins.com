---
title: Home Coffee Roasting - Hobby That Tastes Great
date: 2026-04-18
draft: false
description: How I got into home coffee roasting, upgraded equipment over the years, and added finer airflow control to improve heat transfer during the roast.
categories:
  - hobbies
tags:
  - coffee
  - roasting
  - equipment-hacking
thumbnail: ""
images: []
---

I never drank coffee before about three years ago, but I've been roasting and brewing it at home for much longer. The story starts about ten years back when I met my wife in Seattle. She's a big coffee drinker, and one of the things I started doing was making her coffee in the mornings. I tried a bunch of different brewing methods and eventually landed on the Aeropress, which just gave me the most consistent results making one or two cups in a morning. 

<!--more-->

Actually, we didn't get serious about coffee until we moved to the Dallas suburbs. There was this fantastic specialty roaster there, [Addison Roasters](https://www.addisoncoffee.com/), that carried single-origin coffees from all over the world. At any given time you could walk in and find a dozen or more different single origins available by the pound. I got fascinated by the regional differences, what makes something specialty grade, the whole business side of it. I wasn't roasting coffee myself yet (or even drinking it, really)—just buying the good stuff and learning. I also picked up a few books on the subject. 

## Pandemic Opportunity

Fast forward a couple years, we're in Northern Virginia (not long after Amazon picked the area for HQ2). Then the pandemic hit, and like the rest of the DC suburbs, lockdowns, restrictions, all of it. Bored and stuck at home, I decided to start roasting coffee. I bought a used Artisan 2.5 from a local shop that was upgrading their gear, set it up in a spare room with 220V power and a window for venting.

Over the next couple years I gradually hacked on it to increase performance. Airflow improvements, better chaff filtering, eventually it became an Artisan 3 (the 3-pound model) inside. It was cobbled together with hoses everywhere, not pretty, but it worked and I learned a lot. One of the problems I solved was with the exhaust blower. It was a cheap blower that vibrated like crazy. When I bought it came hard mounted to that little wire cart but it made a ton of noise and vibrated the bean cooler pretty badly.  So.. simple fix.. I separated the two bits of plywood and added some little eyelets and some parachute cord zig-zagging between them to make a vibration isolated suspension mount.  So the blower motor actually hangs under the lower shelf with the two boards only connected by the parachute cord.  I didn't expect it to work so well so didn't bother to make it look good.  It took me all of about 15 minutes but drastically improved the noise while roasting so I just left it. 

Once I had the setup dialed in I started selling to the neighbors. People were stuck at home and didn't want to go out, so I built a little pickup box outside and ran orders through Stripe and advertised through Nextdoor. The Stripe setup turned out to be overkill as everyone preferred to pay with cash in the dropbox. I wasn't trying to build a business, just pay for my hobby. Three or four single origins in rotation, and it worked great for a while with enough repeat customers to pay for the coffee and make it worth my time.  That lasted for a couple years until we moved again. 

![Artisan Roasting Setup|300](roaster_artisan01.jpg "width=300#floatright") ![Coffee Box|400](coffee_box01.jpg "width=300#floatleft")


## New Gear

![Crated Up For the Next Person to Enjoy|300](crated01.jpg "height=300#floatleft")
![Close it up|300](crated02.jpg "height=300#floatright")

I've been following [Coffee Crafters](https://coffeecrafters.com/) for years as they make the roaster I'd been using. They're an American company doing their own design and manufacturing, which I really respect. When they released the Valenta series in early 2025, I bought one. I crated up the the Artisan and went all in on the Valenta 3. It's cleaner, way more compact, fits on a little rolling table in my office. I still roast periodically with a few single origins, though I'm not selling to neighbors anymore. (Could if I wanted to. This thing makes it pretty easy.) I had to make some improvements through. I added a dedicated Raspberry PI with screen to run the optional roasting software (also confusingly called [Artisan](https://artisan-scope.org/)) and then made a few other modifications. 

![Valenta Roaster Setup|300](valenta01.jpg "width=300#floatright")


## The Airflow Problem and My Fix

Here's the thing I've dealt with on both machines: airflow control during the roast is finicky. As beans lose density and expand, they float differently in the air, and the rate of heat transfer changes. The idea is simple: start at max airflow, dial it back as the beans dry and expand to maintain a sufficient loft without blowing beans out the top. It also helps you manage the transition from the drying phase to the development phase and you get faster roasts and better flavors.

Roasting temperature matters most (I aim for 415F for most beans), but the roast length and airflow management matter too. You want to hit temperature fast without over-extending the roast (baking the beans).

The factory loft air control is a little crude. A solid-state relay uses the voltage through a potentiometer to modulate power to the blower motor, but the dial doesn't give you fine control. So I added a second pot in series, rated at about 10% of the factory range. Now I just set the factory knob at the max for this bean mass (usually around 4) and use my secondary adjustment which gives me a full rotation to play with rather than just 1/10 of the arc on the factory knob. Much finer control. That's important because if you slip and cut loft air too much you risk stalling the bean fountain and scorching the beans or even starting a fire.

![Valenta Beans|600](valenta02.jpg "height=600")

