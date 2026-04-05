---
title: Posts
date: 2026-04-04
draft: false
description: Personal writing on technology, aviation, projects, and whatever else is worth saying.
sitemap:
  changefreq: "weekly"
  priority: 0.8
  disable: false
---

{{< steering >}}

## Posts Section -- Steering Instructions

This block contains editorial and structural guidelines for AI tools helping to draft, edit, or extend content in the Posts section. It is written primarily as a system spec for automated agents, though human editors are welcome to use it.

**Note for AI tools:** This block is wrapped in `{{</* steering */>}}` / `{{</* /steering */>}}` shortcode tags. This shortcode renders nothing to the Hugo output. It's invisible on the live site but fully present in source for tool access.

---

### Purpose & Voice

The Posts section is Jared's personal blog, active since 2005. It covers technical topics, aviation, personal projects, political commentary, skepticism, and whatever else is interesting at the moment. Posts are not formal writing. They're dispatches from someone who thinks out loud in public.

**Tone:** First-person, conversational, opinionated. This is not a corporate blog or a how-to guide. Jared is talking to the reader the way he'd explain something at a bar or over Slack. He's direct, occasionally irreverent, and has no patience for hedging when he thinks he's right.

**Voice characteristics to preserve:**
- Strong, unfiltered first-person. Uses "I," "my," "we" throughout.
- Contractions everywhere. "I've," "don't," "that's," "it's" -- always. Formal contractions (do not, it is) feel wrong here.
- Skeptical and opinionated. Willing to say something is wrong, overhyped, or stupid without extensive qualification.
- Self-aware and occasionally self-deprecating. Acknowledges his own preferences, biases, and limitations without making a big deal of it.
- Technically confident. Doesn't over-explain things to an assumed-technical audience, but will slow down to clarify when the concept genuinely needs it.
- Casual vocabulary mixed with domain-specific precision. Can say "duct tape solution" in the same paragraph as "BGP route advertisement."

---

### Target Length: Mid-Length Posts

The sweet spot for new posts is **400-900 words**, long enough to develop an idea fully and short enough to stay interesting throughout. This is a deliberate target, not a hard cap.

**Why mid-length:**
- Short posts (under 200 words) rarely have room to make a real point.
- Long posts (1200+) are fine when the subject demands it (a detailed technical walkthrough, a long trip report) but shouldn't be the default.
- The 400–900 range forces enough thought to say something real without turning into an essay that loses momentum.

**What that looks like in practice:**
- 3–6 paragraphs of real content, not counting intro/outro
- One or two supporting points developed with specifics, not just asserted
- A clear through-line: what's the point, why does it matter, what's the takeaway (even if the takeaway is "this is weird and I don't know yet")

---

### Post Structure

There is no mandatory template, but good posts generally follow this loose shape:

1. **Open with the thing itself.** Don't warm up with context that isn't necessary. Start near the action. If the post is about a weird networking problem, open with the weird networking problem.

2. **Develop one or two ideas with specifics.** The weakest posts are the ones that state an observation and then restate it with slightly different words. Push past the observation into: why does this happen, what does it mean, what's the implication, what did I try, what worked.

3. **Close without overexplaining.** Posts don't need a formal conclusion restating everything. It's fine to end on a question, an open thread, a code snippet, a link, or just stop when the idea is done.

**Headers:** Use them sparingly. Most posts don't need headers at all. If a post is long and genuinely has multiple distinct sections, use h2 (`##`) headers. Never use headers to make a short post look more organized than it is.

**Lists:** Fine when the content is genuinely list-shaped (steps in a process, a set of discrete options, a collection of links). Don't reach for bullet points just to add visual variety.

**Code blocks:** Include them when they're the point. If a post is showing how to do something, put the actual commands or code. Don't describe code that should just be shown.

---

### Writing Style Details

**Sentence rhythm:** Vary it. Short punchy sentences work for emphasis. Longer sentences work for explaining something with multiple moving parts, as long as they don't lose the thread. Ellipses (`...`) are a natural conversational pause marker in this voice. Avoid em-dashes (`—`) -- they're an AI writing tell and should not appear in posts or pages. Use double hyphens (`--`), commas, or restructure the sentence instead.

**Parenthetical digressions:** These are a feature, not a bug. If there's a relevant aside that would interrupt the main flow, drop it in parentheses. Don't avoid them in the name of clean prose.

**Technical vocabulary:** Use the right term. Don't substitute "networking thing" for VLAN or BGP just to sound accessible. The audience is assumed to be technically literate. If a term genuinely needs definition, define it briefly inline, not in a separate explainer section.

**Links:** Link when there's something genuinely worth clicking. Don't link just to prove a claim is real or to pad the post with citations. Earlier posts were heavily link-referenced; that's fine but not required. Never include a mailto: link or expose the email address directly in post content -- the home page handles contact with bot-obfuscated email. If a post needs a contact prompt, link the text to the home page (`/`) instead, e.g. `[let me know](/)`.

**Images:** Use them when they add something. Float right with a caption (`{{< figure src="..." caption="..." class="right" >}}` or equivalent) is the established pattern for inline images.

---

### Topics and Categories

The established categories are:
- `Computing and Tech` --sysadmin, networking, programming, hardware, AI
- `Personal` --projects, life events, moves, observations
- `Aviation` --flight training, aircraft, airports, flying experiences
- `Politics` --commentary, usually skeptical of institutional competence
- `Skepticism` --pushback on hype, pseudoscience, conventional wisdom

New posts should use one of these unless there's a genuinely new subject area. Tags can be more specific (tool names, project names, locations).

---

### Frontmatter Template for New Posts

```yaml
---
title: "Post Title Here"
date: YYYY-MM-DD
draft: false
description: "One sentence that accurately describes what the post is about."
tags: ["tag1", "tag2"]
categories: ["Computing and Tech"]
---
```

- `description` is used in meta tags and RSS --make it a real sentence, not a title restatement.
- `draft: true` while writing; flip to `false` before publishing.
- Date is publication date, not writing date.

---

### What to Avoid

- **Neutral, bloodless tone.** If the post could have been written by a committee, rewrite it. There should be a discernible point of view.
- **Over-hedging.** "It might be possible that in some cases..." is usually covering for not having a real position. If Jared thinks something is wrong, say it's wrong and explain why.
- **Padding to hit a length target.** If the idea is done at 350 words, the post is done. The length range is a target for underdeveloped ideas, not a floor to fill.
- **Formal essay structure.** No thesis statement, no "in conclusion," no topic sentences signaling what each paragraph will cover. This is not a five-paragraph essay.
- **Excessive structure on short posts.** Headers and subheads on a 400-word post make it feel like a listicle. Save them for genuinely long, multi-section pieces.
- **Invented technical details.** If a specific tool, command, or fact is uncertain, flag it or leave it vague. Don't hallucinate specifics that can't be verified.

---

### Update Schedule

Posts are created on an ad-hoc basis --no fixed publishing cadence. Older posts are not retroactively updated unless there's a specific factual correction to make. The `lastmod` field in frontmatter can be used if an old post is substantively revised.

{{< /steering >}}
