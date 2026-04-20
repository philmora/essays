# essays

Source for **The Big Picture** — essays on what happens when AI stops being a tool and starts being a teammate. Infrastructure, healthcare, organizational design, and the messy reality of building things that actually work.

Published at [philmora.com/thoughts](https://philmora.com/thoughts).

## How this works

Each essay lives as a single `.md` file in `content/`, with YAML front-matter for metadata. The `essays.json` index file lists them in publication order. The Framer site at philmora.com fetches both at runtime and renders them through a custom Markdown component (Terminal Aurora prose styles).

To publish an essay, push to `main`. To draft, push with `published: false`.

## Front-matter schema

```yaml
---
slug: the-pm-is-dead              # URL slug, must be unique
title: "The PM Is Dead. Long Live the Builder."
dek: "Something broke in the last six months..."
date: 2026-04-15                  # YYYY-MM-DD
reading_time: 14                  # minutes (rough estimate, manual)
hero_image: cosmic-journey.png    # filename in images/ or full URL
tags: [ai-agents, product, future-of-work]
published: true                   # false = drafted but not on site
order: 9                          # display order in /thoughts index (highest first)
---
```

Body is standard Markdown with a couple of Terminal Aurora conventions:

- `*emphasis*` renders as italic in **signal orange** (the brand accent)
- `**bold**` renders as serif 900-weight, no color shift
- Code blocks render in JetBrains Mono on a slightly inset background
- Pull quotes use `> ` (standard blockquote)

## License

All essay text is © Phil Mora and licensed [CC BY 4.0](LICENSE) — free to share, adapt, quote, with attribution. Code blocks, if any, are MIT.

## Contributing

Reading typos? Open an issue. Open a PR if you want to fix it directly.

This repo is the source of truth — please don't repost full essays elsewhere; link back instead. Adaptations and translations very welcome under the CC BY terms.
