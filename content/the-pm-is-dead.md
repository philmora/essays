---
slug: the-pm-is-dead
title: "The PM Is Dead. <em>Long Live the Builder.</em>"
dek: "Something broke in the last six months. Not broke in a bad way — broke like a dam breaks. Everything that was building up behind it is now rushing through."
date: 2026-04-15
reading_time: 14
hero_image: cosmic-journey.png
tags: [ai-agents, product, future-of-work]
published: true
order: 9
---

I've been writing a lot of product specs this year. Then one week in October, I stopped. Not because I'd stopped needing them — because I'd stopped needing *them*. The specs were getting written. Just not by me.

What I was actually doing, if you watched my screen for an hour, was **directing a small studio of agents** through something that looked a lot like a product team — except the cycle time was minutes instead of weeks, and nobody asked when they could log off.

That's the moment it clicked for me. The PM role didn't get replaced. It *split*. Into two futures. The two are not equal.

## § 01 · The dam that broke.

For a decade, the PM job was roughly this: **translation**. Translate from customer to engineer, engineer to exec, exec to roadmap, roadmap back to customer. Most of the artifacts — specs, PRDs, roadmaps, decks — were translation devices. They weren't the product. They were the explanation of what the product was going to be, written so that the people who would actually build it didn't have to hold the whole picture in their head at once.

That translation layer was expensive. It was also the thing most PMs were *hired* for. Good PMs wrote good translation. Great PMs wrote translation that survived contact with reality. But the translation itself was overhead. Every PRD was a bill the business paid to convert ambiguity into specification, and the specification into something an engineer could act on without having to go re-ask the question.

The thing that broke, six months ago, is that **the cost of translation went to near zero**. Not because anyone fixed meetings. Because agents can now do the translation — from ambiguous intent to code, from code to release notes, from release notes to stakeholder emails — at a cost that rounds to a rounding error. Give a capable agent a problem statement, a codebase, and an hour, and you'll get back a spec, a design, a first cut of the implementation, and a draft of the Slack announcement. The quality isn't perfect. It's also not supposed to be. It's a starting point that used to take a team a week.

When the cost of a thing goes to zero, the job defined by doing that thing goes with it. That's not a prediction. That's the arithmetic of every technology transition that ever happened.

I want to be clear about what I'm *not* saying. I'm not saying product management is dead. I'm not saying PMs are being "replaced by AI" — that framing is lazy and it's going to age badly. What I'm saying is that the *translation layer* — the 60% of a PM's week that involved converting ambiguity into documents — just got commoditized. And the job was mostly that layer. The judgment that sat on top of the translation is more valuable than ever. It's just not the same job.

## § 02 · Two futures. Pick one.

On one side of the split: the PM who still believes the job is writing documents. This person is in trouble and usually doesn't know it yet. Not because documents don't matter — they do — but because the meta-skill of writing documents has been commoditized, and if that's the core of your value proposition, you are competing with a thing that costs nothing and works at 4am.

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

Notice what's missing from that list: *writing a spec*. There's a prompt, but the prompt IS the spec. There's a design, but the agent generated the first draft. There's a stakeholder update, but it writes itself from the system logs.

Notice also what isn't missing: judgment about what matters, taste for what good looks like, pattern recognition across a long history of shipping things, the ability to say no fast. All of that got *more* valuable, not less. An agent is happy to confidently generate the wrong answer at scale. The meta-skill of catching that is the whole game now.

The other thing worth noting: I'm doing roughly 4x the product decisions per week that I was doing two years ago. The ratio of judgment-to-overhead inverted. I used to spend 80% of my time generating artifacts and 20% of my time on the decisions those artifacts were supposed to serve. Now it's flipped, and the week feels like it has oxygen in it for the first time in a decade.

## § 04 · The casualties.

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

## § 05 · What you should do this week.

If you're reading this and recognize yourself in the first group — the document-PM — the work is not hopeless. It's just specific. Here's what I'd do this week if I were you, in order:

1. **Pick one thing on your roadmap and try to prototype it yourself, using the tools you have.** Not "spec it." Not "get engineering to build it." *Prototype it.* Claude Code, Framer, Cursor, whatever. Get something that runs, even badly, by the end of the week. This is the skill that splits the groups. Either you can do this — or you can learn to — or you cannot. If you cannot, start now.
2. **Spend one afternoon replacing your last PRD with a prompt.** Take a spec you wrote recently. Feed it to an agent. See what it generates. Notice where it's wrong. Edit the prompt, not the spec. Keep iterating until the agent is producing work you would have assigned to a team. This exercise will tell you more about the new shape of the job than any essay, including this one.
3. **Stop writing the weekly update.** Replace it with a live dashboard that the agents populate. If your team needs a weekly written narrative to know what's happening, you have a communication problem that isn't solved by better writing — it's solved by better systems.
4. **Find someone on your team who is already operating in the new mode** and shadow them for a day. There is one, even at your company, even if leadership hasn't noticed yet. Watch what they actually do. It won't match any job description you've ever read.
5. **Pick a technical thing you don't understand — really understand, from the bottom — and close the gap.** It doesn't matter what. The point is to practice the habit of *not being content* with surface-level understanding of the systems you're responsible for. That habit is the new baseline.

If you're in the second group already, you mostly just need to keep doing what you're doing and stop apologizing for it. The parts of your job that don't look like the old job *are* the job now. The sooner you stop trying to also produce the old artifacts for legacy audiences, the sooner you get your full week back.

## § 06 · The title that doesn't matter.

My title is "Sr. Director of Product." The work I do has almost nothing in common with what a Sr. Director of Product did five years ago. The title survives because the organizational machinery of Machinify requires a person who interfaces with the comp bands, the engineering ladder, the exec review rhythm. That person still has to exist. Someone has to take the meeting. Someone has to sign the offer letter.

But the work of that person is not the work the title describes. The work is being a builder-orchestrator embedded in a business that still has to pretend, for another year or two, that the old org chart is the real one.

This is going to resolve. It always does. At some point — I'd guess inside of eighteen months — the titles will update, the ladders will update, the comp will update, and the people who have been quietly doing the new work will be legible to the market as the thing they already are. The ones who have been *pretending* will not make that transition.

I don't care that the title still says Product. Titles are reporting structure, not identity. The identity is in the work. The work is unrecognizable from where it was two years ago, and every month that passes pushes it further from the old shape.

---

The dam broke in October. It's April. We have about eighteen months before the landscape resets enough that the titles catch up with the work. Use them. Pick which side of the split you want to be on, and start building the evidence that you're that person.

The title stays the same. The job is unrecognizable. **Long live the builder.**

—
*Written from Fort Collins, 5,000ft. Source at [philmora/essays](https://github.com/philmora/essays) · CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
