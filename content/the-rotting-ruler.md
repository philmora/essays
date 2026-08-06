---
slug: the-rotting-ruler
title: "The <em>Rotting</em> Ruler."
title_plain: "The Rotting Ruler."
dek: "I built the measuring stick for a self-maintaining second brain. The stick turned out to be a living system too, and it rots."
date: 2026-08-06
reading_time: 4
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-rotting-ruler.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 22
---

On an early run of my essay-grading panel, a bug handed all ten judges a file path that pointed at nothing. Four refused to grade. The other six went hunting through the filesystem, found an older copy of the essay, and confidently graded the wrong text. The four that returned nothing were the only honest ones in the room.

I keep coming back to that run, because it compresses everything the summer taught me about instruments.

The background, in one breath: my second brain is six wikis of plain files that AI agents read and maintain, this summer it [started maintaining itself](/essays/the-unsupervised-mind), and I couldn't tell improvement from rot. So five of the six brains got exams (the sixth, my home wiki, sits parked for now): ten to thirteen questions with known answers, a golden set, sealed away from the maintenance loop, scored weekly. Drift becomes a number on a calendar instead of a feeling in my gut. That was supposed to be the end of the story. The exam watches the brain, done.

Then the instrument started teaching me about itself. Three lessons, in the order they landed.

My standards moved first. The first golden set I cut encodes June-2026 me, and June-2026 me went out of date in about three weeks. By the third scoring session I held opinions the set couldn't express. An answer can cite the right file and miss the point. Correct-but-stale is its own failure. Some questions deserve an honest "I don't know." There's a paper that watched practitioners hit exactly this wall, [Who Validates the Validators?](https://arxiv.org/abs/2404.12272), and they gave it a name: criteria drift. Grading outputs is how I discovered my criteria were incomplete. The fix is boring and works. The golden set now carries a version number, in a sidecar note beside the sealed file, since the sealed file itself can't be edited. A grading session that amends a question bumps it, and every eval from here records which version it ran against, so the numbers stay comparable across months.

Second lesson: the loop can memorize the exam. Public benchmarks died this death years ago. Test sets leak into training data, and a score on a memorized benchmark is measuring recall. The field's answer is the living benchmark. [LiveBench](https://arxiv.org/abs/2406.19314) rotates in fresh questions monthly. [FrontierMath](https://arxiv.org/abs/2411.04872) kept its problems private, and even that took a hit; in January 2025 it came out that a funder had access to most of the set. The strictest ruler in the field, and the story still became who governs the ruler. Now, my wiki leaks into nobody's training run, but the structural version lives in my house too. A nightly job proposes notes, I approve them, the eval keeps score, and over time the system can drift toward notes shaped like the test while the number climbs. At my scale the pressure is weak. The defenses went in while they were cheap. The set stays sealed, out of the loop's reach, and every week's score lands against a frozen baseline. The next questions will grow out of recent sessions, which stays ahead of anything the loop could memorize. And a few canary questions assert load-bearing rules, so an approved note that rewrites doctrine trips the alarm.

Third lesson: the judge has a version number. My grader is a model. Providers update models silently, and a judge that scores one way in March scores another way in June, which breaks every comparison across the gap. Model judges also arrive with thumbs on the scale; they favor longer answers and [their own outputs](https://arxiv.org/abs/2404.13076). So my judge is a local qwen2.5-7B, a different family from the Claude models that write the notes, frozen on disk, version recorded on every run. Once a quarter I grade thirty answers blind and check the judge still agrees with me. When agreement sags, I amend the rubric. I don't shop for a friendlier judge.

Which brings me back to the panel that graded the wrong essay. An instrument that improvises its own inputs has stopped measuring, and it doesn't know it. Refusal is required behavior in my graders now. Can't verify the input? Return void. And void never counts as a pass.

The portable version is two lines at the top of one file. If you keep any kind of golden set, give it a version number that bumps when a grading session amends it, and a rotate-by date. Mine says October 8, and both lines went in this week. Next comes the score itself, and the four ways it comes loose from what it measures: [The Four Goodharts](/essays/the-four-goodharts).

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
