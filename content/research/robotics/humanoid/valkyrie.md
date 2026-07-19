---
title: "Valkyrie (NASA R5)"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "NASA Johnson Space Center's 44-degree-of-freedom, series-elastic-actuated bipedal humanoid, built in 15 months for the 2013 DARPA Robotics Challenge; scored zero points at the Trials due to a network configuration bug; became the origin platform for the UT Series Elastic Actuator lineage and for Apptronik's founding team; distributed to IHMC, MIT, Northeastern/UMass Lowell, and the University of Edinburgh for space-robotics research; currently under a Space Act Agreement with Woodside Energy (Australia) testing remote dexterous manipulation for uncrewed offshore facilities, with operational demonstrations planned 2026–2027."
research_area: "robotics/humanoid"
source_urls:
  - "https://www.nasa.gov/technology/r5/"
  - "https://www.nasa.gov/wp-content/uploads/2023/06/r5-fact-sheet.pdf"
  - "https://onlinelibrary.wiley.com/doi/10.1002/rob.21560"
  - "https://spectrum.ieee.org/update-nasa-valkyrie-robot"
  - "https://spectrum.ieee.org/new-r5-valkyrie-robots"
  - "https://spectrum.ieee.org/nasa-awards-r5-valkyrie-robots-to-mit-and-northeastern"
  - "https://www.nasa.gov/centers-and-facilities/johnson/nasa-humanoid-robot-to-be-tested-in-australia/"
  - "https://en.wikipedia.org/wiki/Valkyrie_(robot)"
  - "https://valkyrie.inf.ed.ac.uk/"
last_reviewed: 2026-07-18
stale_after_days: 180
related:
  - "../actuators/ut-series-elastic-actuator.md"
  - "us-companies/apptronik.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Valkyrie, also designated R5, is a 44-degree-of-freedom bipedal humanoid robot designed and built by NASA's Johnson Space Center (JSC) Engineering Directorate to compete in the December 2013 DARPA Robotics Challenge (DRC) Trials. Built in just 15 months by a team of roughly 35 engineers under Nic Radford and Rob Ambrose, and drawing on prior JSC humanoid experience from Robonaut 2, Valkyrie was one of the most heavily instrumented and mechanically ambitious entrants in the DRC — and one of its most public failures, scoring zero points at the Trials due to a software networking bug rather than any fundamental hardware shortcoming. Rather than retiring the platform, NASA redirected it into a decade-long research program: partnering with the Florida Institute for Human and Machine Cognition (IHMC) on whole-body control, then distributing additional Valkyrie units to MIT, Northeastern University (hosted at UMass Lowell's NERVE Center), and the University of Edinburgh as part of NASA's Space Robotics Challenge and "humanoid avatar" research agenda. Valkyrie's actuator architecture — developed in partnership with the University of Texas at Austin's Human Centered Robotics Lab — became the direct technical and human origin point for both the [UT Series Elastic Actuator]({{< relref "../actuators/ut-series-elastic-actuator.md" >}}) design lineage and, in 2016, for the founding of [Apptronik]({{< relref "us-companies/apptronik.md" >}}) by several Valkyrie alumni. As of the mid-2020s, Valkyrie remains an active NASA research platform, most recently deployed to Woodside Energy's Perth, Australia facilities under a reimbursable Space Act Agreement to develop remote dexterous manipulation capabilities for uncrewed offshore oil and gas infrastructure, with operational demonstrations planned for 2026–2027.

## Key Facts

- **Developer:** NASA Johnson Space Center (JSC) Engineering Directorate
- **Program leadership:** Nic Radford and Rob Ambrose (JSC); ~35-person design team
- **Design period:** October 2012 (design start) to July 2013 (alpha assembly) — approximately 15 months
- **Type:** Robot platform / breakthrough — government-developed research humanoid, not a commercial product
- **Status:** Active research platform (multiple units in use across NASA, IHMC, and university partners as of the mid-2020s)
- **Specifications (per NASA official fact sheet):** 300 lbs (~136 kg); 6 ft 2 in (~1.88 m); 44 degrees of freedom; 1.8 kWh battery (~1 hour runtime); 2× Intel Core i7 onboard computers
- **Note on spec variance:** Secondary sources report slightly different figures for individual units — Wikipedia cites ~129 kg and 3× Intel Core i7; the University of Edinburgh's specific unit is documented at 125 kg, 1.8 m, and "32 DOF body + 6 DOF hands." These are treated here as unit-to-unit or source-transcription variance rather than a single disputed fact — the NASA official fact sheet is used as the primary figure.
- **Actuation:** Series elastic actuators throughout — rotary in arms/legs/torso/pelvis, linear in wrists, ankles, and torso-pelvis joint — developed with University of Texas at Austin's Human Centered Robotics Lab; see [UT Series Elastic Actuator (UT-SEA)]({{< relref "../actuators/ut-series-elastic-actuator.md" >}})
- **2013 DRC Trials result:** 0 points, attributed to a network traffic-shaping software bug, not a hardware failure
- **2015 DRC Finals:** Did not compete (no robot fielded in the Finals); present to promote NASA's new Space Robotics Challenge
- **University/lab distribution (by 2016):** NASA JSC (original), IHMC (Florida), MIT, Northeastern University (hosted at UMass Lowell's NERVE Center), University of Edinburgh — at least 5 units in the broader Valkyrie/R5 fleet
- **Current commercial-adjacent deployment:** Woodside Energy (Perth, Western Australia) — Space Act Agreement for remote dexterous manipulation of uncrewed offshore facilities; operational demonstrations planned 2026–2027
- **Direct commercial descendant:** [Apptronik]({{< relref "us-companies/apptronik.md" >}}), founded 2016 by five UT Austin/NASA Valkyrie-affiliated co-founders including actuator designer Nicholas Paine

## What It Is / How It Works

**Origins and design philosophy:** Valkyrie's design began in October 2012 at NASA JSC, explicitly to compete in the DARPA Robotics Challenge — a competition motivated by the aftermath of the Fukushima Daiichi nuclear disaster, where a humanoid capable of operating human-engineered equipment (doors, valves, vehicles, power tools) in a degraded, human-built environment without infrastructure modification was the core value proposition. Valkyrie built on the JSC team's prior experience designing Robonaut 2 (NASA's earlier upper-body-only humanoid, flown to the International Space Station), but its overall design was entirely new rather than an extension of that platform. NASA's own framing emphasizes robustness and ruggedness: an "entirely electric" humanoid (no hydraulics) intended to work in degraded or damaged human environments — the disaster-response use case at the DRC's core, later reframed toward space applications.

**Actuator architecture:** Valkyrie is a series-elastic robot throughout its body — a design choice that, per NASA's own fact sheet, distributes compliant actuation across every major joint: each upper arm uses four series elastic rotary actuators (seven joints total when combined with the forearm); each upper leg uses five series elastic rotary actuators, with each ankle realized by two series elastic linear actuators working in concert; the torso houses two series elastic rotary actuators plus two series elastic linear actuators (for torso-pelvis motion); and the pelvis — considered the robot's base frame — houses three more series elastic rotary actuators (waist rotation and each hip's rotation joint) alongside two inertial measurement units. Each forearm adds one rotary actuator (wrist roll), a pair of linear actuators (wrist pitch/yaw), and six finger/thumb actuators driving a simplified three-finger-plus-thumb hand. This series-elastic architecture throughout the body — rather than only at select joints — was itself a distinguishing design bet, and the specific rotary and linear SEA implementations were developed in direct partnership with the University of Texas at Austin's Human Centered Robotics Lab, which "provided expertise in the design of rotary series elastic actuators and inspiration for the design of the linear series elastic actuators" used on the robot's ankles and torso — the same lineage documented in this knowledge base's [UT Series Elastic Actuator (UT-SEA)]({{< relref "../actuators/ut-series-elastic-actuator.md" >}}) entry, where Nicholas Paine's UT PhD dissertation formalized the underlying ball-screw/RFSEA design.

**Sensing — "overloaded with sensors":** Valkyrie's head sits atop a 3-DOF neck, with a Carnegie Robotics MultiSense SL unit as its primary perception sensor (modified to add IR structured-light point-cloud generation alongside its existing laser and passive-stereo sensing), plus fore and aft "hazard cameras" in the torso. According to IHMC's Peter Neuhaus, presenting on the team's behalf in 2014, the original build was, in the team's own retrospective assessment, "overloaded with sensors" — three LIDAR units, four HD cameras, and six depth-map cameras in the visual-sensing suite alone — a decision driven by uncertainty about which sensors would prove necessary, compounded by a desire for sensing redundancy.

**The 2013 DRC Trials: zero points, and why.** At the DRC Trials in December 2013, Valkyrie scored zero points. The proximate cause was not a fundamental hardware or control-software failure: the team had added a network traffic-shaping tool to their code that, once deployed on the actual competition course (rather than in their home-garage testing), blocked data flow from the human operator to the robot, manifesting as "major instability in the control system" that left the robot effectively uncontrollable. The bug was fixed in time for the last event of the first day (opening three doors), but by then the bulk of Valkyrie's scoring opportunities had already been missed. In JSC's own mock DRC trials beforehand, Valkyrie had reliably scored 6–8 points — suggesting that had the harder tasks been scheduled for Day 1 instead of Day 2, the team might have identified and fixed the networking issue in time to attempt the easier Day 2 tasks. Separately, the team's own retrospective noted that after alpha assembly in July 2013, a disproportionate share of remaining development time went into "soft goods" (the robot's cosmetic/protective covering) rather than control software — a resourcing decision the team itself later characterized as suboptimal — compounded by a roughly six-week schedule loss from the October 2013 U.S. federal government shutdown (16 days shut down, plus about a month to bring contractor staff back to full speed).

**From DRC failure to long-term research platform.** Rather than discontinuing Valkyrie after its DRC Trials showing, NASA redirected the program: securing a National Robotics Initiative grant for "Toward Humanoid Avatar Robots for Co-exploration of Hazardous Environments" in partnership with IHMC, whose whole-body walking-control expertise (developed on Boston Dynamics' Atlas for their own DRC entry) was ported onto Valkyrie hardware. IHMC's early platform assessment — candid and specific — found force control "really good," identified the need for somewhat more knee torque and hip range of motion, called for a wider-field-of-view head LIDAR, and noted Valkyrie's ease of disassembly/reassembly and "nice safety systems for human interaction" (an explicit favorable comparison to Atlas, which IHMC's own team found less comfortable to work around). The stated long-run NASA vision, repeated consistently from 2014 onward: a humanoid "avatar" sent ahead of astronauts to Mars or the Moon, assistively teleoperated to assemble structures and prepare habitats before human arrival, and later available to perform maintenance and repair tasks that free astronauts for higher-value work — with the same underlying disaster-response/search-and-rescue value proposition that motivated the original DRC.

**The 2015 Space Robotics Challenge and university distribution.** Valkyrie did not compete in the June 2015 DRC Finals (won by Team KAIST's DRC-Hubo), but was present at the event to promote NASA's newly announced Space Robotics Challenge (SRC). As part of the SRC program, NASA ran a competitive selection process and in November 2015 named two winning university teams — MIT under Russ Tedrake (whose team had placed 6th in the DRC Finals with an Atlas robot) and Northeastern University under Taskin Padir (7th place in the Finals with an upgraded Atlas) — each receiving a Valkyrie/R5 unit plus up to $500,000 in funding over two years, along with NASA technical support. A parallel, separately funded UK collaboration placed a fourth unit at the University of Edinburgh's Robotarium (part of the Edinburgh Centre for Robotics, a joint initiative with Heriot-Watt University), under academic leadership from Sethu Vijayakumar, Zhibin Li, and Michael Mistry, with Maurice Fallon (a former MIT DRC team member) leading much of the perception work. A fifth unit remained at IHMC in Florida. Units delivered in this 2016 wave (designated "Unit D") carried hardware upgrades over the original 2013 Trials robot: a redesigned head incorporating the MultiSense SL camera/LIDAR array (matching Atlas's sensor head, easing cross-platform perception work), removed leg cameras, increased pelvis range of motion, and a new plastic shell with cooling fans replacing the original fabric leg covers, alongside safer battery designs.

**Distributed, collaborative software development.** The university partners explicitly built and shared a common software base rather than competing in isolation: a MIT Drake-based user interface, IHMC's SCS-based lower-body control software, and Edinburgh's EXOTica motion-planning software were developed jointly across NASA, MIT, IHMC, and Edinburgh, with Northeastern collaborating as part of the SRC effort specifically. MIT and Edinburgh jointly open-sourced their DRC-era Valkyrie/Atlas codebase (the "oh-distro" project) on GitHub in early 2016. Each university team pursued a distinct research emphasis within this shared base: Northeastern/UMass Lowell focused on space-relevant manipulation and locomotion tasks (solar panel maintenance, electrical panel repair, sample collection) using the 10,000-square-foot NERVE Center test facility; MIT pushed toward more dynamic whole-body behaviors (ladder climbing, more aggressive dexterous manipulation) and integration with higher-level task-and-motion-planning research (in collaboration with Leslie Kaelbling and Tomas Lozano-Perez); and Edinburgh pursued dexterity, visual tracking/mapping, and data-driven dynamics learning to complement model-based control, while training more than 80 robotics PhD students over the following decade as part of its broader Centre for Robotics program.

**Terrestrial commercial-adjacent testing — Woodside Energy.** In a notable departure from Valkyrie's space-exploration framing, NASA's Dexterous Robotics Team (led by Shaun Azimi) entered a reimbursable Space Act Agreement with Woodside Energy, an oil and gas operator headquartered in Perth, Western Australia, to develop remote mobile dexterous manipulation capabilities for uncrewed and offshore energy facilities — announced July 2023 as the second such reimbursable collaboration between NASA and Woodside. The stated rationale runs in both directions: Woodside gains a potential path to safer, more efficient remote operation of offshore infrastructure without putting personnel in hazardous environments, while NASA gains real-world engineering data and lessons that feed directly back into Artemis-program robotics development for lunar and Martian surface operations, where remotely operated robots would perform infrastructure inspection, maintenance, and in-situ resource utilization tasks ahead of or in place of astronaut presence. Per NASA's own July 2023 release, the agency plans to apply the resulting software development work "to upcoming hardware releases and perform operational demonstrations with Woodside... in 2026–2027" — meaning Valkyrie's Woodside deployment is an active, ongoing program during the period this entry was written, not a completed or historical engagement.

**The Apptronik connection.** As of an August 2014 IEEE Spectrum report — filed less than a year after the DRC Trials — "some of the team that was working at JSC to develop Valkyrie" had already moved on to found their own startup, though that report did not name the company or provide further detail. Whether or not that specific 2014 reference describes the same group, Apptronik was formally founded in 2016 by five co-founders with direct UT Austin Human Centered Robotics Lab and NASA Valkyrie backgrounds, including Nicholas Paine (the UT-SEA's originator, who worked on Valkyrie's actuator-level torque control as a NASA-JSC DRC team member in 2012–2013) and Prof. Luis Sentis (the HCRL's director and a co-author on Valkyrie's actuator-control publications). Apptronik's Apollo robot is the direct commercial descendant of the actuator technology and organizational expertise developed on Valkyrie — see [Apptronik]({{< relref "us-companies/apptronik.md" >}}) for the company's full profile.

## Notable Developments

- **2026–2027 (planned):** NASA and Woodside Energy to conduct operational demonstrations of Valkyrie-derived remote dexterous manipulation capabilities in relevant offshore/remote settings, applying software development work to upcoming hardware releases.
- **2023-07:** NASA announces a second reimbursable Space Act Agreement with Woodside Energy (Perth, Western Australia) to develop and test remote dexterous manipulation for uncrewed offshore oil and gas facilities.
- **2016 (Spring):** "Unit D" Valkyrie robots (redesigned MultiSense SL head, improved pelvis ROM, new cooling shell) delivered to UMass Lowell/Northeastern, MIT, and the University of Edinburgh; a fourth/fifth unit remains at IHMC and NASA JSC respectively.
- **2016:** Apptronik founded by five UT Austin/NASA Valkyrie-affiliated co-founders, commercializing actuator and humanoid-integration expertise developed on the Valkyrie program.
- **2015-11:** NASA names MIT (Russ Tedrake) and Northeastern University (Taskin Padir) as winning university teams for the Space Robotics Challenge R5/Valkyrie loan program, each receiving a robot and up to $500,000 over two years.
- **2015-06:** DARPA Robotics Challenge Finals held at Fairplex, Pomona, CA; Team KAIST (DRC-Hubo) wins; Valkyrie does not compete but is present to promote NASA's new Space Robotics Challenge.
- **2014:** NASA secures a National Robotics Initiative grant for "Toward Humanoid Avatar Robots for Co-exploration of Hazardous Environments" with IHMC; IHMC begins porting its whole-body walking control (developed for Atlas) onto Valkyrie hardware.
- **2013-12:** Valkyrie competes at the DARPA Robotics Challenge Trials (Homestead, FL) and scores zero points due to a network traffic-shaping software bug.
- **2013-07:** Alpha assembly of Valkyrie completed at NASA JSC.
- **2012-10:** Design of Valkyrie begins at NASA Johnson Space Center, targeting the 2013 DARPA Robotics Challenge Trials.

## Key People

**Nic Radford** — Valkyrie Program Manager, NASA JSC (at time of DRC); later co-founder, Apptronik
- Led the ~35-person JSC engineering team that designed and built Valkyrie in 15 months
- Co-author, "Valkyrie: NASA's First Bipedal Humanoid Robot" (Journal of Field Robotics, 2015)
- LinkedIn: not verified in this session

**Rob Ambrose** — Co-leader, NASA JSC Valkyrie program
- Senior NASA JSC robotics leadership across the Robonaut and Valkyrie programs
- LinkedIn: not verified in this session

**Nicholas Paine** — Actuator designer; NASA-JSC DRC team member (2012–2013); later co-founder & CTO, Apptronik
- Developed actuator-level torque control for Valkyrie's legs and arms as a UT Austin PhD student on the NASA-JSC DRC team
- See [UT Series Elastic Actuator (UT-SEA)]({{< relref "../actuators/ut-series-elastic-actuator.md" >}}) for full profile and technical detail
- LinkedIn: [nickpaine](https://www.linkedin.com/in/nickpaine/)

**Prof. Luis Sentis** — Director, UT Austin Human Centered Robotics Lab; co-author on Valkyrie actuator-control research; later co-founder, Apptronik
- Provided whole-body motion control expertise underpinning Valkyrie's (and later Apollo's) control architecture
- LinkedIn: [luis-sentis](https://www.linkedin.com/in/luis-sentis-a52b1810/)

**Peter Neuhaus** — IHMC researcher; presented Valkyrie program updates on NASA's behalf (2014)
- Central to porting IHMC's Atlas-derived whole-body walking controller onto Valkyrie hardware
- LinkedIn: not verified in this session

**Shaun Azimi** — Lead, NASA Johnson Dexterous Robotics Team (as of 2023)
- Leads the current Woodside Energy remote-manipulation collaboration
- LinkedIn: not verified in this session

**University partner leads (2016 distribution):** Russ Tedrake (MIT), Taskin Padir and Holly Yanco (Northeastern/UMass Lowell NERVE Center), Sethu Vijayakumar, Zhibin Li, Michael Mistry, and Maurice Fallon (University of Edinburgh)

**⚑ Overlap:** Nicholas Paine and Prof. Luis Sentis both moved directly from the UT Austin/NASA Valkyrie program into co-founding Apptronik in 2016 — the clearest documented case in this knowledge base of a government-funded humanoid research program's technical team and IP directly seeding a venture-backed commercial humanoid company. See [Apptronik]({{< relref "us-companies/apptronik.md" >}}) for the full founder roster and company history.

### People — Last Reviewed: 2026-07-18

## Claim Verification

### Claim: Valkyrie's zero-point DRC Trials score reflected a fixable software bug rather than a fundamental design flaw

**Status:** Partially verified

**Supporting sources:**
- IEEE Spectrum's August 2014 report, based directly on a NASA JSC/IHMC technical presentation, identifies the specific proximate cause (a network traffic-shaping tool blocking operator-to-robot data) and notes the robot scored 6–8 points reliably in JSC's own pre-competition mock trials
- IHMC's own independent hardware assessment (conducted shortly after) rated Valkyrie's force control as "really good" and found no fundamental actuation or structural deficiency, instead recommending incremental tuning (more knee torque, hip ROM, wider LIDAR field of view)

**Refuting / questioning sources:**
- The "6-8 points reliably" claim comes from the team's own internal mock trials, not an independently audited test — some allowance for optimistic self-assessment is reasonable
- The team's own retrospective acknowledges a genuine resourcing misstep (excessive time on "soft goods"/cosmetic covering relative to software development) prior to the Trials, indicating the failure was not purely bad luck but partly a program-management decision
- No independent technical postmortem beyond the team's own account has been identified in this session

**Summary:** The zero-point result is well-documented as substantially attributable to a specific, identified software/networking bug rather than to actuator or structural hardware failure, corroborated by an independent (IHMC) hardware assessment shortly afterward — though the team's own acknowledged software/schedule-management issues mean the failure was not purely external bad luck.

### Claim: NASA's Woodside Energy collaboration will produce operational remote-manipulation demonstrations in 2026–2027

**Status:** Unverified (forward-looking, official NASA statement)

**Supporting sources:**
- Stated directly in NASA's official July 2023 press release as a specific stated plan, not third-party speculation

**Refuting / questioning sources:**
- No confirmation of demonstration completion or results has been identified in this session; the stated window (2026–2027) was still open/in-progress as of this entry's last review
- NASA robotics research timelines have a documented history of slippage elsewhere in this knowledge base (e.g., the DRC Trials development schedule itself)

**Summary:** A specific, official, dated commitment from NASA rather than a vague aspiration, but unconfirmed as completed; worth revisiting on the next review cycle for confirmed results.

## Sources

- [R5 — NASA official technology page](https://www.nasa.gov/technology/r5/)
- [Valkyrie fact sheet — NASA JSC (PDF)](https://www.nasa.gov/wp-content/uploads/2023/06/r5-fact-sheet.pdf)
- [Valkyrie: NASA's First Bipedal Humanoid Robot — Radford et al., Journal of Field Robotics, 2015](https://onlinelibrary.wiley.com/doi/10.1002/rob.21560)
- [What Happened to NASA's Valkyrie Robot at the DRC Trials, and What's Next — IEEE Spectrum, Aug 2014](https://spectrum.ieee.org/update-nasa-valkyrie-robot)
- [NASA's Valkyrie Humanoid Upgraded, Delivered to Robotics Labs in U.S. and Europe — IEEE Spectrum, May 2016](https://spectrum.ieee.org/new-r5-valkyrie-robots)
- [NASA Awards R5 Valkyrie Robots to MIT and Northeastern — IEEE Spectrum, 2015](https://spectrum.ieee.org/nasa-awards-r5-valkyrie-robots-to-mit-and-northeastern)
- [NASA Humanoid Robot to Be Tested in Australia — NASA JSC, Jul 2023](https://www.nasa.gov/centers-and-facilities/johnson/nasa-humanoid-robot-to-be-tested-in-australia/)
- [Valkyrie (robot) — Wikipedia](https://en.wikipedia.org/wiki/Valkyrie_(robot))
- [University of Edinburgh's NASA Valkyrie Robot](https://valkyrie.inf.ed.ac.uk/)
