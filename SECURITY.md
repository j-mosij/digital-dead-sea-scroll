# Security & IP Protection

**Copyright (c) 2026 jeremiahnmosij (j-mosij). All rights reserved under CC BY-NC-ND 4.0.**

## Strict Rules for Anyone Copying or Adding

- This repository and its contents (code, corpus, generated fragments, designs, ontology of Nux and Null) are original work.
- No unauthorized copying, forking for redistribution, derivative distribution, or commercial use is permitted.
- Attribution is mandatory if sharing the unmodified original.
- Do not remove copyright notices, license headers, or this SECURITY.md.
- Violations will be addressed (including DMCA notices where applicable).
- Contributions must preserve the original design intent and will be reviewed for IP compliance. No external code may be added without explicit approval.

## Security Posture

- Pure local / offline by design. No network calls, no telemetry, no external dependencies at runtime.
- No client-server surface exists. If a client/server is ever added:
  - Keep secrets and private keys out of the public repo.
  - Prefer a private repository for any authenticated or key-bearing components, with a public documentation-only mirror if needed.
  - Use authentication, input sanitization, and post-quantum cryptography (PQC) for any key exchange or long-term protection.
- Continuous injection checks run on every push/PR via GitHub Actions (scans for `eval`, `exec`, `os.system`, `subprocess`, `__import__`, and similar). Builds fail on detection.
- Optional future encryption of outputs can use pure-Python or PQC libraries; current outputs are plaintext fragments.

## Dependencies & Anonymity

- Runtime: Python 3 standard library only (zero external packages).
- Optional / future: post-quantum crypto (e.g., for key encapsulation), JSON config files for parameters, and full offline/anonymous operation (no phone-home).
- See `requirements.txt` for the current empty runtime list and notes.

## Reporting

Security issues or IP concerns: open a private issue or contact the owner directly. Do not post exploit details publicly.
