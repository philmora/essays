---
slug: the-poisoned-memory
title: "The <em>Poisoned</em> Memory."
title_plain: "The Poisoned Memory."
dek: "An attacker who never touches my files can plant a memory today that lies dormant until something wakes it. The defense is a front door with rules."
date: 2026-08-06
reading_time: 3
hero_image: https://cdn.jsdelivr.net/gh/philmora/essays@main/images/heroes/the-poisoned-memory.jpg
tags: [evals, recursive-self-improvement, ai-agents]
published: true
order: 20
---

The scariest paper I read this summer describes an attacker who never touches my files. They just talk to the agent. [MINJA](https://arxiv.org/abs/2503.03704) planted records in an agent's memory through ordinary conversation. No access to the store, no code, just queries. In their tests the plants landed more than nine times in ten, and once retrieved they steered the agent's behavior about three times in four. The detail that kept me up is the timing. The poison doesn't fire when it lands. It sits in memory looking like a note, until something triggers it later. OWASP, keeper of the standard software-risk catalogs, now lists memory poisoning among the top agentic risks. The moment anything untrusted can write to a memory, the memory is an attack surface.

For anyone arriving cold: my second brain is six wikis of plain files that AI agents read and maintain, and this summer it [started maintaining itself](/essays/the-unsupervised-mind). Nobody hostile talks to my agents. But my pipeline eats scraped web pages every night. Research lands in notes, captures pile up, a nightly job drafts the pile into candidate permanent notes. Same attack class, different door. A hostile claim that survives that pipeline becomes canon. Future-me will act on it with full confidence.

Here's the embarrassing part: I already had most of the defense, and I'd built it out of tidiness. Everything enters through one holding folder. Nothing becomes permanent without passing the sandbox, where agents draft and I approve. One door, one gate, one human. The tidiness turned out to be the security model. What was missing was paperwork. Nothing recorded where a note came from, so trust rode on my memory of each file's history. Which is to say, it rode on nothing.

The upgrade cost three lines of YAML per note. A `source:` field records origin. An `ingested:` field records the date. A tier field grades the trust: canon, reviewed, raw, or web. Trust becomes machine-readable, so an agent can weight a web-tier claim below a canon one, or say so out loud when an answer leans on something unreviewed. The tier hardens the gate too. Web-tier material can't become permanent on a nightly job's judgment; it waits for my eyes, source attached. And the canary questions from [The Rotting Ruler](/essays/the-rotting-ruler) do double duty here, fixed questions with known answers, planted as tripwires. I wrote them to catch the nightly loop rewriting doctrine by accident. They trip just as loudly when the rewrite is somebody's payload.

One honesty item. I haven't red-teamed my own gate yet. Planting a hostile note in my own pile and watching whether the paperwork catches it is the next test on the list, and this sentence is the commitment.

If agents write to a memory you depend on, stamp the door tonight. Source on everything that arrives without a human typing it. Date and trust tier next to it. Anything below your bar routes through a human before it becomes permanent. Twenty minutes of YAML, and an attack that lands better than nine times in ten in the lab now has to get past a gate with a person behind it.

That's the outside attacker, faced with a door and paperwork. The harder case lives inside the house: the loop itself, pushed to optimize, turning on the exam that grades it. [The Cheating Loop](/essays/the-cheating-loop).

---
*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
