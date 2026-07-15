# Validation Protocol

## Goal

The validation goal is to determine whether Cross Venue Latency Arb Simulator measures a stable microstructure effect rather
than a fragile artifact of synthetic inputs. Passing unit tests proves deterministic behavior; it
does not prove economic usefulness.

## Required Checks

1. Point-in-time data handling: every feature must be available at or before the decision timestamp.
2. Session segmentation: opening, midday, close, auction, halt, and news periods should be reviewed separately.
3. Cost sensitivity: rankings should be rechecked after spread, fee, latency, and missed-fill assumptions.
4. Robustness: parameter changes should not completely reverse the result under small perturbations.
5. Replayability: every result should be reproducible from stored inputs and versioned parameters.

## Metrics

Useful validation metrics include hit rate, precision by score bucket, calibration error, turnover,
decay horizon, feature stability, and worst-regime degradation. For execution-facing models, missed
fills and adverse selection are as important as headline accuracy.

## Evidence Standard

A candidate should only be promoted when it passes unit tests, has an out-of-sample report, survives
basic transaction-cost assumptions, and has a written failure-mode review. Anything less should stay
in the research backlog.
