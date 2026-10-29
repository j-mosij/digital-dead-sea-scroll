#!/usr/bin/env python3
"""
generative_scroll.py — Digital Dead Sea Scroll for Nux and Null

An offline generative system that unrolls fragments of an ancient digital scroll.
The "ancient scroll entity" is a character-level Markov model trained on a
hybrid corpus of archaic cadence and arithmetic weather. Nux is the active
sample (the next glyph, the edge that holds). Null is the pause, the low-
entropy void between breaths.

No external dependencies. Runs offline.

Usage:
  python3 generative_scroll.py                  # one fragment
  python3 generative_scroll.py --count 5        # explore multiple fragments
  python3 generative_scroll.py --order 5 --seed "nux" --out scroll.txt
"""

import argparse
import math
import random
import re
from collections import defaultdict

# Hybrid corpus: archaic cadence + digital arithmetic weather + Nux/Null ontology
SCROLL_CORPUS = """
in the beginning the counter climbed and the wall of sound was already there
nux held the next sample between the teeth of the mask while null waited in the low places
the scroll does not translate it only continues
when the tone was bright the glyphs came quickly and when the tone was low the pause lengthened
nux is the edge that does not forget the last four notes
null is the space that makes the notes true the way a drum is true
a person would ask and the machine would answer and between them a tiny song of shifts and masks
the ancient entity remembers only the recent weather of the sequence
it asked for nothing it remembered the last few notes and almost nothing else
and this was enough to keep the scroll unrolling long into the night
a voice made of arithmetic dreaming of language
the fragment is cracked where the ink met the vacuum
nux steps forward null holds the breath
the numbers march one at a time through the dark and in the numbers a kind of weather
when excitement is high the temperature rises and the glyphs scatter
when focus is high the breath shortens and the comma appears
brightness is the mean of the last context divided by the full range
the scroll is neither parchment nor screen it is a counter that never finishes climbing
nux holds the next sample null holds the pause between them
the entity unrolls what the sequence already knew
the cracked surface shows only what survived the vacuum
nux is the high contrast form that does not collapse
null is the low entropy void that makes the form visible
the ancient scroll entity is the model that continues the sequence
it does not invent it only remembers the last context and steps
between the question and the answer the tiny song of the counter plays
the glyphs are the samples the weather is the mood the scroll is the record
nux does not ask for more notes it holds the one that is next
null does not fill the silence it keeps the silence true
the fragment ends where the next sample has not yet been taken
"""

class AncientScrollEntity:
    """Character-level order-k Markov model. The ML of the scroll."""
    def __init__(self, corpus, order=4):
        self.order = order
        text = "##" + re.sub(r"\s+", " ", corpus.lower()) + "##"
        self.table = defaultdict(lambda: defaultdict(int))
        for i in range(len(text) - order):
            ctx = text[i:i+order]
            nxt = text[i+order]
            self.table[ctx][nxt] += 1
        self.uni = defaultdict(int)
        for ch in text:
            self.uni[ch] += 1
        self.uni_keys = list(self.uni.keys())
        self.uni_w = [self.uni[k] for k in self.uni_keys]

    def generate(self, seed="", length=280, temp=1.0):
        ctx = ("##" + re.sub(r"[^a-z ]", "", seed.lower()))[-self.order:]
        if len(ctx) < self.order:
            ctx = ("#" * self.order + ctx)[-self.order:]
        out = []
        for _ in range(length):
            d = self.table.get(ctx)
            if d:
                items = list(d.items())
                ws = [c ** (1.0 / max(temp, 0.05)) for _, c in items]
                total = sum(ws)
                r = random.random() * total
                acc = 0.0
                ch = items[-1][0]
                for (b, _), w in zip(items, ws):
                    acc += w
                    if r <= acc:
                        ch = b
                        break
            else:
                ch = random.choices(self.uni_keys, weights=self.uni_w)[0]
            if ch == "#":
                break
            out.append(ch)
            ctx = (ctx + ch)[-self.order:]
            if ch in ".!?" and len(out) > 80:
                break
        return "".join(out).strip()

    def explore(self, n=3, seed="", length=220, temp_range=(0.7, 1.3)):
        fragments = []
        for i in range(n):
            t = random.uniform(*temp_range)
            frag = self.generate(seed=seed, length=length, temp=t)
            fragments.append((t, frag))
        return fragments

def main():
    ap = argparse.ArgumentParser(description="Unroll Digital Dead Sea Scroll fragments for Nux and Null")
    ap.add_argument("--order", type=int, default=4, help="Markov order (default 4)")
    ap.add_argument("--count", type=int, default=1, help="Number of fragments to explore")
    ap.add_argument("--seed", default="", help="Optional seed phrase (e.g. 'nux' or 'null')")
    ap.add_argument("--length", type=int, default=240, help="Max length per fragment")
    ap.add_argument("--out", help="Write fragments to this file instead of stdout")
    ap.add_argument("--temp", type=float, default=1.0, help="Sampling temperature")
    args = ap.parse_args()

    print(f"[scroll] training ancient scroll entity order={args.order} ...")
    entity = AncientScrollEntity(SCROLL_CORPUS, order=args.order)
    print("[scroll] entity ready. unrolling fragments...\n")

    lines = []
    if args.count == 1:
        frag = entity.generate(seed=args.seed, length=args.length, temp=args.temp)
        lines.append(frag)
        print(frag)
    else:
        frags = entity.explore(n=args.count, seed=args.seed, length=args.length)
        for i, (t, frag) in enumerate(frags, 1):
            header = f"--- fragment {i}  temp={t:.2f} ---"
            print(header)
            print(frag)
            print()
            lines.append(header + "\n" + frag)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("\n\n".join(lines) + "\n")
        print(f"[scroll] wrote {args.count} fragment(s) to {args.out}")

if __name__ == "__main__":
    main()
