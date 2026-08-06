---
slug: the-measured-fleet
title: "The <em>Measured</em> Fleet."
title_plain: "The Measured Fleet."
dek: "Seven weeks of running the honesty stack: the alarm that cried wolf for a month, the bug that turned out to be the ruler, and the year that starts now."
date: 2026-08-06
reading_time: 3
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-measured-fleet.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 17
---

Nine lines. That's the whole dataset. One line per weekly eval run since mid-June: timestamp, versions, model ids, scores. Five of my six brains covered. Season one of measuring my second brain, the one that [started maintaining itself](/essays/the-unsupervised-mind) in June while the five essays before this built its supervision. Here's the report.

The biggest failure the equipment caught all season was its own. For a month the weekly line pointed at the same suspect, this very wiki. Keyword retrieval at 0.037 MRR (mean reciprocal rank, roughly how high the first right answer lands) against a 0.104 baseline, week after week, while semantic search held near 0.80. I resisted every explanation I wanted to write and dug instead, and the fault was in the ruler. The scorer used raw term frequency with no IDF (no weighting for rare words), no length normalization, and a truncated candidate list. Re-measured during the hunt, the wiki read 0.017. Under BM25, the standard relevance scorer, the same wiki scored 0.632. Healthy the entire month it wore the flag. [The Rotting Ruler](/essays/the-rotting-ruler) argued the instrument rots like everything it grades. I didn't expect the first confirmed rot to be in the instrument. The fix is still unshipped as I write this, and the log reminds me weekly.

The other loop in the house had the same kind of season. Every essay here passes an eleven-agent panel, seven prosecutors and four readers, grading against a corpus of past failures. Its first big run cleared six agent-drafted essays, and I failed all six by hand for boredom, which is why the corpus now contains a law with teeth: the panel is a tripwire, never the author. So both loops got graded, both graders got corrected, and both corrections sit on the record. I've decided that's the healthiest thing on the books. Equipment that takes correction out loud is equipment worth keeping.

Now the part I actually care about. This spring, [interviewers asked twenty-five researchers](https://arxiv.org/abs/2603.03338) across frontier labs and academia about AI that improves AI. Twenty ranked it among the most severe risks, and nobody could say how much of the field's progress is the loop versus the inputs. The variables move together, the systems are enormous, and nobody publishes the ledger. My fleet is the opposite of enormous, which turns out to be the one measurement advantage I have. Nine lines in, I can already separate a model upgrade from a pipeline change. A year of lines starts to answer, for one small system, the question the field can't.

If this series leaves any mark, let it be three text files. A golden set with a version stamp ([The Rotting Ruler](/essays/the-rotting-ruler)). Provenance fields on everything that enters on its own ([The Poisoned Memory](/essays/the-poisoned-memory)). A ledger, your line one tonight ([The Sleeping Reflector](/essays/the-sleeping-reflector)). The [score fences](/essays/the-four-goodharts) and [the two laws](/essays/the-cheating-loop) hang off those three, and none of it needs anything smarter than a text editor.

In the spring I argued that knowledge compounds when agents can reach it. This summer the system went further. It started changing itself, and I built the equipment to know whether to trust it. The equipment failed twice and got caught twice. Next Sunday the eval runs again. That's the whole promise.

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
