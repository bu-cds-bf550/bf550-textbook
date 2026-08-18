#!/usr/bin/env python3
"""Compile chapter frontmatter into corpus.json for the (future) tutor skill."""
import re, json, glob, yaml

corpus = []
for path in sorted(glob.glob("chapters/*.qmd")):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if m:
        fm = yaml.safe_load(m.group(1))
        fm["path"] = path
        corpus.append(fm)
json.dump({"chapters": corpus}, open("corpus.json", "w"), indent=2)
print(f"corpus.json: {len(corpus)} chapters")
