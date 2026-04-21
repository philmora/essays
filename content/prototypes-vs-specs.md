---
slug: prototypes-vs-specs
title: "Prototypes > <em>Specs</em>."
dek: "The working thing ends the meeting. A short argument for showing before telling, in a field that is addicted to telling."
date: 2026-01-22
reading_time: 7
hero_image: ocean-sunrise.png
tags: [product, shipping]
published: true
order: 1
---

A working thing ends the meeting. Even a half-broken one ends most meetings, because the room finally has the same picture in their heads. A document never quite does that.

This isn't anti-document. It's anti-substituting documents for things that should be prototypes. There's a difference, and the cost of getting it wrong used to be high. Now it's nearly zero.

## § 01 · What the working thing does.

Put five product people in a room with a PRD and you will get five interpretations. Each person reads the document and builds a slightly different picture in their head. The meeting is mostly spent reconciling those pictures — catching the person who thought it was a blue button when it should be orange, the one who assumed the workflow was linear when it's branching, the one who didn't notice the edge case on page three.

Put the same five people in a room with a *working prototype* and the picture is the same for everyone. It's right there. They can click it. They can see what happens. The meeting isn't about reconciling interpretations; it's about deciding what to change. You went from "does everyone agree what we're building" to "does everyone agree we should ship this" in one step.

The working thing isn't better because it's more detailed. Specs can be arbitrarily detailed. The working thing is better because it *forecloses ambiguity*. A sentence has interpretations. A button has behavior. You can argue about what a sentence means; you can't argue about what happens when you click the button. The button either does the thing or it doesn't.

This is not a new observation. Linus famously said "talk is cheap, show me the code." Design studios have known this forever — you don't brief a client on a typography choice, you show them the typography. What's new is that this principle now applies to everything, because everything is now cheap to prototype.

## § 02 · Why we got addicted to telling.

The spec-heavy culture of modern software teams made sense for a reason that no longer applies.

The reason: prototypes used to be expensive. Building even a non-functional mockup of a real workflow took a designer half a week. Building a working prototype took an engineer longer than that. At a big company, with dozens of stakeholders, the cost of prototyping-to-consensus was high enough that it was cheaper to write the spec, argue about the spec, update the spec, argue again, and only then build.

That math was correct, for fifteen years. The spec was the cheap proxy for the expensive build.

But the cost of the build collapsed. Not gradually — it collapsed. An engineer with Cursor can mock a workflow in an hour that would have taken a week in 2020. A PM with Framer or v0 can prototype a UI over lunch. A designer with any modern tool can produce a working animated interaction during the meeting they were called into. The proxy for the expensive build is now more expensive than the build itself.

We know this, and we still write specs. Why?

Because the *culture* of writing specs is a load-bearing part of how large companies make decisions. Specs are not just prototypes; they are political documents. They distribute accountability. They let the exec sign off on something that can later be pointed to. They create a paper trail that survives turnover. They are, in their honest form, bureaucratic instruments.

There's nothing wrong with bureaucracy for the things it's good for. There's a lot wrong with using it as a substitute for seeing the actual thing. The spec is *not the product*. The meeting about the spec is not progress. Every hour spent writing, circulating, and debating a spec is an hour the working thing could have been built, shown, and argued about on its own terms.

## § 03 · How to prototype in the new regime.

Three rules I've landed on, after a year of trying to make prototyping the default:

**1. If a piece of work is going to take less than two days to prototype, don't spec it. Prototype it first, then write the spec from the prototype.** Reversing the order matters. The prototype reveals the hard questions. The spec then answers them with specific language. A spec written from a prototype is a better spec than one written from imagination, because imagination skips over the parts you didn't think about.

**2. If the spec is longer than the prototype would take, you are writing the wrong thing.** I have seen 30-page PRDs for features that could be prototyped in a single afternoon. This is not diligence. This is displacement activity. The team is writing a spec because writing is comfortable and building is scary. Fix the fear, don't pad the document.

**3. When you can't prototype it — because it touches core infrastructure, or has regulatory implications, or requires customer access you don't have — write a spec that explicitly says why.** Most specs hide the reason they're specs. The good ones name it. "Prototype not possible because we need PHI access to test, so here's the written argument for the proposed design" is a better spec than "Here is the proposed design." The first tells you why the document exists. The second pretends the document is the point.

These rules imply something uncomfortable: most of the specs your team wrote last quarter should have been prototypes. The work will come out better if you run this experiment for a few weeks.

## § 04 · What you still write specs for.

I said at the top this isn't anti-document. Let me close with the cases where specs are still the right tool.

- **Decisions with external commitments.** A contract with a vendor, a commitment to a customer, a regulatory filing. These require language, not clickable prototypes. The artifact is words on purpose.
- **Systems with strong compatibility requirements.** An API that other teams will build against. A data schema that outlives the team. A migration plan that will be executed by a stranger six months from now. These need written specs because the audience is *future humans*, not the current room.
- **The argument for *why*.** A prototype shows you what. It rarely shows you why. The case for doing something expensive, risky, or unusual requires written argument — a memo, a design doc, a decision log. The prototype supports the argument; the argument is the thing.
- **Retrospectives and decision records.** What did we build, why did we build it, what did we learn. This is a document, and it should be. Prototypes are transient; documents persist.

What these have in common: the *artifact is the point*. The document isn't a proxy for something that could have been built. The document is the deliverable. Write those. Write them well.

Everything else — the feature specs, the workflow designs, the UI mocks, the user flow diagrams — should be prototypes. Most of them would be better, faster, cheaper, and more decision-useful as prototypes. The tools are there. The cost is gone.

The working thing ends the meeting. Start building it instead of describing it.

—
*Written from Fort Collins, 5,000ft. Source at [philmora/essays](https://github.com/philmora/essays) · CC BY 4.0. Reach me: [hi@philmora.com](mailto:hi@philmora.com).*
