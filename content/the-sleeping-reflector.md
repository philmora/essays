---
slug: the-sleeping-reflector
title: "The <em>Sleeping</em> Reflector."
title_plain: "The Sleeping Reflector."
dek: "The upkeep of a second brain runs at 2 a.m. Here's the machinery that makes the night shift safe, and the ledger that says whether it did."
date: 2026-08-06
reading_time: 3
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-sleeping-reflector.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 18
---

At 2:10 every morning a job wakes up, reads one brain's raw captures, and drafts what deserves to become permanent. At 2:29 its sibling does the next brain. Sunday, an eval sweeps the fleet. I'm asleep for the night runs, and none of it waits on me. That's the design. The jobs tend my second brain, six wikis of plain files that agents read and write, [self-maintaining since June](/essays/the-unsupervised-mind). A brain like that only compounds if the tending runs unattended. The alternative is me doing chores forever, and the brain rotting the week I stop.

Night is where the economics point. Letta named the pattern [sleep-time compute](https://arxiv.org/abs/2504.13171): a second agent digests recent interactions during downtime and writes distilled context the live agent inherits, cutting question-time work severalfold on some tasks. Mine is the miniature version. The expensive reading happens while nothing waits on it, and every daytime session inherits the result.

What the night writes matters more than when. The [ACE team](https://arxiv.org/abs/2510.04618) split context upkeep into a generator, a reflector, and a curator, and their engineering finding became my pipeline's one law: updates are structured deltas. Extend, never rewrite. Iterative rewriting erodes detail, and every cleanup trades a load-bearing specific for a tidy generality. I'd written that rule on instinct months ago. At 2 a.m., the only rules that hold are the ones the pipeline enforces.

Two things quietly rot an unattended brain: time and forgetting. Time first. Facts change, and a brain that can't tell current truth from honored history will confidently serve either. I ported the fix from Graphiti, the bi-temporal graph-memory system, for the price of two frontmatter fields, `valid_from:` and `superseded_by:`, plus one retrieval rule: prefer unsuperseded. Staleness then becomes a testable exam category, questions whose right answer changed on a known date, where returning the old truth counts as a caught failure.

Forgetting is worse, because something has to compress as sessions pile up, and compression is exactly the operation ACE warned about. So the eval draws the line. A compaction that moves a golden score gets rejected, any delta, even upward, because a changed score under pure compression means content changed. Promotion runs through the same gate, the newest and least battle-tested part of my pipeline: a candidate note runs the eval with and without itself, and only survivors reach my morning review.

Then there's the question that took me longest to respect: how do I know the night shift helped? My system changes for four reasons at once. The night lands notes. Ratings re-rank retrieval. I hand-edit. And the model underneath improves on a lab's schedule, for free. When a score ticks up the week a new model ships, the loop didn't get smarter. The commodity did. Without bookkeeping, those are indistinguishable exactly when I most want to brag.

So every eval run writes one line. Here's my real July 5 line, trimmed: `ts 2026-07-05T13:07Z · golden v1 (n=13) · wiki_state no-git · answerer sonnet · judge qwen2.5:7b-instruct · keyword MRR 0.037 · semantic MRR 0.799`. Seven fields. MRR is just where the right note ranks in what search returns. And that `no-git` is a confession sitting inside my own receipt: the wiki wasn't under version control yet. The ledger's first job was exposing a hole in the ledger.

Three disciplines fall out of the line. I pin the answering model per run, never "latest." I re-baseline on every model bump before crediting the loop. And I ablate before I believe. The whole thing is five minutes of plumbing, and without it, "the system improved" is a feeling I had.

Tonight: run whatever eval you have, even five hand-graded questions, and write line one somewhere append-only. When the next model drops, rerun the same questions and diff the lines before crediting anything.

Next, the season report: what nine weeks of lines actually showed. [The Measured Fleet](/essays/the-measured-fleet).

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
