# Digital Dead Sea Scroll — Nux & Null

Offline generative system that unrolls fragments of an ancient digital scroll.

The **ancient scroll entity** is a character-level Markov model trained on a hybrid corpus of archaic cadence and arithmetic weather. It does not translate. It only continues.

- **Nux** holds the next sample — the edge, the active glyph, the high-contrast form that does not forget the last few notes.
- **Null** holds the pause — the low-entropy void between breaths, the space that makes the sequence true.

## Usage

```bash
python3 generative_scroll.py                  # one fragment
python3 generative_scroll.py --count 5        # explore multiple fragments
python3 generative_scroll.py --order 5 --seed "nux" --out scroll.txt
python3 generative_scroll.py --seed "null" --temp 0.8 --count 3
```

No dependencies beyond the Python standard library. Works offline.

## Ontology

The scroll is neither parchment nor screen. It is a counter that never finishes climbing.  
Nux steps forward. Null holds the breath.  
The entity unrolls what the sequence already knew.

## Related

Derived from the same arithmetic-weather lineage as bytebeat-trained sequence models. The mood of the context (excitement, focus, brightness) can later modulate temperature and breath if you wire this into a larger system.

---

*jeremiahnmosij — original work, not copied.*
