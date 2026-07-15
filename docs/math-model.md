# Math Model

        ## Research Hypothesis

        Cross Venue Latency Arb Simulator starts from the hypothesis that cross-venue opportunities must be ranked after fees and latency decay, not by raw quote difference alone. The code in this repository is a compact
        executable reference model; this document describes the mathematical interpretation reviewers
        should use when reading the implementation.

        ## State Variables

        - `venue bid`
- `venue ask`
- `latency microseconds`
- `fees`
- `edge after latency penalty`

        These variables are intentionally observable from synthetic examples. A later private-data study
        should replace the toy inputs with point-in-time market data, venue metadata, and explicit session
        labels. The public model keeps the variables small so the assumptions can be inspected.

        ## Scoring Function

        The model maps a current market state into a normalized score or label. The score is not a trading
        instruction. It is a research measurement that can be ranked, stress-tested, and compared across
        regimes. Good use of the model requires tracking inputs, output, timestamp, session, and the
        exact parameter set that produced the result.

        ## Calibration

        Calibration should be performed out of sample. Parameters should be estimated on one period,
        frozen, and evaluated on later periods. Any update to thresholds, decay rates, or penalties should
        create a new experiment record rather than overwriting the old one.
