# Digital Dead Sea Scroll — Nux & Null

**Copyright (c) 2026 jeremiahnmosij. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) — no commercial use, no derivatives, attribution required.**

Offline generative system that unrolls fragments of an ancient digital scroll.

The **ancient scroll entity** is a character-level Markov model trained on a hybrid corpus of archaic cadence and arithmetic weather. It does not translate. It only continues.

- **Nux** holds the next sample — the edge, the active glyph, the high-contrast form that does not forget the last few notes.
- **Null** holds the pause — the low-entropy void between breaths, the space that makes the sequence true.

## New Designs

- Ancient scroll entity ML: pure character-level order-k Markov that continues the sequence rather than inventing. Trained only on the embedded hybrid corpus.
- Nux / Null ontology: Nux as the active next-sample edge; Null as the low-entropy pause that makes the sequence true. Explicitly modeled in corpus and generation.
- Arithmetic weather lineage: temperature, breath, and mood concepts drawn from the same family as bytebeat-trained sequence models.
- Cracked-fragment aesthetic: short corpus deliberately produces partially legible output, matching the digital Dead Sea Scroll metaphor (only what survived remains).
- Zero-dependency offline core: stdlib only, no network, no telemetry, fully anonymous by design.

## Usage

```bash
python3 generative_scroll.py                  # one fragment
python3 generative_scroll.py --count 5        # explore multiple fragments
python3 generative_scroll.py --order 5 --seed "nux" --out scroll.txt
python3 generative_scroll.py --seed "null" --temp 0.8 --count 3
```

No runtime dependencies beyond the Python standard library. Works offline.

## Dependencies

- Runtime: none (see `requirements.txt`).
- Optional future: post-quantum cryptography (PQC) for any key material, JSON configs, full anonymity guarantees.
- Continuous injection checks run on every push and pull request (`.github/workflows/security.yml`).

## Security & Protection

- Pure local script. No client-server surface. If one is added later, keep keys and secrets in a private repository and expose only documentation publicly.
- Strict IP rules in `LICENSE` and `SECURITY.md`. Unauthorized copying or derivative redistribution is prohibited.
- Builds fail if injection patterns (`eval`, `exec`, `os.system`, `subprocess`, etc.) are detected.

## Ontology

The scroll is neither parchment nor screen. It is a counter that never finishes climbing.  
Nux steps forward. Null holds the breath.  
The entity unrolls what the sequence already knew.

## Related

Derived from the same arithmetic-weather lineage as bytebeat-trained sequence models. The mood of the context (excitement, focus, brightness) can later modulate temperature and breath if you wire this into a larger system.

---

*jeremiahnmosij — original work, not copied. See LICENSE and SECURITY.md.*
