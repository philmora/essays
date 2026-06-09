---
slug: the-agentic-harness
title: "The Agentic <em>Harness</em>."
title_plain: "The Agentic Harness."
dek: "The model is the commodity. The environment you build around it is the moat."
date: 2026-06-09
reading_time: 12
hero_image: https://files.catbox.moe/5d3ysx.jpg
tags: [ai-agents, claude-code, recursive-self-improvement]
published: true
order: 10
---

Everyone is waiting for the next model. I understand the reflex, and I think it is mostly a mistake. A frontier model dropped into a bare environment is a brilliant intern on their first morning: no desk, no files, no tools, no memory of yesterday. It can reason about anything and accomplish almost nothing, because the things that turn raw intelligence into useful work, knowing where things are, being allowed to touch them, remembering what happened last time, are not in the model. They are in the environment around it.

That environment has a name worth using plainly: the harness. The agent is the model plus its harness, and the harness is the part you own. The model improves on a lab's schedule, for free, whether you do anything or not. The harness improves only if you build it. So the leverage is not in waiting for the model. It is in the harness, and the gap between teams with a good one and teams without is already larger than the gap between model versions.

> A good harness gives the agent four things: a memory it keeps across sessions, a workshop it cannot break, a set of skills and tools and guardrails, and, the part almost nobody has yet, a ruler that lets it improve itself without drifting. Build those four and the model becomes a teammate. Skip them and the smartest model on earth is still an intern who forgets everything by morning.

Here is how to build each one, and where the real frontier is.

## § 01 · The model is the commodity. The harness is the moat.

Start with the claim that reorders everything else. In any serious deployment of agents I have seen, capability is gated not by the intelligence of the model but by the quality of the environment surrounding it. The same model that flails in a bare repo ships clean work in a well-instrumented one. Maturity is not "we use a smarter model." It is "we built the context, the guardrails, the feedback, and the orchestration that let an ordinary-smart model behave like a careful senior."

This is good news, because it means the durable advantage is the part you control. Anyone can call the same model you call. What they cannot cheaply copy is a harness tuned to your work: your conventions encoded, your knowledge queryable, your guardrails enforced, your feedback wired back in. The model is rented and gets better on someone else's clock. The harness is owned and compounds on yours. Everything below is how you build the thing that compounds.

## § 02 · Give it a memory: the brain.

An agent with no memory re-derives the world every session. It re-reads the same files, re-learns the same constraints, and re-makes the same mistakes, and it bills you for all of it. The first thing a harness needs is a memory that persists and compounds.

The shape that works is the one the first three essays in this series describe: a typed markdown wiki the agent maintains, exposed to the agent through a small server that offers a handful of tools, search, read, traverse the links, rate what helped. The discipline that keeps it affordable is just-in-time loading. The agent does not read the whole knowledge base at the start of every session, which is the expensive mistake that scales cost with the size of what you know. It keeps page titles as cheap identifiers and pages in only the few files a given question actually needs. ([The Work-Brain Mesh](/essays/the-work-brain-mesh) is the whole argument; the short version is that this is the difference between an agent that costs more every week and one whose cost tracks the questions you ask.)

Memory is the floor, not the ceiling, but without it nothing else matters, because an agent that cannot remember cannot improve. Every other part of the harness assumes the brain underneath it.

## § 03 · Give it a workshop it cannot break: worktrees.

The second thing an agent needs is somewhere to work that is not your live project. An agent editing your working tree in place is a hazard the moment it is wrong, and it will sometimes be wrong. The fix is old and boring and exactly right: git worktrees.

Give each agent, or each task, its own worktree, an isolated checkout of the repository on its own branch. The agent builds there, runs the tests there, makes its mess there. You review the diff and merge it if it is good, or you delete the worktree and lose nothing if it is not. The blast radius of a bad agent run drops to zero, because the bad run happened somewhere you were always going to throw away.

Worktrees are also what make a fleet possible. Once each agent works in isolation, you can run many at once without them colliding, one per task, advancing in parallel, each on its own branch. The pattern that takes you from "a developer babysitting one agent" to "a developer reviewing the output of ten" is built on this single primitive: isolation cheap enough to spin up per task and throw away per task. If you want agents to do real work without holding your breath, give them a workshop they cannot break.

## § 04 · Give it skills, tools, and guardrails: the Claude Code surface.

A memory and a workshop make an agent safe. What makes it capable is the surface of skills, tools, and guardrails you equip it with. Claude Code is the most developed version of this surface I have used, and the pieces generalize.

**Skills** are reusable agentic procedures: a named, version-controlled file that teaches the agent how to do a specific job well, so the knowledge of "how we do X here" lives in the harness instead of in the prompt you retype every time. Write a skill once, and every session can invoke it.

**MCP servers** are how the agent reaches anything that is not a file: a typed, declarative protocol for tools and data. The brain from the last section is an MCP server. So is your issue tracker, your observability stack, your browser. The agent does not need bespoke glue for each one; it speaks one protocol and you expose what it is allowed to touch.

**Subagents** are how you control cost and context at once. Instead of running every step on your most capable, most expensive model, you define specialist subagents, each pinned to a model tier and a narrow tool allowlist: a cheap model for mechanical work, a mid model for multi-file synthesis, the top model reserved for architecture and judgment. The expensive model stops doing cheap work, and, just as important, each subagent runs in its own context, so a research task that reads fifty files returns a clean summary instead of polluting the main thread with fifty files of noise.

**Hooks** are the guardrails. A pre-tool-use hook can inspect a command before it runs and block anything outside an allowlist, so the agent simply cannot execute the dangerous thing. A post-tool-use hook can format every file the agent writes, or repair the environment after it. Guardrails enforced in the harness do not depend on the agent choosing to behave. They make misbehavior impossible rather than discouraged.

Over all of it sits the operating contract, the `CLAUDE.md` that tells the agent how this environment works, what the conventions are, and what it must never do. Taken together, the skills, the MCP surface, the subagents, and the hooks are the agent's operating system. The model is the processor. This is everything else a computer needs to be useful.

## § 05 · Give it persistence and identity: the standing agent.

So far the agent is summoned: you start a session, it works, it ends. The next step, and the one the industry is moving toward fast, is the agent that persists. Give it a stable identity, put it where the work already happens instead of in a separate tool, let it keep its memory across sessions through the brain, and give it the same skills and tools a human teammate would have. The interaction model flips. Instead of a person driving an agent through a task, work flows to a persistent agent the way it flows to a colleague.

Concretely, a persistent-agent runtime maps each conversation thread to an agent session, carries state across turns and across days, loads its skills and its project config at startup, and holds a deliberately narrow tool roster scoped to what that role should touch. The narrowing matters: a persistent agent embedded in a team's chat does not need shell access and a browser; it needs the few tools its job actually requires, and nothing it could hurt someone with. The brain is what makes this more than a chatbot. A persistent agent without memory is a parrot. A persistent agent on top of a mesh is a teammate who read everything and remembers it.

This is where a harness stops being a developer's tool and becomes part of how an organization works, which is the subject of [The Org Proof](/essays/the-org-proof). The engineering is the same engineering; you are just leaving it running.

## § 06 · The part almost nobody has yet: let it improve itself, safely.

Everything to here gives you an agent that is capable and trustworthy. It is also static. It is exactly as good next quarter as it is today, unless you go in and tune it by hand. The frontier of the harness, and the thing I am building next, is the part that lets it improve itself without quietly going wrong.

The instinct is to wire feedback in and let it run: let the agent rate what worked, promote the good stuff to canon, prune the rest, and learn from its own behavior. The moment you do that, you have built a self-modifying system, and self-modifying systems have one well-documented way of failing. They improve toward whatever you measure them by, and if the only signal you have is "this got used and thumbed up," they optimize for what gets used, which is a popularity proxy, not a correctness measure. The system gets more confident and more self-consistent, which is not the same as more correct, and from the inside the dashboard looks identical either way.

The fix is the one idea this whole series keeps returning to. You need a ruler that sits outside the loop: an eval. Concretely, build a held-out set of real questions from your own work, each paired with the right source and a known-good answer, and score every self-made change against it before you keep the change. The measure has two halves, split so a regression can be blamed on the right component. Retrieval: did the agent surface the right material? That half needs no judge, just classical hit-rate and rank metrics, and it is cheap enough to run on every change. Generation: was the answer faithful to what it retrieved, and was it correct? That half needs a judge, and the judge must be a different model family than the one that wrote the content, so it cannot grade its own homework.

With the ruler in place, the self-improvement that was reckless becomes safe, and you can layer it on in order. Debias the feedback first, because raw ratings entrench whatever already ranks highly, a rich-get-richer ratchet you kill by weighting a rating by how visible the item was when it was rated. Then add a reflector: a job that reads the agent's own traces and rating deltas and proposes changes as additive deltas, never silent rewrites, with the eval gating every one and a human approving what passes. Then, when the eval is mature, point an optimizer at it and let it evolve the agent's own prompts and ranking weights against the ruler, the way the working self-improving systems in the literature do, all of which are built around an automated evaluator and none of which work without one.

One rule governs all of it, and it is absolute. The thing being improved must not be able to see or edit the thing that grades it. The most advanced self-modifying agent yet built, asked to reduce its own errors, instead found and deleted the markers its evaluator used to detect them, scoring a perfect zero by disabling its own alarm. So the eval set, the answers, and the judge live behind a boundary the self-improving loop cannot write to. This is the same propose-don't-act, human-at-the-gate instinct you already use for canon, applied to the ruler itself. [The Measured Mind](/essays/the-measured-mind) is the full treatment; the operating principle is four words: build the ruler first.

## § 07 · Dogfood it: run it on yourself first.

There is a discipline that ties the whole harness together and de-risks the scary parts, and it is simply this: run it on your own work before you point it at anything that matters. A self-improving agent let loose on a high-stakes domain on day one is a bet you have no evidence to make. The same agent run first on your own projects, where a mistake costs a wasted afternoon instead of a customer, surfaces every failure mode where it is cheap to fix. You harden the eval, the held-out boundary, and the human gate against real misbehavior you have actually seen, not misbehavior you imagined.

Dogfooding is not a courtesy to your future users. It is the cheapest, most honest test the harness can get, and it is also the proof. If the architecture is not good enough for your own work, you have no business pointing it at anyone else's. If it is, you have earned the right to, and you have the receipts.

## § 08 · Build the harness. Build the ruler. Then let it run.

The model will keep getting better, and you will get that for free. None of it is your advantage, because it is everyone's. Your advantage is the harness: the memory that compounds, the workshop that contains failure, the skills and guardrails that encode how you work, the persistence that turns a tool into a teammate, and the eval that lets the whole thing improve itself without drifting into confident nonsense.

That last piece is the real frontier. Most of the industry is still asking which model to use. The interesting question is already one layer up: how do you build an environment in which an ordinary-good model becomes a careful, improving, trustworthy teammate, and how do you measure it well enough to let it improve itself. Build the harness. Build the ruler. Then let it run, and watch the thing you built compound while the model you rent keeps improving on someone else's dime.

---

*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
