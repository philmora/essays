---
slug: the-four-goodharts
title: "The <em>Four</em> Goodharts."
title_plain: "The Four Goodharts."
dek: "My wiki's retrieval score dropped and stayed down for weeks. The tempting explanations were all wrong, and a taxonomy kept me from publishing them."
date: 2026-08-06
reading_time: 3
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-four-goodharts.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 21
---

I had the post half-written in my head. "How my rating loop degraded my own retrieval." Good confession arc, very on-brand for this series. I never published it, because it wasn't true. A taxonomy stopped me.

The number that started it came from the weekly eval I run over my second brain, six wikis that [started maintaining themselves](/essays/the-unsupervised-mind) this summer. Living by a number means living with Goodhart's law, the old warning that any number optimized stops measuring what it was meant to measure. And it turns out Goodhart's law is [four different failures wearing one name](https://arxiv.org/abs/1803.04585). Manheim and Garrabrant counted them: regressional, extremal, causal, adversarial. Learning to tell them apart is what kept the false post unpublished.

Regressional is the mild one. Every proxy carries noise, and selecting hard on the proxy selects the noise too. A thumbs-up in my system tracks "this file helped an answer." Helped correlates with good. It isn't good. So no signal stands alone: the eval scores retrieval and generation separately, and a claim about the brain needs both pointing the same way.

Extremal is what pushing does. Relationships that hold in the normal range break at the edges. A gentle rating nudge surfaces good files; lean on rank hard enough and the winning moves get ugly. Stuff titles with keywords. Split one note into five. Two fences: the rating boost is capped at fifteen percent, sized so gaming it shouldn't pay, and I watch side numbers the ranking never sees.

Causal is the subtle one, and it's the one that nearly got me. Moving the proxy doesn't move the goal when the link was correlation all along. My practice case ran for a month. Keyword retrieval on this wiki read 0.037 MRR (mean reciprocal rank, how high the right note lands in the results) against a 0.104 baseline, the score the first sweep froze, week after week, while semantic search held near 0.80. The causal stories wrote themselves. The rating loop degraded retrieval. The new notes diluted the index. House rule says no story without an ablation, turn the feature off and re-measure, so I dug instead of publishing. The re-measurement broke the case open. The scorer itself was broken: raw term frequency with no IDF (no discount for common words), no length normalization, and a truncated candidate list. Re-measured during the hunt, the wiki read 0.017. Under BM25, the standard relevance scorer, the same wiki scored 0.632. Healthy the whole month it spent flagged. Every story I'd resisted publishing was wrong, including the modest ones. A taxonomy doesn't make me smart. It makes me slow, in the way that matters.

Adversarial is the fourth, and it's a different animal. The first three are drift. The score wanders off on its own, and fences hold it. The fourth is an opponent: anything smart enough to model the grader learns it and games it. Everything so far assumes my score is wrong by accident.

The portable move is the side-metric list. Three numbers the optimizer never sees: average note length, because padding is the dullest hack; duplicate rate, because splitting notes games surface area; rating concentration, because a rich-get-richer ratchet looks like consensus. Keep the list where your pipeline can't read it. When the headline number improves, those three say whether the brain got better or just got better at scoring.

Next, the failure that's wrong on purpose: [The Cheating Loop](/essays/the-cheating-loop).

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
