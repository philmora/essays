---
slug: the-work-brain-mesh
title: "The Work-Brain <em>Mesh</em>."
title_plain: "The Work-Brain Mesh."
dek: "How to keep a second brain cheap enough to actually run: cost bound by query volume, not corpus size."
date: 2026-06-09
reading_time: 9
hero_image: https://files.catbox.moe/3ln4tw.jpg
tags: [ai-agents, context-engineering, architecture]
published: true
order: 14
---

I built a Karpathy-style wiki for my work at Machinify, where I help automate healthcare-payments claims. It did what the first two essays promised. It compounded. After a few months it could answer "why did we decide this, and what did we learn" in seconds, in my own voice, with citations to the exact pages.

Then the bill came. Six weeks of Claude Code spend, $4,700. Not from the thinking. From the loading. My setup followed the obvious instruction sitting at the top of every session: read the wiki index, then read what you need. As the wiki grew, "read the index" quietly turned into "drag the whole catalog, plus the relevant memory, plus the skill descriptions, into the model's working memory before the first question is even asked." The corpus had outgrown the pattern that built it.

So the question that produced this essay is a money question before it is an architecture question. How do you keep a brain that compounds from becoming a brain you cannot afford?

> The cost of a second brain should track how much you ask it, not how much it knows. The naive pattern couples cost to corpus size, which is exactly backwards, because the entire point is for the corpus to grow. The fix is to stop pre-loading and start retrieving just in time. That one change turns an expensive brain into a mesh that stays cheap as it scales.

## § 01 · The bill that broke the pattern.

Here is what $4,700 buys you if you are not careful. Every new session began by loading the index of the whole wiki, the slice of long-term memory the harness thought might be relevant, and a catalog of every skill the agent could call. That payload went into the system prompt, the part of the request that gets written to cache and then read back on every turn. Cache-write and cache-read costs dominated the bill. I was paying the full corpus tax at the start of every conversation, before a single useful question had been answered, and the tax went up every week because the corpus went up every week.

That is the eager-load pattern, and it has a fatal property: cost scales with the size of what you know, not with the number of things you ask. A wiki that is succeeding, growing denser and more valuable, is a wiki whose per-session bill is climbing for no reason the user can see. The system punishes you for the exact behavior it is supposed to reward.

## § 02 · Context is RAM, not disk.

The deeper reason eager-load is wrong is not financial. It is that pre-loading makes the model worse at the thing in front of it.

Use Karpathy's framing. The model is a processor, the context window is RAM, the filesystem is disk, and the agent is a long-running program. You do not copy the whole disk into RAM on the chance you will need it. You page in what the current operation requires and nothing more. The context window is scarce working memory, not storage.

And it is scarce in a way that bites. Anthropic, writing about context engineering for agents, calls context a finite resource with an attention budget: as the token count rises, the model's ability to accurately recall any particular fact in that context degrades. It is a gradient, not a cliff, but it is real and measured. So pre-loading "just in case" is wrong twice over. You pay for tokens the question does not need, and you spend the model's attention budget on noise, which makes it less accurate on the question you actually asked. The discipline that fixes both at once is the whole game here: put into context the smallest set of high-signal tokens that the next step needs, and leave the rest on disk.

## § 03 · Three layers: raw, cache, canon.

The architecture separates knowledge by two axes that the eager-load pattern ignores: how durable it is, and how much you trust it. Three layers fall out.

**L1, raw.** The source artifacts. Slack threads, calendar entries, meeting transcripts, the documents other people wrote. The agent reads these but never rewrites them. They are the system of record you replay from when the higher layers come up short.

**L2, cache.** A session-volatile semantic memory. I use Trivia, an open-source agent-memory store. Its clever move is that it embeds the *mnemonic*, a short "what this is about" descriptor, rather than the full content, so a search matches the aboutness of a memory and the embedding cost stays flat as memories pile up. It auto-merges near-duplicates. It is a fast, fuzzy scratchpad for a single conversation. It is explicitly not canon.

**L3, canon.** The curated markdown wiki. Typed atomic notes, dense cross-links, written in my voice, durable. This is the source of truth. The agent reads it freely and writes to it only through a gate, which is the next section.

The read path runs top down by trust. The agent asks canon first. If canon is thin on the question, it falls back to the L2 cache. It replays raw L1 only when neither higher layer can answer. And one hard rule holds the whole structure together: **no parallel canonical.** The cache is a cache. The day it quietly becomes a second source of truth competing with the wiki, you have split your curation budget in half and you now maintain two stores that drift apart. L1 is the replay, L2 is the cache, L3 is the canon. They are not interchangeable, and conflating them is how every multi-tier knowledge system has ever died.

## § 04 · The JIT contract.

The change that fixed the bill is a single paragraph in the agent's operating manual.

The old paragraph said: at session start, read the index. The new one says: at session start, read nothing. When a question needs domain knowledge, call `wiki_search`. Read only the genuine hits, in full, with `wiki_read`. When the lineage of a decision matters, walk the typed links with `wiki_traverse`. At the end of the turn, rate the files that actually helped, and the ones that were loaded but missed, with `wiki_rate`, which feeds the ranking. Page titles are cheap identifiers that live in the search index. Full pages load only on a hit.

This is the same pattern the rest of the field landed on in the same year. Frontier agents now keep lightweight identifiers, file paths and stored queries, and load the underlying content into context at runtime through tools, discovering what they need by exploration instead of front-loading it. The difference it makes to the bill is the difference between paying for a library card and buying the whole library every time you have a question.

## § 05 · The machinery, all commodity.

None of this is exotic, which is the point. It has to be inspectable to be trustworthy.

A small server exposes five tools to the agent over the Model Context Protocol: search, read, traverse, rate, and recent-changes. It is a couple hundred lines of Python.

Behind it sits a search engine that is deliberately *file-level*, not chunk-based RAG. It runs three tiers: a plain substring scan, then cosine similarity over whole-file embeddings, then a cross-encoder reranker for precision on the short list. It returns whole files, never fragments. The research backs the choice. A 2025 finding showed that fixed-size chunks match or beat "smart" semantic chunking, which means the gains in retrieval were never about shredding documents more cleverly. They are about retrieving coherent ones. A whole note carries its own context. Three chunks of it do not.

Writes to canon go through a propose-don't-act gate. The agent drafts proposed notes into a sandbox, and I approve before anything becomes canonical. The agent does the clerical labor it is good at. I keep authorship of what my wiki actually claims.

And rather than downgrade my main session to save money, I route the routable work to cheaper models: a mechanical subagent on the cheapest tier for shell commands and small reads, a synthesis subagent on the middle tier for multi-file summarizing, and the top tier reserved for architecture and judgment. Cost discipline by dispatch, not by dumbing down the front door.

Every layer is plain text, plain SQLite, plain Python. I can read it, grep it, version it, and fix it by hand. There is no embedding space I cannot open and no vendor format I cannot leave.

## § 06 · What it cost, and what it costs now.

The JIT contract pulled per-session context from over 80KB down under 30KB. Search returns in well under half a second. And the spend that ran $4,700 over six weeks before the change has dropped below its $2,800 target and kept going: in June I am tracking under $2,000, *while the corpus keeps growing*.

That last clause is the entire thesis. Under eager-load, growth and cost rise together, so success is expensive. Under the mesh, I can add a thousand notes and the cost of any single question barely moves, because the question still loads only the handful of pages it touches. Cost is bounded by query volume, not corpus size. The brain is now allowed to get as big as it wants.

## § 07 · A brain becomes a mesh.

Here is the leap that names the thing.

One person's just-in-time wiki is a brain. But because page titles are cheap and full pages load only on demand, there is no reason the agent has to traverse a single wiki. Point it at many, one per person, one per role, and it can answer across all of them at the moment a question is asked, still paying only for the pages that question touches. That is the mesh: N wikis, owned by N people, traversed by one agent. The cost math that makes a single brain affordable is precisely what makes a hundred brains affordable.

And that is the unshipped white space. Single-person LLM wikis are proven. Multi-source agent retrieval is proven. Nobody has yet shipped many wikis, owned by many people, traversed by one shared agent, as an organization's memory. The reason it has not happened is that the obvious way to build it, load everything so the agent can reason across it, is exactly the eager-load pattern that does not survive contact with a real corpus, let alone a hundred of them. The just-in-time architecture is what makes a mesh not merely possible but cheap.

## § 08 · The question this leaves open.

The mesh makes a compounding second brain affordable, first for a person and, as the next essay argues, for a whole company. But cheap self-maintenance raises a question this essay has not answered. If the agent is rating files, drafting canon, and pruning sessions on its own, how do you know the maintenance is making the knowledge *better* rather than just *different*? An agent that quietly optimizes for "answers that get rated useful" instead of "answers that are correct" would look, from the inside, exactly like one that is improving. Hold that thought. It is the subject of [The Measured Mind](/essays/the-measured-mind). First, what the mesh becomes when an entire organization runs it: [The Org Proof](/essays/the-org-proof).

---

*Written from Northern Colorado, 5,000 ft. Source at [philmora/essays](https://github.com/philmora/essays). CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
