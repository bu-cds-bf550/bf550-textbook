#!/usr/bin/env python3
"""Lint chapter .qmd files against the conventions a machine can check.

Rules:
  L1  frontmatter parses and carries id, unit; exactly one H1, carrying {#sec-<id>}
      (title lives in the H1 only — a frontmatter title would render a duplicate heading)
  L2  every {python} chunk is <= 35 lines
  L3  any EXECUTED chunk that touches randomness constructs a seeded default_rng
      (eval: false exhibits are exempt -- there is no output to reproduce)
  L4  boundary tripwire: instructor-repo vocabulary must never appear here
  L5  register: no deception/agency metaphors for models, negations included
  L6  self-contained: every prerequisite a chapter declares is a concept (or id)
      introduced by an earlier-unit chapter -- nothing leans on outside background
"""
import re, sys, glob, yaml

MAX_CHUNK = 35
TRIPWIRE = re.compile(r"INSTRUCTOR NOTES|unseal|planted defect|AIAS [0-9]", re.I)
REGISTER = re.compile(r"\blies?\b|\blied\b|\blying\b|deceiv|\btricks? you\b|\bfools? you\b", re.I)
RANDOM = re.compile(r"np\.random|default_rng|\brng\b|random\.")
SEEDED = re.compile(r"default_rng\(\s*\d+\s*\)")

fail = 0
chapter_meta = []
for path in sorted(glob.glob("chapters/*.qmd")) + ["index.qmd"]:
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if path.startswith("chapters/"):
        if not m:
            print(f"L1 {path}: no frontmatter"); fail += 1; continue
        try:
            fm = yaml.safe_load(m.group(1))
            missing = [k for k in ("id", "unit") if k not in fm]
            if missing:
                print(f"L1 {path}: missing {missing}"); fail += 1
            if "title" in fm:
                print(f"L1 {path}: frontmatter title renders a duplicate heading — title lives in the H1"); fail += 1
            h1s = re.findall(r"^# .*$", text, re.M)
            if len(h1s) != 1 or f'{{#sec-{fm.get("id")}}}' not in h1s[0]:
                print(f"L1 {path}: need exactly one H1 ending {{#sec-{fm.get('id')}}}, found {len(h1s)}"); fail += 1
            chapter_meta.append((fm.get("unit", 99), path, fm))
        except yaml.YAMLError as e:
            print(f"L1 {path}: bad yaml: {e}"); fail += 1
    for chunk in re.findall(r"```\{python\}\n(.*?)```", text, re.S):
        lines = [l for l in chunk.splitlines() if not l.startswith("#|")]
        if len(lines) > MAX_CHUNK:
            print(f"L2 {path}: chunk of {len(lines)} lines (max {MAX_CHUNK})"); fail += 1
        executed = "#| eval: false" not in chunk
        if executed and RANDOM.search(chunk) and not SEEDED.search(chunk):
            print(f"L3 {path}: randomness without a seeded default_rng"); fail += 1
    hit = TRIPWIRE.search(text)
    if hit:
        print(f"L4 {path}: boundary tripwire: {hit.group(0)!r}"); fail += 1
    hit = REGISTER.search(text)
    if hit:
        print(f"L5 {path}: register (Box, not deception): {hit.group(0)!r}"); fail += 1

# L6: the concept graph -- prerequisites must be introduced by earlier units
ASSUMED = set()   # background allowed without introduction; grow deliberately, never casually
known = set(ASSUMED)
for unit, path, fm in sorted(chapter_meta):
    for prereq in fm.get("prerequisites") or []:
        if prereq not in known:
            print(f"L6 {path}: prerequisite {prereq!r} is not introduced by any earlier chapter"); fail += 1
    known.add(fm.get("id"))
    known.update(fm.get("concepts") or [])

sys.exit(1 if fail else print("lint: all clean") or 0)
