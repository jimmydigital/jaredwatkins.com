---
title: R2Beer2
date: 2026-05-25
draft: false
description: ""
categories:
  - ""
tags:
  - ""
images: []
---
I joined AWS in late 2012 on a team that owned several low-level infrastructure services. In all my time there it was the most difficult team I'd been on, pager PTSD, brutal ops load, and a bunch of mission critical, but unrelated, services to learn. But that kind of crucible forges good friendships, and those have lasted long past my turn on that team. At the time, AWS held a monthly beer bust in the big conference room at the top of the Blackfoot building in downtown Seattle. Each month would be hosted by a different service team and would have a different theme chosen by that team.

We got about six months' notice when our turn came up, and for once things were going well enough that we had some cycles to spare. Our manager, Mike, was a very positive and energetic guy who happened to love Star Wars, so that was selected for our party theme. I don't remember exactly how the idea surfaced, but a few of us decided we needed to build an R2-themed, beer-dispensing robot for the party. Justin volunteered his garage for the build and started scrounging parts from thrift shops around town. The wooden milk powder barrel was one of the first pieces we found, and it's what pushed us toward a steampunk R2 aesthetic. We were improvising with whatever we could scrounge, so we leaned into it. Dhan offered to help with the RC electronics and I pitched in where I could in other areas.

I found an old electric wheelchair on Craigslist with dead batteries and salvaged the 24v motors and wheels out of it. I also took some classes at a little private shop near Boeing Field and learned to MIG weld well enough to get by. I sourced and put together the CO2 system to serve the beer and built the head electronics that drove lights, R2 sounds, and head movements. That ran on an Arduino Uno with some C code, plus a couple of supporting boards for sound playback and I2C-programmable LEDs. I also helped with other parts of the build like refinishing the barrel and making various mounting fixtures. Everything above the motorized base could be removed for loading the keg (wrapped in ice blankets). The legs, for instance, were held on by bolts welded to cup-shaped candle holder bases. It took us roughly 200 hours over 3.5 months that summer of 2013 to build R2Beer2 1.0, and it was one of the more fun things I've built.

We had it ready for the party, but "ready" was doing a lot of work in that sentence. The pair of MDF plates mounting the head to the barrel tended to drag and prevent the head from rotating. The lead batteries were too large and heavy for the amount of energy we needed. Worse, mounting the motors directly to the aluminum relay rack base frame was causing the whole assembly to flex and deflect. The front wheel mounted on two thin strips of plate aluminum was also flexing and bending every time we changed directions. The whole thing weighed about 250 lbs loaded with a full keg. It was a lot. As if all that weren't enough, the beer was coming out with way too much foam!

After a few events and a clear-eyed look at everything that was wrong with the gen1, I started work on a round of refinements. This included a total redo of how the motors and front wheel mounted to the frame. I picked up some scrap 1/4" steel plate from a metal vendor in south Seattle and did some precision (for my garage) work to mount the motors to this plate, which the frame then sat on. Same for the front wheel mount. My other big contribution was to redo the way the head mounted to the barrel body. I replaced the pair of MDF plates with a lightweight steel adjustable suspension mount that was easily fine-tuned for center and height and fixed all the drag issues. It also let me run power and signal wires up from the base, eliminating the separate batteries in the head that were a constant nuisance to swap. Most importantly, I fixed the foaming beer problem by adjusting the pressure down slightly and putting longer tubing between the keg and faucets.

While I worked on the structural and functional side, Justin focused on several aesthetic upgrades to the head. Leather patches and actual hand-hammered copper rivets, which required a delicate touch on the fiberglass. The results looked fantastic and much closer to the original look we were after.

The first appearance was October 2013 at the beer bust, followed by events in various buildings around Seattle for a while after. Having had my fun for three years on that team, I moved on around mid-2015 and transferred ownership of R2 to Mike, who continued to take it to events through at least 2019, including one stage visit at re:Invent. So what happened to it? When Mike moved on he took R2, which went through a bit of an identity crisis and emerged as BrewskiBot. Under that name it continued to make appearances (paid ones this time) at weddings and parties, though links to those events seem to have vanished from the internet. It appears R2 has now retired from the party circuit, getting a well-earned rest. It was never built to last, but it hung in there well and proved more resilient than I ever expected.

I had a roadmap of upgrades that never materialized: an insulated barrel with refrigeration, Wi-Fi for beyond-line-of-sight control, a badge reader with serving metrics and a dashboard, and automated internal awards for top consumers. At some point we decided that gamifying beer consumption was probably a bad idea for an office full of competitive developer types. Still, it was one of those projects where you learn something new every weekend (welding, CO2 systems, embedded electronics, fiberglass) and then get to wheel the thing into an office party. I got more out of it than I put in.



{{< gallery cols="3" >}}
- pre_barrels_before.jpg
  Barrels before refinishing
  Found these great lightweight barrels but a little rusty.
- pre_cleaned_up_barrel_on_base.jpg
  Cleaned up barrel on base
- pre_head_foam_huge.jpg
  Head foam form
  Our first attempt at a head mold was way too big.
- pre_head_initial_mold.jpg
  Head initial mold
- pre_early_frame01.jpg
  Early frame build
  Early frame ideas before we decided to just use the barrels
- pre_base_progress1.jpg
  Base frame progress
- pre_first_shield_mount.jpg
  First shield mount
  Front brass shield from a fireplace wood carrier
- pre_green_head1.jpg
  Green head mock-up
  Didn't quite have the final shape down but mocking up for fit and appearance. 
- pre_green_head2.jpg
  Green head mock-up
- pre_green_head3.jpg
  Green head mock-up
  That looks better
- pre_green_head_final_shape.jpg
  Green head final shape
- pre_mock_legs.jpg
  Mock legs
- pre_mock_legs2.jpg
  Mock legs
- pre_mock_legs3.jpg
  Mock legs
- pre_mock_legs_glassed_battery_cover.jpg
  Mock legs with glassed battery cover
- pre_mock_legs_shield.jpg
  Mock legs with shield
- pre_motor_mounts.jpg
  Motor mounts
  Gen1 motor mount detail with rc receiver. Went straight to the rack frame which wasn't strong enough.
- beer_line.jpg
  Beer line
  Beer line fittings
- gen1_base_motor_mounts_topview.jpg
  Gen 1 base motor mounts top view
  Gen1 top view of installed motors and frame.
- gen1_beer_line_installed.jpg
  Gen 1 beer line installed
  Gen1 beer line installed. The short runs ended up making too much foam. 
- gen1_front_wheel_mount1.jpg
  Gen 1 front wheel mount
  Gen1 front wheel mount detail. This deflected too much under weight.
- gen1_motor_mount_deflection.jpg
  Gen 1 motor mount deflection
  Look at that deflection! This will end in tears if we don't fix.
- gen1_front_wheel_mount2.jpg
  Gen 1 front wheel mount
- gen1_head_plates1.jpg
  Gen 1 head plates
  Gen1 head mounting plates. Ended up being too heavy and would drag on the barrel. 
- gen1_head_wiring1.jpg
  Gen 1 head wiring
- gen1_meeting1.jpg
  Gen 1 team meeting
- gen1_office1.jpg
  Gen 1 in the office
- gen1_office2.jpg
  Gen 1 in the office
- gen1_office3.jpg
  Gen 1 in the office
- gen1_office4.jpg
  Gen 1 in the office
- gen1_office5.jpg
  Gen 1 in the office
- gen1_office6.jpg
  Gen 1 in the office
- gen1_office7.jpg
  Gen 1 in the office
- gen1_party2.jpg
  Gen 1 party
- gen1_party3.jpg
  Gen 1 party
- gen1_party4.jpg
  Gen 1 party
- gen1_party5.jpg
  Gen 1 party
- gen1_party_chris.jpg
  Gen 1 party — Chris
- gen1_party_makers1.jpg
  Gen 1 party — makers
- gen1_party_makers2.jpg
  Gen 1 party — makers
- gen1_party_makers3.jpg
  Gen 1 party — makers
- gen1_party_mike.jpg
  Gen 1 party — Mike
- gen1_party_screen.jpg
  Gen 1 party — screen
- gen1_party_trooper.jpg
  Gen 1 party — stormtrooper
- gen1_party_trooper1.jpg
  Gen 1 party — stormtrooper
- gen1_party_trooper2.jpg
  Gen 1 party — stormtrooper
- gen1_safety_third.jpg
  Safety third
  Final assembly and finishing in the office. Safety third!
- gen2_battery_bracket1.jpg
  Gen 2 battery bracket
- gen2_battery_bracket2.jpg
  Gen 2 battery bracket
- gen2_battery_bracket3.jpg
  Gen 2 battery bracket
  Made a custom bracket to hold smaller batteries tucked up under the frame. Relocated from the rear and deleted large battery box cover.
- gen2_battery_bracket_installed.jpg
  Gen 2 battery bracket installed
- gen2_battery_bracket_installed2.jpg
  Gen 2 battery bracket installed
- gen2_battery_bracket_installed3.jpg
  Gen 2 battery bracket installed
- gen2_battery_mount_position.jpg
  Gen 2 battery mount position
- gen2_bottle_bracket.jpg
  Gen 2 bottle bracket
  CO2 bottle bracket
- gen2_front_wheel_mount_upgrade.jpg
  Gen 2 front wheel mount upgrade
  Front wheel mount gets a steel upgrade
- gen2_head_electronics_complete1.jpg
  Gen 2 head electronics complete
  Not my best work but good enough! Complete and mounted head electronics. 
- gen2_head_electronics_complete2.jpg
  Gen 2 head electronics complete
- gen2_head_electronics_complete3.jpg
  Gen 2 head electronics complete
  Let me double check that wiring diagram
- gen2_head_electronics_detail.jpg
  Gen 2 head electronics detail
- gen2_head_electronics_detail1.jpg
  Gen 2 head electronics detail
- gen2_head_electronics_detail2.jpg
  Gen 2 head electronics detail
  Tried a few different ways of connecting the base to the head. Ended up using an ethernet jack to carry 24v and some signals from the RC receiver. That's cool right?
- gen2_head_electronics_detail3.jpg
  Gen 2 head electronics detail
- gen2_head_electronics_detail4.jpg
  Gen 2 head electronics detail
- gen2_head_electronics_mount_bare.jpg
  Gen 2 head electronics mount bare
- gen2_head_electronics_mounted1.jpg
  Gen 2 head electronics mounted
  Arduino Uno, sound playback board and 1W amp, dc/dc power boards. I took 24v from the main battery and needed both 5v and 3.3v. 
- gen2_head_electronics_wiring1.jpg
  Gen 2 head electronics wiring
- gen2_head_mount1.jpg
  Gen 2 head mount
- gen2_head_mount_detail.jpg
  Gen 2 head mount detail
  Adjustable mount allows centering the head on the barrel.
- gen2_head_mount_detail2.jpg
  Gen 2 head mount detail
- gen2_head_mount_detail3.jpg
  Gen 2 head mount detail
  Drilled the motor shaft and that nut. This pin connects the bottom spider mount to the upper mount via the motor shaft. 
- gen2_head_mount_detail4.jpg
  Gen 2 head mount detail
- gen2_head_mount_fitting.jpg
  Gen 2 head mount fitting
- gen2_head_mount_motor_fitting.jpg
  Gen 2 head mount motor fitting
- gen2_head_mount_spider_fitting.jpg
  Gen 2 head mount spider fitting
  Gen2 spider mount for the head. Lighter and allows free rotation. Replaces MDF plates.
- gen2_head_on_table.jpg
  Gen 2 head on table
- gen2_head_on_table2.jpg
  Gen 2 head on table
- gen2_head_on_table3.jpg
  Gen 2 head on table
- gen2_head_on_table4.jpg
  Gen 2 head on table
- gen2_head_underside_wiring.jpg
  Gen 2 head underside wiring
- gen2_led_programming.jpg
  Gen 2 LED programming
- gen2_motor_plate_drilling.jpg
  Gen 2 motor plate drilling
  Making the new motor mount plate out of 1/4" steel.
- gen2_motor_plate_drilling2.jpg
  Gen 2 motor plate drilling
  Used paper templates taped to the ends of the plate for somewhat precise drilling on a wobbly harbor freight drill press. 
- gen2_motor_plate_finished.jpg
  Gen 2 motor plate finished
- gen2_motor_plate_finished2.jpg
  Gen 2 motor plate finished
- gen2_motor_plate_fitting.jpg
  Gen 2 motor plate fitting
  I can't believe how well everything aligns. All holes drilled by hand using those paper templates.
- gen2_motor_plate_installed.jpg
  Gen 2 motor plate installed
- gen2_motor_plate_installed2.jpg
  Gen 2 motor plate installed
   No deflection here.
- gen2_naked_base.jpg
  Gen 2 naked base
- gen2_office1.jpg
  Gen 2 in the office
- gen2_office2.jpg
  Gen 2 in the office
- gen2_office3.jpg
  Gen 2 in the office
- gen2_party1.jpg
  Gen 2 party
- gen2_party2.jpg
  Gen 2 party

{{</ gallery >}}
