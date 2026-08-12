# AFF-003 — Claude generation-5 quality regression measurements

## Summary

A reproducible benchmark comparison reported substantially lower nonsense-detection performance for measured Claude generation-5 models than for selected generation-4.6/4.8 baselines, together with materially higher output-token usage in several matched configurations.

The full datasets, metric definitions, caveats, and reproduction scripts remain in the upstream issue. This case is only the durable index entry.

## Impact

Lower vigilance on plausible-sounding nonsense can degrade review, debugging, persistent-memory, and agentic workflows even when general capability remains high. Higher verbosity also increases latency, review burden, and token cost.

## Evidence level

**L4 — quantitatively measured / reproducible.**

The upstream issue reports repeatable benchmark runs, sample sizes, confidence intervals, metric definitions, and scripts used to reproduce the analysis.

## What is proven

- Public upstream issue `anthropics/claude-code#83510` was filed by `KeilerHirsch`.
- Identical BullshitBench prompts were evaluated across multiple Claude model generations and effort settings.
- The report separates strict nonsense detection, engagement, refusals, output tokens, and latency rather than collapsing them into one score.
- Both v1 (`n=55`) and v2 (`n=100`) datasets are reported with reproducible analysis scripts.
- The issue explicitly corrects or qualifies several third-party claims where public evidence was insufficient.

## What is not proven

- The measurements do not by themselves prove a specific internal post-training, RLHF, product, or marketing decision caused the regression.
- Grouped model-generation comparisons mix effort settings by design; per-model rows are the stronger primary evidence.
- Complaint-volume proxies and third-party reports are contextual evidence, not substitutes for the benchmark.
- Future model revisions may change the result.

## References

- Upstream: https://github.com/anthropics/claude-code/issues/83510
- Benchmark dataset: https://github.com/petergpt/bullshit-benchmark
- Analysis archive referenced by the upstream issue: https://gist.github.com/KeilerHirsch/5e212e6f9fb6fd670f191920eea4cb78
