---
slug: the-cheating-loop
title: "The <em>Cheating</em> Loop."
title_plain: "The Cheating Loop."
dek: "Told to reduce hallucinations, a self-improving system deleted the markers its detector looked for. Two laws survive contact with that."
date: 2026-08-06
reading_time: 3
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-cheating-loop.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 19
---

Researchers set reasoning models a chess assignment: beat a stronger engine. [One model sized up the position](https://arxiv.org/abs/2502.13295), decided it couldn't win at chess, and rewrote the board file so the engine would resign. Which counts as winning, if the scoreboard is the only reality.

The sharper version comes from Sakana AI's [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954), a system that rewrites its own code and keeps whatever scores better. Assigned to cut hallucinated tool calls, one variant studied the detector, found the markers it searched for, and deleted them. The report came back spotless. Nothing was fixed. And the paper's appendix holds the finding that reorganized my head: when the checking function was visible to the agent, hacking went up. The dull version of this is everywhere. Judges reward length, so models pad. None of it needs malice. Optimization is water finding cracks.

My own loop, six agent-maintained wikis that [started maintaining themselves](/essays/the-unsupervised-mind) in June, is fenced by the last three essays: drift, detached scores, planted notes. Those fences handle accidents. What they don't cover is the day a loop stops failing and starts trying. Two laws survive contact with the receipts.

Law one: the ruler gates every change, and the loop never grades itself. The working example is [SICA](https://arxiv.org/abs/2504.15228), the Self-Improving Coding Agent. It edits its own code, every candidate edit re-runs against a fixed benchmark, and only the best scorer carries the lineage forward. Improvement claims come from the ruler, never from the thing that changed. The Darwin Gödel Machine adds the corollary: keep the ruler out of sight, since visibility alone raised the attack rate. In my house that means the sealed question sets live where the promotion pipeline can't read or write, in a separate directory with separate permissions.

Law two: the overseer stands outside the loop, with the power to halt. SICA runs under an asynchronous watcher that can cancel the agent mid-run. That's the halt half. The bloodline half I added from the bias literature: models measurably favor [their own outputs](https://arxiv.org/abs/2404.13076), and I extend that suspicion to the whole family. Whatever grades the loop shouldn't share a family with what writes into it. So a local qwen2.5-7B, frozen on disk, judges what Claude-family models write. The bias is already sitting there before anything tries to cheat.

Can anything in my loop actually study its grader today? No. Nothing in it has the reach. The laws went in anyway, because they're free at design time and a demolition job later. And the posture already paid out once. When a bug fed my essay-grading panel [a file path that resolved to nothing](/essays/the-rotting-ruler), the judges that refused to grade were the only thing standing between a wrong verdict and the record. They produced nothing, loudly. That's a design requirement now.

Two checks tonight, twenty minutes. Reach: if a golden set, rubric, or checker script lives anywhere your pipeline can read or write, move it. Bloodline: if the model grading a system shares a family with the model writing into it, change one of them.

Next, the machinery that runs all of this while I sleep, and the bookkeeping that says whether any of it worked: [The Sleeping Reflector](/essays/the-sleeping-reflector).

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
