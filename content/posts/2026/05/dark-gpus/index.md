---
title: Let the (AI) Bodies Hit the Floor
date: 2026-05-07
lastmod: 2026-05-28
draft: false
description: The AI datacenter buildout is hitting a wall of physical constraints that echoes the late-90s dark fiber overbuild. But GPUs depreciate in months, not decades, and the US economy is strapped to the outcome.
tags:
  - ai
  - computing
  - datacenter
  - economics
  - infrastructure
  - investing
  - nvidia
  - tech
---

In 2001, an estimated 95% of all the fiber optic cable in the ground was dark. Telecom companies poured over $500 billion into it on the thesis that internet traffic was doubling every hundred days (it wasn't, but everyone believed it was), and WorldCom, Global Crossing, and Williams Communications took on enormous debt to lay fiber across oceans and under highways. It took nearly 20 years for traffic to grow into that capacity. Several of those companies went bankrupt. The fiber itself was fine, sitting patiently in the ground, waiting for demand to catch up.

The GPU version of this is already happening. And unlike fiber, GPUs don't wait.

<!--more-->

## The buildout that can't be built

The numbers are staggering on paper. Microsoft, Amazon, Google, and Meta have committed roughly $725 billion in AI-related capital expenditure for 2026 alone, up 77% from the prior year. The announced pipeline of US datacenter capacity for 2026 is somewhere around 12 to 16 gigawatts. That's a lot of zeros.

Here's the problem: only about a third of it has broken ground. Close to half of planned US datacenter builds for 2026 have been delayed or canceled, according to Sightline Climate. Not because demand evaporated (the checks are being written), but because the physical world has hard constraints that press releases don't.

The poster child is Stargate, the $500 billion joint venture between OpenAI, Oracle, and SoftBank that Trump personally announced in January 2025. More than a year later, the JV hasn't hired staff and isn't actively developing datacenters. The planned 600 MW expansion at the Abilene, Texas campus was canceled after negotiations broke down. Satellite imagery of the original 1,200-acre site shows six plots cleared, one with actual development. Oracle pushed delivery schedules for several large OpenAI facilities from 2027 to 2028, blaming labor and materials shortages.

But the construction delays aren't even the most interesting problem with Stargate. The money isn't real. SoftBank, the supposed primary financial backer, could only assemble 10% equity funding. The rest was going to come from debt. Their first $10 billion tranche was borrowed from Mizuho and other Japanese lenders. OpenAI tried to build its own datacenters but couldn't get financing because lenders weren't willing to back billion-dollar construction projects from a company losing $14 billion a year with no clear path to profitability. SoftBank eventually conditioned its investment on OpenAI restructuring into a public benefit corporation, or the commitment drops to $10 billion. The partners spent months arguing about control structure instead of breaking ground.

And then there's the circular financing, which is the part that should make anyone who remembers the telecom bubble really nervous. NVIDIA invested in OpenAI. OpenAI uses that money to buy NVIDIA chips. Oracle committed to spending $40 billion on NVIDIA GPUs to power Stargate's Abilene facility. OpenAI signed a $300 billion deal to buy Oracle cloud capacity. So NVIDIA funds OpenAI, who pays Oracle, who pays NVIDIA. The money goes in a circle. Bloomberg published a whole investigation into these arrangements, calling them what they are: AI circular deals where Microsoft, OpenAI, and NVIDIA keep paying each other.

This is vendor financing with extra steps. If you drew it on a whiteboard, a first-year business student would circle it in red. Somewhere in Cupertino and Redmond, very smart people are nodding at this chart and calling it a partnership ecosystem. In the late 90s, telecom equipment makers like Nortel and Lucent lent money to their customers so those customers could buy their products. It inflated demand numbers beautifully right up until the loans went bad and the whole thing collapsed. The AI version is more sophisticated (it's structured as equity investments, cloud commitments, and partnership agreements rather than simple loans), but the economic logic is identical. The demand looks enormous on paper because the same dollars are being counted multiple times as they circulate between a handful of companies. When actual external revenue has to support the structure instead of recycled internal capital, the math stops working.

Stargate isn't an outlier. It's the pattern.

To be clear, the fact that these companies are willing to spend this kind of money isn't irrational. The underlying demand signal for AI compute is real and growing fast. The problem isn't the bet. It's the mismatch between the speed of the financial commitments and the speed of the physical world.

## Everything bottlenecks at once

The constraint isn't any single thing. It's everything, simultaneously.

Large power transformers now have lead times of 128 to 144 weeks. That's two and a half to nearly three years. Prices are up 77% since 2019, and Wood Mackenzie projects a 30% deficit in power transformer availability for 2026. These aren't exotic components. They're the things that connect a datacenter to the electrical grid. Without them, nothing turns on.

HBM (the specialized memory that goes into AI accelerators) has demand growing 80 to 100% annually against supply growing 50 to 60%. Only three companies on earth make it. NVIDIA's Blackwell GPUs are sold out through mid-2026 with a massive backlog, and the company reportedly cut consumer RTX 50-series production significantly because the same memory capacity feeds HBM production lines. Datacenters will consume 70% of all memory chips produced worldwide in 2026.

Copper is at roughly $5.60 a pound and hit $6 earlier this year. A datacenter needs about 27 tonnes per megawatt of capacity. The same copper is being fought over by the renewable energy buildout that's supposed to power these same facilities.

And then there's the grid interconnection queue, which is the real binding constraint. You can have the land, the permits, the chips, and the money, but if you can't get power to the site, you have a very expensive, very well-permitted patch of dirt.

None of these constraints are permanent. Transformer manufacturing is scaling (Hitachi Energy, Siemens, and others are expanding capacity). HBM production is ramping. But "scaling" and "ramping" operate on industrial timelines. Tech leadership hasn't had to face that level of reality in recent decades. 

## Behind-the-meter won't save you

The industry's answer to the power bottleneck has been behind-the-meter generation: bring your own power plant, skip the grid entirely. It's a smart instinct, and it's the kind of creative problem-solving that eventually does work in infrastructure buildouts. But the near-term reality is messier than the pitch decks suggest.

Most BTM deals are centered on natural gas, with some nuclear restarts and fuel cell projects in the mix. AEP and Bloom Energy announced a 1 GW fuel cell deal (the largest utility-scale fuel cell procurement in US history). It hasn't delivered yet. Some of the announced deals read more like science fiction (space-based solar, small modular reactor designs that don't exist yet) with delivery timelines in the 2028 to 2030 range. That's not giving you near-term relief. Anything more than 3 years out feels more like hope than a plan.

The fuel cell angle deserves its own reality check. Bloom Energy and others talk about fuel cells as clean, flexible BTM power, and the technology is real. But hydrogen isn't an energy source. It's an energy carrier. Unlike natural gas, which comes out of the ground ready to burn, hydrogen has to be manufactured first, usually by electrolysis (running electricity through water) or steam methane reforming (which uses natural gas anyway, so what's the point). The round-trip energy efficiency of producing hydrogen, compressing it, and running it through a fuel cell is roughly 40%. You're losing 60% of the energy you started with before a single GPU turns on. (There is a version of this where the clean energy answer is just a very complicated way to burn natural gas less efficiently, and some of these announcements are basically that.) And that's before you deal with the storage and transport problems: hydrogen is the smallest molecule there is, it leaks through containment walls and pipe joints that are perfectly tight for other gases, it causes embrittlement in conventional steel (gradually weakening the metal until it cracks), it needs to be stored at extremely high pressures or cryogenic temperatures, and it's explosive across a wide range of concentrations in air. There is no industrial-scale hydrogen supply chain today, and building one is a decades-long infrastructure project unto itself. Fuel cells running on natural gas are more practical, but at that point you've built a less efficient gas turbine with extra steps.

Even the relatively conventional BTM projects (gas turbines, which are the most deployable option) face the same transformer and switchgear bottlenecks as grid-connected builds. Gas turbines produce AC at medium voltage. The next-gen AI racks they're supposed to power run on 400V to 800V DC. That means you still need the full power conversion chain between the generator and the rack: step-down transformers, rectifiers, and DC distribution infrastructure, all of which use the same components that are backordered for years. BTM doesn't eliminate the supply chain. It just changes who you're buying from. And the 800VDC ecosystem that NVIDIA's latest architectures require won't even be commercially available until the second half of 2026.

It also doesn't eliminate the community opposition problem, and may actually make it worse. Nobody loves having a datacenter next door, but a datacenter with its own gas-fired power plant raises environmental and permitting issues that a grid-connected facility doesn't. There are now 188 local opposition groups across 40 states. Over 300 state datacenter bills were filed in just the first six weeks of 2026. Maine enacted the first state-level moratorium on large datacenters. Virginia (home to 643 facilities) has a proposed moratorium halting all new applications until July 2028. Georgia's Senate is considering a one-year ban. There's even a federal moratorium bill now. While it's not expected to pass the sentiment against these projects is growing.

Behind-the-meter power isn't big enough and won't come online fast enough to rescue the near-term pipeline. And the local opposition is only getting louder.

## Dark GPUs are worse than dark fiber

Here's where the analogy breaks down in a way that makes the current situation more dangerous to the economy than dark fiber of the past.

Dark fiber sits in the ground. It doesn't rot. It doesn't become obsolete. It costs almost nothing to maintain once installed. The fiber laid in 1998 was still perfectly usable in 2015 when traffic finally grew into it. Patience was rewarded, even if the investors who funded the original buildout went bankrupt waiting.

GPUs don't work that way. A GPU that can't be powered or deployed today isn't going to sit on a shelf and be useful in three years. AI accelerator generations move on 18 to 24 month cycles. NVIDIA's Blackwell is already being succeeded by Rubin. The H100s that were the hottest commodity in 2023 are already being displaced. A chip produced today that can't be put to work has a shelf life measured in months before it's obsolete, not decades.

And this isn't hypothetical. It's already happening. Microsoft's Satya Nadella has said publicly that power, not compute, is their biggest datacenter constraint, and that Microsoft has AI GPUs "sitting in inventory" because it lacks the power to install them. In Santa Clara (literally minutes from NVIDIA's headquarters), two freshly built datacenters, Digital Realty's SJC37 and Stack Infrastructure's SVY02 campus, are standing empty because the local utility can't supply the electricity. They may sit empty for years. In Northern Virginia, the largest datacenter market in the country, connection delays are running multiple years as utilities struggle to reinforce high-voltage infrastructure. Regions in the Pacific Northwest and the Southeast are reporting wait times of two to five years for new power capacity.

So the dark GPUs aren't a future risk. They exist right now. NVIDIA keeps shipping chips. The datacenters keep getting built (or half-built). And the power to run them isn't there. Every GPU that sits in a warehouse or in a powered-down rack is depreciating toward obsolescence while the next generation rolls off the fab line.

The capital destruction isn't deferred. It's immediate. And it's compounding. Unlike fiber that sat dark but held its value, a GPU that misses its deployment window doesn't get a second chance. By the time the power arrives, the chip is last-generation and worth a fraction of what was paid for it.

This pricing reality probably isn't fully baked into the market yet, because the worst of the delivery failures are still 12 to 18 months out. The commitments have been made, the purchase orders are in, but the physical constraints haven't fully collided with the financial expectations. When they do, someone is going to be holding a lot of very expensive, very obsolete silicon.

## The subsidy cliff

There's a demand-side problem too, and it's related.

![](115Free.jpg#floatright "width=400")

OpenAI is projected to lose $14 billion in 2026 despite hitting $20 billion in annualized revenue and having 900 million weekly ChatGPT users. Ninety-five percent of those users don't pay.  The company's cumulative losses between 2023 and 2029 are projected at an eye-watering [$115 billion](https://www.cnbc.com/2025/09/06/openai-business-to-burn-115-billion-through-2029-the-information.html), (with a B) with profitability not expected until 2029 or 2030. That's a lot of subsidized usage.

Anthropic is doing better on unit economics (they reportedly hit $30 billion ARR while spending a quarter of what OpenAI spends on training), but the broader pattern holds across the industry: AI services are being sold below cost to build market share, and the bills are coming due. The era of $20-a-month plans that cost the provider $100-plus to serve is ending as these companies approach IPOs and investor patience thins.

When prices rise to cover actual costs, how much of current usage survives? A 2025 MIT study found that 95% of enterprise AI pilot programs failed to deliver measurable financial returns. Only 6% of organizations qualify as "AI high performers" (generating 5% or more EBIT impact) per McKinsey. Now, to be fair, those numbers deserve some nuance. Enterprise adoption of anything is historically slow, and a lot of those early pilots were running older models with teams that were still figuring out how to use them. It's not clear how much of that 95% failure rate reflects genuine limitations of the technology versus enterprises being bad at adoption (which they almost always are with new tools) versus a measurement problem where the ROI is real but shows up in places the study wasn't looking. The tools have gotten dramatically better even in the last twelve months, and the organizations that started early are probably seeing compounding returns that newer adopters haven't caught up to yet. But even granting all of that, the gap between the infrastructure investment and the demonstrable enterprise revenue is enormous, and it's the revenue that has to justify the buildout.

Sequoia Capital's David Cahn laid out the math starkly: take NVIDIA's GPU revenue, double it for total datacenter costs, double again for the margins end users need to justify the spending, and you get a $600 billion annual revenue requirement from AI services. The actual revenue is a fraction of that. That gap tripled in twelve months.

## The balance sheet problem

The hyperscalers funding this buildout are entering unfamiliar financial territory.

Historically, these companies spent about 40% of their operating cash flow on capital expenditure. In 2026, that number approaches 100%. Google's free cash flow is projected to drop roughly 90%, from $73 billion to around $8 billion. Amazon is expected to go free-cash-flow negative (Morgan Stanley projects negative $17 billion, Bank of America projects negative $28 billion). Microsoft's free cash flow drops an estimated 28%. Meta has $237 billion in non-cancelable contractual commitments.

These companies have always been valued partly on their enormous free cash flow generation. They didn't need to borrow. They self-funded everything. That's changing. Bank of America forecasts hyperscaler debt issuance will hit $175 billion in 2026, more than six times the annual average of the prior five years.

When tech companies that were valued like capital-light software businesses start borrowing like capital-intensive industrial companies, the market tends to re-rate them accordingly. Software companies trade at 25 to 35x earnings. Heavy industrials and utilities trade at 12 to 18x. If investors start pricing hyperscalers like the infrastructure-heavy companies they're becoming, the multiple compression alone wipes out trillions in market cap before a single revenue target is missed.

That said, these companies aren't utilities. They still have the advertising, cloud, and commerce businesses that generated the cash flow in the first place. The AI capex is an overlay on businesses that remain enormously profitable. The repricing risk is real, but it assumes the market ignores the base business entirely, which is the kind of overcorrection that creates buying opportunities as often as it creates crises.

There's a workforce trap buried in that repricing. These companies have built their compensation structures around stock. At Google, Meta, and Microsoft, stock-based compensation is a huge chunk of total pay, especially for the engineering talent they can't afford to lose during a buildout this complex. That worked beautifully when share prices climbed every year. But when multiples compress, stock comp stops being a retention tool and starts being a source of attrition. The employees who can leave, will. And the companies can't just replace stock comp with cash, because they've spent all their cash (and then some) on datacenters and GPUs. You end up in a situation where the people you need most to execute the buildout are the ones most likely to walk, right when you have the least financial flexibility to keep them.

And here's why that matters beyond tech investors: AI-related stocks now represent roughly 45% of S&P 500 market cap. Forty-one AI-linked stocks (about 8% of index constituents) account for 47% of the total index value and contributed 74% of the index's gains since ChatGPT launched. The S&P 500 isn't a broad market index anymore. It's a leveraged bet on AI monetization.

AI-linked investment-grade debt has climbed to $1.4 trillion, representing 15% of the US credit market. If the revenue doesn't materialize on schedule, the correction doesn't stay in tech. It cascades through every retirement account, every index fund, every pension plan that's passively allocated to the S&P 500.

## Crowding out the reindustrialization

Here's a dimension of this that I think is badly underappreciated: the AI buildout isn't happening in a vacuum. It's happening at the same time the US is trying to reshore semiconductor fabrication, battery manufacturing, and a whole range of industrial capacity that's been offshore for decades.

The numbers on that reshoring push are enormous. Since 2020, over $630 billion has been invested across 140 semiconductor projects alone, creating roughly 500,000 jobs in 28 states. TSMC is building a $100 billion campus in Arizona. Micron announced $200 billion across Idaho, New York, and Virginia. Total manufacturing construction spending hit $234 billion annually by mid-2024, up 217% from 2019. The IRA, CHIPS Act, and IIJA together authorized over $2 trillion in federal funding. This is the most ambitious industrial policy the US has attempted in generations.

And it needs the same stuff the AI buildout needs. The same transformers, the same switchgear, the same copper, the same grid interconnection capacity, the same skilled electricians, the same construction labor. A single TSMC fab phase requires around 200 megawatts of power. Multiply that across dozens of fabs, battery plants, and related industrial facilities, and you're talking about gigawatts of new industrial demand competing with the datacenter pipeline for grid capacity that doesn't exist yet.

The grid interconnection queue now exceeds 2,100 gigawatts, which is more than the total installed capacity of the US grid. Everything is in line: datacenter projects, semiconductor fabs, battery plants, solar farms, wind farms. The queue itself has become the bottleneck, and the datacenter buildout is the 800-pound gorilla in that line.

The labor competition is just as bad. The datacenter construction industry faces a projected shortfall of up to 500k workers. TSMC's Arizona fab was delayed six months largely because of skilled labor shortages, with Intel and other fab builders competing for the same pool of certified electricians and mechanical specialists. Construction unemployment hit a record low of 3.2% in August 2025. There's no reserve workforce to absorb simultaneous megaproject buildouts across multiple industries.

What this means in practice is that every datacenter project that outbids an industrial project for transformers, power capacity, or construction crews is directly slowing down the reshoring effort. And the datacenter operators have deeper pockets. Hyperscalers can pay whatever it takes for a transformer allocation or a power interconnection because they're spending hundreds of billions this year. A midsized semiconductor equipment supplier or battery plant builder can't compete with that.

Data for Progress polling in early 2026 found that more than two-thirds of voters support new manufacturing, housing, and clean energy projects in their communities. Support for new datacenter development sits at 48%. People want the factories. They're less sure about the datacenters. And the datacenters are eating the supply chain alive.

If the AI buildout stalls and the capital turns out to have been misallocated, the damage isn't limited to tech company balance sheets. It will have crowded out and delayed the industrial projects that were supposed to reduce American dependence on foreign supply chains. That's a strategic cost that goes well beyond stock prices.

## The employment squeeze

And all of this is happening alongside a labor market disruption that's already underway and accelerating.

Companies are cutting jobs in anticipation of AI's impact, not because AI has actually proven it can replace those jobs. Harvard Business Review reported in January 2026 that firms are laying off workers based on AI's potential, not its demonstrated performance. Fifty-five thousand job cuts were directly attributed to AI in 2025, with another 32,000 in the first two months of 2026. One in six employers expects AI to reduce headcount this year.

The irony is thick: the same AI that isn't generating enough revenue to justify its infrastructure costs is already being used as justification for layoffs. Gartner predicts that by 2027, half of the companies that attributed headcount reductions to AI will rehire for similar functions under different titles, having overestimated what AI could actually do. But that's cold comfort to the people being let go now.

Looking further out, the World Economic Forum projects 23% structural labor market churn through 2027, with a net loss of 14 million jobs globally. The introduction of capable, affordable robotics in the three to six year timeframe will sharpen this considerably, extending AI displacement from knowledge work into physical labor.

## Where this all lands

What makes this moment different from a normal correction is that everything is converging at once. The physical buildout is stalling (transformers, power, chips, community opposition). The demand is softer than projected (subsidies ending, enterprise ROI still unproven at scale). The financial engineering is reaching its limits (free cash flow consumed, debt replacing equity, circular financing inflating demand numbers). The stock market is concentrated enough that a tech repricing ripples through every index fund and pension plan in the country. The labor market is absorbing AI-driven cuts based on hype rather than demonstrated capability. And the whole thing is competing for resources with the reindustrialization effort that's supposed to reduce American dependence on foreign supply chains.

Let me try to put a timeline on how this plays out.

Late 2026 through mid-2027 is when the first wave of delivery failures becomes undeniable. The datacenter projects announced in 2024 and 2025 with 18 to 24 month timelines start missing their dates in volume. GPUs pile up in warehouses and unpowered facilities. The gap between announced capacity and operational capacity widens visibly. Hyperscaler earnings calls start featuring uncomfortable questions about returns on AI capex. The token factory companies (OpenAI, Anthropic, and the rest) face real pressure to raise prices as investor patience wears thin, and usage numbers start revealing how much of current demand was price-sensitive.

2027 through 2028 is when the financial consequences arrive. If hyperscaler free cash flow stays near zero or negative for multiple quarters, the market will reprice these companies. A shift from software-company multiples (25 to 35x) toward industrial multiples (12 to 18x) on companies that represent 45% of the S&P 500 would be a multi-trillion dollar repricing event. Stock-based compensation loses its pull, talent starts moving, and the companies can't replace it with cash they don't have. Credit markets tighten on AI-linked debt (currently $1.4 trillion). Meanwhile, the reindustrialization pipeline is two to three years behind schedule because the datacenters ate the transformers, the construction labor, and the grid interconnection capacity.

2028 through 2030 is where the employment picture gets sharp. By then, the AI tools will have matured enough (and the robotics will have arrived in early commercial form) that the job displacement moves from anticipatory layoffs to structural replacement. The companies doing the replacing will be under financial pressure themselves, creating a strange dynamic where firms cut headcount to save money on labor while simultaneously spending more on AI infrastructure that isn't paying for itself yet.

The aggregate impact? If even half of this plays out on the timeline I'm sketching, you're looking at a meaningful drag on US GDP. Not a recession caused by AI directly, but a combination of suppressed capital investment returns, stock market wealth destruction concentrated in the indices that most Americans are exposed to through retirement accounts, a delayed reindustrialization that leaves supply chain vulnerabilities unaddressed, and labor market disruption hitting both white-collar and (eventually) blue-collar workers simultaneously. The 2000 to 2002 tech correction erased about $5 trillion in market value and contributed to a mild recession. The current AI exposure is larger in both absolute and relative terms.

I've tried to be fair to the counterarguments throughout, because they're real. The engineering talent being thrown at these constraints is world-class, the financial incentives to solve them are enormous, and the history of technology consistently embarrasses people who bet against human ingenuity on long enough timescales. I don't think this is a bubble in the sense that the underlying technology is fake. I think it's a buildout that's outrunning its own supply chain and revenue base, and the correction when those things catch up will be painful.

The question isn't whether AI will be transformative. I think it will. The question is whether the timeline of the buildout matches the timeline of the revenue, and what happens to the US economy during the gap between the two. The dark fiber era took twenty years to resolve. The companies that laid the fiber went bankrupt, but the fiber itself eventually became the backbone of the modern internet. With dark GPUs, the hardware won't wait. The chips depreciate, the architectures move on, and the capital is gone. If there's a resolution, it has to come faster than twenty years, because the assets don't have twenty years in them. And I don't think anyone knows the answer yet.

---

## Predictions vs. Reality

*The original post above doesn't get edited as evidence comes in. This section does. New entries go here as the predictions play out.*

---

### Update: May 2026

I wrote that the token factory companies would face real pressure to raise prices as investor patience wears thin, and that usage numbers would start revealing how much demand was price-sensitive. I put that in the late 2026 to mid-2027 window. It's showing up now, and it's coming from the demand side first.

Microsoft canceled most of its internal Claude Code licenses in mid-May. The affected engineers, in the Experiences and Devices division, have until June 30 to migrate to GitHub Copilot CLI. The reason isn't capability. It's that agentic coding tools burn tokens at rates that are orders of magnitude above single-query LLM use, and the per-engineer monthly bills were running $500 to $2,000. Multiply that across a division at Microsoft scale and it stops penciling out.

Sit with that for a second. Microsoft. The company that bet its cloud franchise on Copilot, that's directly invested in OpenAI, that's been the loudest enterprise AI evangelist in the industry. Pulling back on AI tool licenses inside its own engineering org. If the economics don't hold for the company selling this stuff, the pitch to enterprise customers has a credibility problem.

Uber's story is sharper. The CTO disclosed that Uber had exhausted its entire 2026 AI coding tools budget by April. The whole year's budget. In four months. And there's a detail in there that's worse than the number: Uber said token consumption didn't appear to correlate reliably with useful product output. So they weren't even getting value proportional to what they were spending. They were just burning tokens.

This is the subsidy cliff, but from the buyer side. Not providers being priced too low (though that's also true), but enterprises discovering that agentic workflows cost dramatically more than anyone forecasted when "token spend" was still an abstract line in a planning doc rather than a real invoice.

It's not just these two. A [Mavvrik survey](https://www.mavvrik.ai/blog/ai-cost-statistics-2026/) found 85% of companies missed their AI cost forecasts by more than 10%, and 84% saw gross margins drop more than six points. One healthcare company consumed a trillion tokens over six months and racked up more than $6 million in unplanned costs before anyone in finance figured out what was causing the spike. Amazon had an internal "tokenmaxxing" problem where employees were inflating AI usage metrics by using tools for unnecessary tasks (which is a very human response to being measured on a proxy metric, and also completely useless to the business).

Goldman Sachs put out a forecast that agentic AI could drive a [24-fold increase in token demand by 2030](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-begin-to-bite-as-agents-may-increase-token-demand-by-24-times-says-goldman-sachs-report-uber-and-microsoft-among-companies-feeling-the-bite-of-tokenized-billing). That's the bull case for the infrastructure buildout. It's also a problem for near-term revenue if enterprises are already pulling licenses at current token consumption levels. The demand expansion Goldman is forecasting assumes someone will pay for all those tokens. The evidence from May 2026 is that enterprises are not enthusiastic about that.

On the ROI side, the numbers have gotten worse since I cited the 2025 MIT study. McKinsey's 2026 survey puts the failure rate at 73% of AI projects not delivering intended business value. IBM finds only 25% of AI initiatives delivering expected ROI. Morgan Stanley says only 21% of S&P 500 companies can point to any measurable AI benefit at all. Token prices have fallen roughly 280-fold over two years, and total enterprise AI spending rose 320% in the same period. Cheaper tokens don't reduce the bill. They expand consumption until something structural pushes back. Right now that structural pushback is a CFO asking why the engineering department blew its annual AI budget before Q2 ended.

I said the subsidy cliff would become visible in late 2026. It's visible now. The first people going over it are enterprise buyers who got a real invoice, which is a problem for OpenAI and Anthropic specifically, since enterprise contracts (not the $20/month consumer plans that cost more to serve than they charge) are supposed to be the revenue base that eventually makes the unit economics work.
