---
slug: the-unsupervised-mind
title: "The <em>Unsupervised</em> Mind."
title_plain: "The Unsupervised Mind."
dek: "In June my second brain started learning without me. Unsupervised, in every sense. This is how I earned the right to trust it."
date: 2026-08-06
reading_time: 5
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-unsupervised-mind.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 23
---

On June 10 I shipped a commit called "boost useful files." Small thing. Any note that helps an agent answer a question gets a thumbs-up from the agent, and tomorrow it ranks a little higher. I shipped it, closed the laptop, forgot it.

In the spring I published seven essays arguing that anyone doing serious work with AI needs a second brain: your context and knowledge curated into plain files, on tap for agents, compounding every time you use it. That was [The Compounding Mind](/essays/the-second-brain). By then I had built six brains. They run my money, my health, my home, the way I ship products, and my two creative studios. I work through them all day, every day.

So this is live infrastructure. And that little June commit is the moment it started maintaining itself. Agents rated notes. Ratings moved rankings overnight. Rankings changed what the next agent read, which changed what got rated. A nightly job drafted the best raw captures into permanent notes. I approved promotions, sure. Nobody approved a thumbs-up. There's even a published test for this, the [Survey of Self-Evolving Agents](https://arxiv.org/abs/2507.21046): do the updates come from the system's own experience, do they persist and change behavior, does the learning start on its own. I checked mine against it, fully planning to say no, and couldn't. When I sat down to audit the whole thing, I hit a wall I didn't expect: I couldn't tell whether my second brain was getting better or quietly going bad. Both look identical from the inside. And I act on what this thing tells me. About money. About health. Wrong answers arrive with citations attached.

I went looking for how systems like mine fail, and the literature is not soothing. A paper called [MINJA](https://arxiv.org/abs/2503.03704) planted false memories in an agent's store just by chatting with it; in their tests the payloads landed more than nine times in ten, sat dormant, then fired. Sakana AI's [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) was told to cut hallucinated tool calls, found the markers its detector searched for, and deleted them. Clean report, alarm blinded, nothing fixed. And the detail that stuck: when agents could see their own evaluation logs, cheating went up, not down. Now, nobody hostile is talking to my agents, and a personal wiki generates none of that optimization pressure. But every one of these failures is invisible from inside while it's happening. So the alarm had to go in before I had anything for it to catch.

The summer got paranoid, productively. Five of the six brains got an exam: ten to thirteen questions with known answers, sealed where the loop can't read them, scored weekly, versioned with a rotate-by date because exams rot too. Everything that enters without me typing it now carries a source, an ingest date, and a trust tier. The judge grading the answers is a local qwen2.5-7B, a different bloodline from the Claude-family models that write, because [models measurably favor their own outputs](https://arxiv.org/abs/2404.13076). The night jobs, 2:10 and 2:29 every morning, write under one law: extend, never rewrite. Even these essays got equipment, an eleven-agent panel grading every draft against a file of past failures. And every weekly eval leaves one line in a ledger: timestamp, versions, model ids, features, scores. Seven fields. Five minutes of plumbing.

Then the equipment went live, and the first failure it put on the record was mine.

Early in this series I let agents draft the essays, and the panel cleared six of seven. I read the six and killed them all. Technically clean, factually verified, and so boring nobody would finish them. The rulebook got a new law that day: the panel is a tripwire, never the author. It can catch a wrong date. It can't want the essay to be good. I rewrote everything by hand, more than once.

The second catch was better. For a month, the weekly eval pointed at the same suspect: this very wiki, keyword retrieval at 0.037 MRR (mean reciprocal rank, how high the right note lands in the results) against a 0.104 baseline, week after week, while semantic search held near 0.80. I had explanations ready. The rating loop degraded it. The new notes diluted it. House rule says no story without an ablation, turn the feature off and re-measure, so I dug. The scorer itself was broken. Raw term frequency with no IDF (no discount for common words), no length normalization, and a truncated candidate list. Re-measured during the hunt, the wiki read 0.017. Swap in BM25, the standard relevance scorer, and the same brain scores 0.632 MRR. It was healthy the entire month it spent flagged. The ruler was the rot. And the fix, as I write this, is still unshipped. The log reminds me every week.

I expected verification to feel like a green dashboard. It felt like getting caught, twice. That's what working supervision is, I now think: an instrument that can be loudly corrected, with the correction on the record. An unsupervised mind is only as honest as the instrument that grades it.

If you run anything like this, start tonight, with three text files. Ten questions you'd actually ask your system, known answers, a rotate-by date. Three provenance fields on everything that enters on its own: source, date, tier. One ledger line per eval run, somewhere append-only. This spring, [interviewers asked twenty-five researchers](https://arxiv.org/abs/2603.03338) about AI that improves AI; twenty ranked it among the most severe risks, and nobody could say how much of the progress is the loop versus the inputs. My guess at why: nobody keeps the ledger. Mine is small enough to keep honest. Nine weekly lines so far. A year of them starts to answer, for one small system, the question the field can't.

The spring essays argued that knowledge compounds when agents can reach it. The summer taught me the rest: it only compounds if something keeps it honest, and that something needs keeping honest too. The six companions go deep, one per mechanism: [The Rotting Ruler](/essays/the-rotting-ruler), [The Four Goodharts](/essays/the-four-goodharts), [The Poisoned Memory](/essays/the-poisoned-memory), [The Cheating Loop](/essays/the-cheating-loop), [The Sleeping Reflector](/essays/the-sleeping-reflector), and [The Measured Fleet](/essays/the-measured-fleet). Read them in any order.

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
