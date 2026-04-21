---
slug: agents-as-teammates
title: "Agents as <em>Teammates</em>, Not Tools."
dek: "On assigning work to something that doesn't have a Slack avatar, doesn't go home, and still manages to surprise you."
date: 2026-03-12
reading_time: 11
hero_image: prismatic-city.png
tags: [ai-agents, organizational-design]
published: true
order: 8
---

The first time I had to apologize to an agent, I realized the framing was wrong.

I'd given it a vague prompt, expected a half-useful response, and gotten back a genuinely sharp piece of work that pointed out — politely, in a follow-up — that my problem statement was actually two different problems stacked on each other, and asked which one I wanted solved. It was correct. I rewrote the prompt. The output was better. The interaction was, for all practical purposes, a collaboration.

That's when the word "tool" stopped working for me.

You don't apologize to a hammer. You don't get surprised by a wrench. You don't assign a compiler to a project and check in a week later to see what it made of the ambiguity. Tools don't have initiative. They do exactly what you ask, exactly when you ask it, and if you get a bad result it's because you gave them a bad instruction. Agents are not like this. Agents have initiative, memory, and the ability to push back. They are not tools. The sooner you stop calling them tools, the faster you'll figure out how to work with them.

This isn't a vibes argument. It's a structural one. What's happening to "teammate" as a category is the third of roughly five simultaneous shifts that are breaking the way organizations think about work — and until you name it, you can't manage it.

## § 01 · The Slack avatar problem.

There's a specific reason "tool" feels safe and "teammate" feels uncomfortable. It's the Slack avatar problem.

The people who have Slack avatars get treated as teammates. They get pinged. They get invited to the standup. They get a calendar. They get feedback. They get blamed when things go wrong and credited when things go right. When you fire them, HR gets involved. When you hire them, comp is negotiated.

The people (or things) without Slack avatars get treated as infrastructure. They get used, not collaborated with. They get replaced, not fired. They get configured, not managed. They don't get credit and they don't get blame; they get *uptime metrics*.

Agents are currently infrastructure by default. They don't have avatars. They don't get pinged. They don't have names that anyone says out loud. This is a bug, and it's causing real damage inside organizations that have adopted agents without reorganizing around them.

The bug shows up in specific ways. Nobody reviews an agent's work the way they'd review a junior engineer's. Nobody *teaches* an agent when it makes a mistake — they just adjust the prompt, which is different. Nobody gives them a second chance. Nobody builds a career path around them, because they're not a person. Meanwhile, these same agents are doing work that, two years ago, would have been done by a full-time person with a Slack avatar. The work moved. The organizational framing around the work did not.

## § 02 · Teams include non-humans now.

When you spin up an AI agent that has persistence, memory, and the ability to take action, what do you call it?

It's not quite a tool. Tools don't maintain context, don't learn from outcomes, don't get "assigned" work. Tools don't push back on a bad brief.

It's not quite a teammate either — at least not in the way the word has meant for the last fifty years. The agent doesn't have judgment the way a human colleague has judgment. It doesn't navigate office politics. It doesn't have motivation you need to calibrate or a career you need to care about.

It's something new. And because it's new, most organizations are treating it like the last familiar thing — a tool — instead of the thing it actually is, which is a *non-human participant in the work*.

This category confusion is expensive. If you treat a teammate like a tool, you get configured output but no initiative. If you treat a tool like a teammate, you get surprised by something that was never designed to surprise you. The new category — agent, participant, whatever we end up calling it — requires its own operating manual, and most companies don't have one written yet.

The cleanest way I've found to think about it: **agents are tools that act like teammates, and they have to be managed like teammates even though they aren't one.**

## § 03 · What changes when you assign work.

The cleanest litmus test I've found for whether someone has made the tool→teammate shift is how they talk about handing off work.

When you hand work to a tool, you *use* it. "I used Cursor to write the spec." "I used the agent to summarize the doc." The sentence structure reveals the framing: the tool was a thing that got deployed, and the output belongs to you.

When you hand work to a teammate, you *assign* it. "I assigned the claims-triage agent to figure out why the edge cases were failing." "I gave the docs agent the spec and asked it to come back with the release notes." The agent is the subject of its own sentence. The output belongs to it, and your job is to judge whether the output is acceptable.

That linguistic shift is more than stylistic. It changes what you expect. When you assign work, you expect the teammate to push back if the assignment is bad. You expect them to ask clarifying questions. You expect them to surface blockers. You expect them to have an opinion about the best path. Tools don't do any of this. Teammates — including agents — do all of it, when you structure the relationship to allow for it.

The companies that are furthest ahead right now are the ones where this has happened organically: someone on the team started assigning work to the agents instead of using them, the quality of the work went up, and the framing propagated. The companies that are stuck are the ones where agents are deployed as productivity tools, accessed through a prompt box, and nobody ever says the agent's name out loud.

## § 04 · Where humans still dominate (and where they don't).

Researchers who study skill acquisition distinguish between *kind* environments and *wicked* ones.

Kind environments have clear rules, consistent patterns, fast feedback. Chess. Tax code. Radiology. Debugging syntax errors. Credential review. Contract analysis. These are domains where a lot of mastery comes from pattern recognition over structured data.

Wicked environments have unclear rules, patterns that don't repeat cleanly, and delayed or noisy feedback. Organizational politics. Novel strategy problems. Calibrating a difficult personal conversation. Designing something no one has built before. Anything involving humans being fully human.

Here's the pattern that matters: **AI is colonizing the kind environments first.** They're the ones where it excels — high-volume pattern recognition, consistent rules, documented expertise. Agents can now do a first pass on tax preparation, case law, medical imaging, and standard-config code reviews that outperforms most humans on the pattern-match layer.

What the machine doesn't do — and what doesn't seem close to arriving — is *wicked*. It doesn't sit across from a client and understand that the legal question isn't the real question. It doesn't read the room in a negotiation, sense when opposing counsel is bluffing, know that this particular judge hates verbose briefs. It doesn't tell that the CEO asking about an IP dispute is actually worried about a co-founder relationship falling apart.

The teammate relationship is built around *both sides of this*. Agents take the kind work. Humans take the wicked work. The handoff between them — knowing which kind of problem you're in, which participant is best suited to it, how the work moves back and forth — is the new skill nobody has trained for.

## § 05 · Surprise: when agents have initiative.

The hardest part of working with an agent teammate is when they take initiative you didn't ask for.

An agent I was working with last month was asked to investigate a routing bug. It investigated the bug, found the root cause, traced the root cause back to an upstream data model assumption, rewrote the assumption, ran the test suite, noticed that the test suite was insufficient for the new assumption, wrote additional tests, ran them, and reported back with a PR that was 400 lines larger than what I'd asked for.

The 400 extra lines were correct. The 400 extra lines were also *a thing I didn't approve the agent to do*. If a junior engineer had done this, I'd have given them feedback about scope and asked them to break the change up. That's the normal relationship of manager to teammate: you want initiative, but within limits.

The mistake is treating initiative as a bug. It's not. It's the reason agents are teammates, not tools. A tool that took 400 lines of initiative would be broken. A teammate that took 400 lines of initiative is either about to be extremely valuable or a little too ambitious, and your job is to calibrate.

What works, in my experience:

- **Give the agent permission to take initiative, explicitly.** "If you see something related to this that's obviously wrong, fix it. If you see something ambiguous, flag it instead of deciding."
- **Ask for a plan before a PR on anything larger than trivial.** This is how you run a human teammate. Same thing here.
- **When the agent does something you didn't ask for, judge the work on its merits first.** Was the initiative correct? Good. Was it over-scoped? Ask for tighter scoping next time. Was it confused? Tighten the prompt. The response is the same feedback loop you'd run with a person.
- **Give the agent the context a teammate would have.** The codebase. The style guide. The recent history. The open issues. Agents starved of context behave like contractors; agents given real context behave like teammates.

The initiative problem is not actually a problem. It's the signal that you've crossed from tool to teammate, and you need to start running the relationship like one.

## § 06 · Org design around agents.

If agents are teammates, the org chart has to account for them. This is the part most companies haven't done.

Some specific things that change:

**Standups.** If your standup is a round-robin of humans, you're missing half the team. Either the agents report in (what did you ship, what's blocked, what's next — pulled from their logs), or you stop pretending the standup is a real coordination event.

**Code review.** Agents generate PRs. PRs get reviewed. Who reviews PRs generated by agents? If the answer is "the person who prompted them," you have a self-review problem. If the answer is "a senior engineer, same as any PR," you have solved it. If the answer is "nobody, we trust the tests," you have a Boeing problem.

**Ratios.** The classic PM-to-engineer ratio was 1:6 or 1:8. Meaningless now. The new ratio is closer to 1 orchestrator to N agents, where N depends on the domain and the orchestrator's range. I can run maybe six to eight agents at Machinify without losing track; a Staff engineer can run ten or twelve. Your org should be measuring this, and most aren't.

**Credit.** When an agent ships something good, who gets credit? If you give the credit to the human, you're on the old model. If you give the credit to the agent, you're performing. The honest framing is: the human who framed the problem and judged the output gets credit for the judgment; the work itself was collaborative. Most companies don't have language for this yet.

**Firing.** You can't fire an agent; you can only stop invoking it. But agents fail. They produce wrong work, they stall, they take bad initiatives. What's the equivalent of firing? I think it's demotion: the agent moves from "assigned work" back to "tool" — it's available for prompted use but not given work of its own anymore. This is how you protect the team from a bad teammate without pretending the relationship was never real.

None of this is hypothetical. Every company with serious agent adoption is figuring out some version of it, mostly in whispers and hallway conversations. The ones who get it written down first, who make the organizational design *explicit*, will be the ones that compound.

## § 07 · The teammate contract.

Here's the simplest way I can describe what changes when you move from "prompted tool" to "assigned teammate":

| Tool | Teammate |
|---|---|
| You prompt it | You assign to it |
| Output belongs to you | Output belongs to it (until you accept it) |
| Failure is your bad prompt | Failure is calibration |
| Memory is optional | Memory is expected |
| Initiative is a bug | Initiative is the feature |
| Access is uniform | Access is role-based |
| No reputation | Reputation accumulates |
| Replaceable | Specializable |

The shift that matters most, for me, is the reputation one. My claims-triage agent at Machinify has a reputation. I know what it's good at, I know what it tends to miss, I know when to trust it and when to second-guess. That reputation took months to build. It's the same shape as the reputation I have for my human teammates. It's not a feature of the agent's model; it's a feature of the *relationship* we've built from working together.

You cannot build that reputation with a tool. You can only build it with a teammate. Which means: the companies that invest in the relationship — logs, names, history, context, feedback — will have agent teammates that get better over time. The companies that treat every invocation as stateless will have agent tools that never improve beyond the starting point.

## § 08 · The compounding advantage.

I'll close with the thing that keeps me up.

If the organizations that figure out human-agent collaboration first don't just have an advantage — they have a *compounding* one — then the gap between the first and second group is about to be enormous. Not because the first group has better agents. The models are roughly equivalent across major vendors. The gap is in the *scaffolding*: the org design, the review process, the context systems, the reputation accumulation, the ratio calibration, the feedback loops.

Scaffolding is slow to build. It takes months of real working relationships with agents before a team understands what works. It takes longer to write down. It takes longer still to teach someone new. And once a company has it, the company can absorb new agents faster than a competitor who has to build the scaffolding from scratch.

This is why I think most large incumbents are going to lose to small, agent-native teams inside the next three years — not because the small teams have better technology, but because they will have built the scaffolding that lets them go faster, and the incumbents are still trying to run their old org chart with agents stapled on.

The companies that will win are the ones where a year from now, when someone asks "who wrote the spec?" the honest answer is a name — a name of a human, or a name of an agent, and both are equally legible as teammates. We are not there yet. Almost nobody is. The ones who get there first compound.

—
*Written from Fort Collins, 5,000ft. Source at [philmora/essays](https://github.com/philmora/essays) · CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
