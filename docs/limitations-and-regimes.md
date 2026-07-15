# Limitations And Regimes

## Known Limitations

the simulator can overstate opportunity value when queue position, stale quotes, fill uncertainty, or cancel latency are ignored. This limitation is not a footnote; it should determine how the model is used. A clean
implementation can still produce misleading research if the market regime is mislabeled.

## Regime Checklist

- Opening auction and first continuous-trading minutes
- Midday low-liquidity drift
- Closing auction and rebalance pressure
- Earnings, macro releases, and unscheduled news
- Volatility expansion and spread widening
- Venue-specific behavior and quote-staleness windows

## Promotion Rule

The model should not be treated as a final signal engine. It is a measurement component that becomes
more valuable when combined with point-in-time validation, transaction-cost modeling, and explicit
regime labels. A promoted version should include model version, data version, parameters, validation
report, and a human-readable decision memo.

## Practical Use

The safest public use is educational and diagnostic: inspect whether the feature behaves as expected
on controlled inputs, then use that behavior as a foundation for larger private experiments.
