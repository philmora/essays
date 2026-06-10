Seven essays on this blog argue that a second brain finally works, that the unit of knowledge is becoming the reasoning trace, that a mesh of small brains beats one big one, and that none of it is safe to automate until you can measure it. Arguments are cheap. As of last night, this one is a git clone.

## § 01 · The argument became a repo.

[github.com/philmora/compounding-mind](https://github.com/philmora/compounding-mind) is the working code behind this series: the search engine, the per-brain MCP servers, the evaluation harness, the publishing airlock, and an installer that is not a shell script wizard but a conversation. You clone it, run one bootstrap, open Claude Code, and say:

```bash
git clone https://github.com/philmora/compounding-mind && cd compounding-mind
./install/bootstrap.sh        # or --full for embeddings and the local judge
claude
> install my mesh
```

Claude does the rest: adopts your existing notes folder or scaffolds a fresh brain, indexes it, registers it as a search tool, then interviews you. Not a quiz about your files. Four to six plain questions about your rules: what must never happen, who approves changes, when the honest answer is "not covered." Your answers become the doctrine of your evaluation set, sealed with your authority, and the first baseline burns. From that moment your brain has a ruler, and every future change gets compared against it.

There is also a [condensed field guide as a gist](https://gist.github.com/philmora/8f73849c9c73ac3d4c077124474c5bd5) if you want the whole method on one page first.

## § 02 · Why the ruler ships in the box.

Every starter template in this genre ships the notes and skips the measurement. That is backwards, and The Measured Mind explains why at length: the moment an agent maintains your knowledge, rates what it retrieves, and promotes what it learns, you own a self-modifying system, and a self-modifying system improves toward whatever you measure. Measure nothing and it optimizes the only signal it has, which is its own usage. It gets more confident and more self-consistent, which is not the same as more correct, and from the inside those look identical.

So the kit treats evaluation as the product, not the test. Each brain carries a golden set: doctrine items only you can author, with canary tripwires for your hard rules; retrieval items verified against the actual corpus; one abstention item, because a brain that invents answers is worse than one that says it does not know. Retrieval is scored with boring, free, classical metrics on every change. Answers are graded for faithfulness by a small local judge of a different model family than the writer, frozen weights, fully reproducible, so nobody grades their own homework. Every run writes a ledger: golden version, answerer model, pinned system prompt, judge digest. When a number moves, you know whether your mesh got smarter or your rented model did.

## § 03 · The numbers that earned their place.

I did not trust any of this until it embarrassed me, repeatedly, in one afternoon.

The deployed keyword search scored a perfect zero on its first real exam. Twelve natural-language questions, twelve misses, on a system that had just passed its smoke test, because the smoke test asked in keywords and humans ask in questions. Token-level scoring fixed it; the fix moved the score from 0.00 to 0.71 MRR, and the eval caught a bug in itself along the way. Then the verdict flipped at scale: semantic retrieval, which lost to plain keywords on a 16-file brain, crushed them on every 100-plus-file brain, near zero against 0.87. The crossover sits around 18 files, the server now applies that policy automatically, and I would have argued the opposite from vibes. The field's newest memory benchmark says the architecture bet pays too: files read whole by an agent scored 72.5 percent where the strongest RAG baseline managed 48.5.

The judge had to audition for its job and failed it. Two local models, four prompt designs, and a correct paraphrase still got scored as a contradiction. So correctness grading stays human until a candidate passes five fixed control cases, faithfulness runs automated because it actually passes, and the audition harness ships in the box so your judge earns trust the same way.

And the publishing scanner caught three leaks before launch: two real ones sitting in an already-public repo, and then, on the final pre-push scan, me. The system flagged its own author's attribution because the gate does not care who you are. That last one is the point of the whole series in one anecdote.

## § 04 · What is deliberately not in the box.

The kit ships the two layers proven in my own fleet: the curated brains and the ruler. The optional session-cache layer has an excellent open-source drop-in, [Trivia](https://github.com/chrisdickinson/trivia), Chris Dickinson's semantic memory, his work not mine, and the mesh runs fine without it. The self-improvement layer everyone wants, nightly consolidation that proposes its own promotions, is designed, documented, and not shipped, because it has not yet proven itself against my own baselines. It will ship when it does, behind the same rule as everything else here.

The lineage is named where it is owed: the no-RAG, file-level, agent-as-librarian pattern is Andrej Karpathy's synthesis. This kit's contribution is the part the pattern was missing: the instrument that lets you trust it while it maintains itself.

## § 05 · Clone it.

Seven brains run on this on my machine: work, home, health, money, craft, the muse, this site. Yours will look different, which is the point; the installer interviews you, not me. Build the ruler first. Then let it compound.

[The repo](https://github.com/philmora/compounding-mind) · [the gist](https://gist.github.com/philmora/8f73849c9c73ac3d4c077124474c5bd5) · [start of the series](/essays/the-second-brain)
