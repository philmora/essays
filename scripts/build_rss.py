#!/usr/bin/env python3
"""Generate feed.xml (Atom) from essays.json. Run after publishing a new essay."""
import json, os, datetime, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "essays.json"
OUT = ROOT / "feed.xml"

SITE = "https://philmora.com"
AUTHOR_NAME = "Phil Mora"
AUTHOR_EMAIL = "hi@philmora.com"
FEED_TITLE = "Phil Mora · The Big Picture"
FEED_SUBTITLE = "Dispatches on builder-operators in the agent era. CC BY 4.0."

with open(INDEX, "r", encoding="utf-8") as f:
    data = json.load(f)

essays = sorted(
    (e for e in data["essays"] if e.get("published", True)),
    key=lambda e: e.get("order", 0),
    reverse=True,
)

now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def entry(e):
    slug = e["slug"]
    url = f"{SITE}/essays/{slug}"
    title = html.escape(e.get("title_plain") or e["title"])
    dek = html.escape(e.get("dek", ""))
    date = e.get("date", "2026-01-01")
    published = f"{date}T12:00:00Z"
    return f"""  <entry>
    <title>{title}</title>
    <link href="{url}" rel="alternate" />
    <id>{url}</id>
    <published>{published}</published>
    <updated>{published}</updated>
    <summary>{dek}</summary>
    <author>
      <name>{AUTHOR_NAME}</name>
      <email>{AUTHOR_EMAIL}</email>
    </author>
    <category term="{html.escape(e.get('tags', ['essay'])[0] if e.get('tags') else 'essay')}" />
    <rights>CC BY 4.0</rights>
  </entry>"""


feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>{FEED_TITLE}</title>
  <subtitle>{FEED_SUBTITLE}</subtitle>
  <link href="{SITE}/feed.xml" rel="self" />
  <link href="{SITE}" />
  <id>{SITE}/</id>
  <updated>{now}</updated>
  <author>
    <name>{AUTHOR_NAME}</name>
    <email>{AUTHOR_EMAIL}</email>
  </author>
  <rights>CC BY 4.0 — {AUTHOR_NAME}</rights>
{chr(10).join(entry(e) for e in essays)}
</feed>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(feed)

print(f"✓ RSS generated: {OUT} ({len(essays)} entries)")
