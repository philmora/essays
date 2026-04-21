---
slug: the-pm-is-dead
title: "The PM Is Dead. <em>Long Live the Builder.</em>"
dek: "Something broke in the last six months. Not broke in a bad way — broke like a dam breaks. Everything that was building up behind it is now rushing through."
date: 2026-04-15
reading_time: 14
hero_image: cosmic-journey.png
tags: [ai-agents, product, future-of-work]
published: true
order: 8
---

Something broke in the last six months.

Not broke in a bad way. Broke like a dam breaks — everything that was building up behind it is now rushing through.

OpenClaw went from zero to 135,000 GitHub stars in weeks. Jensen Huang called it "the operating system for personal AI." Shopify's CEO told every employee to prove AI can't do the job before requesting a single hire. A PM I follow on LinkedIn built three working prototypes last Tuesday before lunch — no engineering team involved.

And here I am at Machinify, watching this play out inside one of the most complex domains in enterprise software. Healthcare payments. Billions in claims. Agents that are no longer hypothetical participants in the work — they're on the team.

The thing I keep coming back to: the job I'm doing today barely resembles the job I was doing eighteen months ago.

Here's what changed.

## § 01 · The dam that broke.

For a decade, product management was roughly one thing: **translation**. Translate from customer to engineer, engineer to exec, exec to roadmap, roadmap back to customer. Most of the artifacts — specs, PRDs, roadmaps, decks — were translation devices. They weren't the product. They were the explanation of what the product was going to be, written so that the people who would actually build it didn't have to hold the whole picture in their head at once.

That translation layer was expensive. It was also the thing most PMs were *hired* for. Good PMs wrote good translation. Great PMs wrote translation that survived contact with reality. But the translation itself was overhead. Every PRD was a bill the business paid to convert ambiguity into specification, and the specification into something an engineer could act on without having to go re-ask the question.

The thing that broke, six months ago, is that **the cost of translation went to near zero**. Not because anyone fixed meetings. Because agents can now do the translation — from ambiguous intent to code, from code to release notes, from release notes to stakeholder emails — at a cost that rounds to a rounding error. Give a capable agent a problem statement, a codebase, and an hour, and you'll get back a spec, a design, a first cut of the implementation, and a draft of the Slack announcement.

When the cost of building dropped to near zero, **the cost of building the wrong thing became the only cost that matters**. That changes what product people are for.

I want to be clear about what I'm *not* saying. I'm not saying product management is dead. I'm not saying PMs are being "replaced by AI" — that framing is lazy and it's going to age badly. What I'm saying is that the *translation layer* — the 60% of a PM's week that involved converting ambiguity into documents — just got commoditized. And the job was mostly that layer. The judgment that sat on top of the translation is more valuable than ever. It's just not the same job.

## § 02 · Two futures. Pick one.

On one side of the split: the PM who still believes the job is writing documents and managing backlogs. This person is in trouble and usually doesn't know it yet. Not because documents don't matter — they do — but because the meta-skill of writing documents has been commoditized, and if that's the core of your value proposition, you are competing with a thing that costs nothing and works at 4am.

If you ask these PMs what they did this week, the answer is a list of artifacts. "I wrote the Q3 strategy doc. I updated the roadmap. I ran three stakeholder reviews." All of that work is real. Some of it is even hard. But none of it is unique to them anymore. The strategy doc can be assembled from the data. The roadmap can be generated from the commits. The stakeholder review can be synthesized from the system logs. The work survives. The *person* writing it doesn't have to be you.

On the other side: the PM who realized a year ago that **the artifact was never the job**. The job was judgment. The artifact was just the vessel the judgment fit into. If you can get judgment out of your head and into the system some other way — by orchestrating agents, by prototyping directly, by pairing with a builder-teammate — the document becomes optional. Sometimes unnecessary. Occasionally a liability.

If you ask these PMs what they did this week, the answer is a list of *decisions*. "I killed a feature we'd already scoped because the data said nobody wanted it. I rewired the agent pipeline to pull from the new identity graph. I wrote the prompt that replaced the four-person QA team. I called the meeting where we decided to stop shipping and start refactoring." They barely wrote any documents. They made the business move.

These two people are not going to end up in the same place. The first is being automated away on a timeline measured in quarters. The second is doing work that *didn't exist* two years ago, and the comp for that work is going in a direction that is embarrassing the comp bands of the first group.

The gap between the two is mostly disposition. It's not credential, it's not tenure, it's not domain. It's whether you were willing to sit down and learn how the new tools actually work, and whether you were willing to let go of the identity of "person who writes excellent documents."

## § 03 · What the builder-orchestrator actually does.

I want to be careful here because this phrase is already being used to mean nothing. Let me be specific about what I actually do on a Tuesday at Machinify, where my job title still says "Sr. Director of Product" but the work bears less and less resemblance to what that title meant in 2023.

1. **I set the goal in plain English.** "This claim should route to the right queue 95% of the time, the other 5% should show me why they failed." That's the prompt. The prompt is the spec.
2. **I decide which agent gets the work.** Our platform has specialized agents — claims triage, policy lookup, provider matching, appeals. Deciding which agent is the right call is product judgment, not orchestration trivia. Pick wrong and you waste a week. Pick right and the work is done in a day.
3. **I watch the first run.** Agents surface their reasoning. I read it. If they're off, I adjust the frame. If they're on, I move to the next one. This is the part of the job that looks most like old product management — you're evaluating whether a first cut matches your model of the problem.
4. **I judge the output.** This is the part that cannot be outsourced. Did the agent get it right? Is the failure mode acceptable? Does this match the real-world decision we'd make? That's the job. An agent will confidently produce a wrong answer. My job is to catch it before it ships to 160 million lives.
5. **I ship.** Push to the cluster. Flag for human review. Monitor. When the metrics move, we learn. When they don't, we learn faster.

Notice what's missing from that list: *writing a spec*. The PRD isn't dead — but its *audience* changed. It's not a communication artifact for humans anymore; it's context for agents. The clearer your spec, the better your agent output. Ironically, the PM skill of writing precise requirements matters more now — you're just writing for a different reader.

Notice also what isn't missing: judgment about what matters, taste for what good looks like, pattern recognition across a long history of shipping things, the ability to say no fast. All of that got *more* valuable, not less. An agent is happy to confidently generate the wrong answer at scale. The meta-skill of catching that is the whole game now.

The other thing worth noting: I'm doing roughly 4x the product decisions per week that I was doing two years ago. The ratio of judgment-to-overhead inverted. I used to spend 80% of my time generating artifacts and 20% of my time on the decisions those artifacts were supposed to serve. Now it's flipped, and the week feels like it has oxygen in it for the first time in a decade.

## § 04 · The ratio that's about to invert.

The PM-to-engineer ratio was 1:6 or 1:8 for most of the last decade. I've seen credible people argue it's about to go 2:1, maybe further. I don't know if the exact math is right, but the direction is obvious.

When every engineer has 10x leverage from AI coding tools, the bottleneck stops being "how fast can engineering ship?" and starts being "how fast can we figure out *what's worth shipping?*" That second question is the product question. And the answer, at scale, requires more people doing the product job — not fewer.

This isn't a new phenomenon. It's the same pattern every time a production bottleneck opens up. When the cost of manufacturing fell, the bottleneck moved to design. When the cost of distribution collapsed, the bottleneck moved to marketing. When the cost of coding drops to near zero, the bottleneck moves to *what to build*. That's the product job, and it's about to get a lot bigger.

The PMs who survive this transition aren't going to be the ones with the best Jira hygiene. They're going to be the ones who can:

- Hold the whole system in their head while agents do the typing.
- Prototype in an afternoon what used to require a sprint.
- Write prompts that produce production-grade output.
- Know when the agent got it wrong — and why.
- Design the guardrails, not just the features.

That last one matters more than anyone has fully internalized yet.

## § 05 · Agents need governance, not just configuration.

This is the part most people haven't figured out.

When you have agents taking action autonomously — making decisions about claims processing, flagging anomalies, routing work, talking to customers — you need more than a good prompt and a tested model. You need **guardrails, escalation paths, feedback loops, audit trails, and a theory of when humans intervene.**

That's not engineering work. It's product work. It's just not the product work we trained for.

The PMs who figure this out first become the only ones capable of running agent-native teams at scale. Everyone else is going to be either (a) too scared to deploy agents, or (b) deploying them with a configuration mentality and getting burned when something goes sideways at 2 AM.

What governance actually looks like, in practice:

- **Escalation by confidence.** If the agent's confidence drops below X, route to a human. Calibrated per use-case. Monitored weekly.
- **Reversibility by default.** Any agent action that affects the real world gets a rollback path. Agents that take irreversible action without human confirmation are bugs.
- **Reputation tracking.** Each agent has a trust score that accumulates. Agents with high scores get more autonomy; agents that fail get demoted back to "suggestion mode."
- **Feedback loops to the prompt.** When an agent fails, the failure becomes training for the prompt. Not just "try again" but "here's what I actually wanted."
- **Audit trails that a human can read.** If something goes wrong, you need to be able to answer "what did the agent decide, and why?" without reading 400 pages of JSON.

None of this is part of any PM job description I've ever seen. All of it is the job now.

## § 06 · The casualties.

Here is what I think is going away, and soon:

- **PRD season.** Biweekly spec review meetings. The Confluence page that has been through nine stakeholder rounds and still isn't the product.
- **The PM whose main output is a document deck whose main output is another deck.**
- **The "alignment meeting."** You don't need to align fourteen people around a doc if the doc writes itself from the system state and everyone can query it directly.
- **The roadmap as fiction.** A quarterly plan written to give the illusion of control, when in practice the plan changes every two weeks. When prototyping is free, the roadmap is a rolling bet you re-place weekly.
- **The "product requirements review" as a ritual.** It becomes a 20-minute standup. The agents already wrote the requirements; you're just checking the framing.

Here is what I think is getting *more* valuable, not less:

- **Judgment about what to build, not what to describe.** What problem is worth solving this quarter?
- **Taste.** Does this feel right? Agents will optimize a metric into a bad product; humans still have to notice when the thing is ugly or dishonest.
- **The ability to hold the whole system in your head.** If you can't see the dependencies, you'll route work to the wrong agent and lose a week.
- **Writing well — because your prompts are now your product.** The PM who can't write a clear sentence can't prompt a clear result.
- **Speaking to engineers as peers.** Agents do the typing. Engineers do the architecture. PMs who can't tell the difference are about to get stuck.
- **Having shipped actual code at some point in your life** so you know what's cheap and what's not. The PMs who came up through engineering have an unfair advantage right now, and they know it.

The second list is mostly things that used to be considered *adjacent* to the PM job. They are now the job. The centerpiece skills of the old job — stakeholder management, requirement gathering, spec writing, prioritization frameworks — are either commoditized or being absorbed into the agents themselves.

## § 07 · What you should do this week.

If you're reading this and recognize yourself in the first group — the document-PM — the work is not hopeless. It's just specific. Here's what I'd do this week if I were you, in order:

1. **Pick one thing on your roadmap and try to prototype it yourself, using the tools you have.** Not "spec it." Not "get engineering to build it." *Prototype it.* Claude Code, Cursor, Framer, v0, whatever. Get something that runs, even badly, by the end of the week. This is the skill that splits the groups. Either you can do this — or you can learn to — or you cannot. If you cannot, start now.
2. **Spend one afternoon replacing your last PRD with a prompt.** Take a spec you wrote recently. Feed it to an agent. See what it generates. Notice where it's wrong. Edit the prompt, not the spec. Keep iterating until the agent is producing work you would have assigned to a team. This exercise will tell you more about the new shape of the job than any essay, including this one.
3. **Stop writing the weekly update.** Replace it with a live dashboard that the agents populate. If your team needs a weekly written narrative to know what's happening, you have a communication problem that isn't solved by better writing — it's solved by better systems.
4. **Find someone on your team who is already operating in the new mode** and shadow them for a day. There is one, even at your company, even if leadership hasn't noticed yet. Watch what they actually do. It won't match any job description you've ever read.
5. **Pick a technical thing you don't understand — really understand, from the bottom — and close the gap.** It doesn't matter what. The point is to practice the habit of *not being content* with surface-level understanding of the systems you're responsible for. That habit is the new baseline.

If you're in the second group already, you mostly just need to keep doing what you're doing and stop apologizing for it. The parts of your job that don't look like the old job *are* the job now. The sooner you stop trying to also produce the old artifacts for legacy audiences, the sooner you get your full week back.

## § 08 · The title that doesn't matter.

My title is "Sr. Director of Product." The work I do has almost nothing in common with what a Sr. Director of Product did five years ago. The title stays because organizational machinery — comp bands, engineering ladders, exec review rhythms — takes longer to evolve than the work itself. Someone still has to take the meeting. Someone still has to sign the offer letter. That part endures.

But the *work* of that person is not the work the old title describes. The work is being a builder-orchestrator embedded in a business that's actively inventing the new shape of itself as it goes. At Machinify, that's part of what makes this the best chapter of my career — you're not retrofitting an agent-native way of working onto a legacy org chart; you're building both in parallel, alongside a team that genuinely wants to be first.

This is going to resolve everywhere, eventually. It always does. At some point — I'd guess inside of eighteen months — titles will catch up, ladders will catch up, comp will catch up, and the people who have been quietly doing the new work will be legible to the market as the thing they already are. The companies that give their people permission to do the new work before the machinery catches up are the ones that win the transition. I'm lucky enough to be inside one of them.

Titles are reporting structure, not identity. The identity is in the work. The work is unrecognizable from where it was two years ago, and every month that passes pushes it further into a future worth building.

---

If you're a product leader reading this: the question isn't whether to learn these tools. It's whether you're already too late.

I don't think you are. But the window is closing faster than anyone expected.

The title stays the same. The job is unrecognizable. **Long live the builder.**

—
*Written from Fort Collins, 5,000ft. Source at [philmora/essays](https://github.com/philmora/essays) · CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
