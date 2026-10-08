# PrintCraft plugin

Prerelease **0.1.0-dev.6**: six digest-bound upstream skills plus a thin local Harness.
Independent execution/verification protocols preserve uncertain outcomes and require artifact review. Portable and generated Codex manifests share the product identity.

The upstream source is locked to a verified GitHub release, commit and 78 file digests. See project-status.json for publication status. Native sample, host, model-dispatch and release evidence remain separate.

See [中文说明](README.zh-CN.md), [host support](docs/host-support.md), [implementation evidence](docs/verification/implementation-2026-10-08.md), and [OpenSpec tasks](openspec/changes/harden-printcraft-plugin-delivery/tasks.md).

Install the prerelease after adding the marketplace:

```bash
codex plugin marketplace add partme-ai/full-aigc-plugins
codex plugin add printcraft@full-aigc-plugins
```

Codex is the tested host. ZCode/Kimi manifests are generated metadata; runtime and model acceptance are NOT_RUN. Chinese OCR, other native platforms and mobile delivery remain open.

Explicit optional Tesseract Chinese OCR is available through Harness `ocr`; pinned native OCR remains English-only. Native PDF reading order and full-phrase search have known limitations; see [Chinese OCR evidence](docs/verification/external-ocr-2026-10-08.md).
