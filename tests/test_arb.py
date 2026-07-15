from cross_venue_latency_arb_simulator.arb import VenueQuote, best_opportunity

def test_best_opportunity_finds_positive_latency_adjusted_edge() -> None:
    quotes = [
        VenueQuote("A", bid=100.00, ask=100.02, latency_us=10, fee=0.001),
        VenueQuote("B", bid=100.08, ask=100.10, latency_us=20, fee=0.001),
    ]
    result = best_opportunity(quotes, latency_penalty_per_us=0.0001)
    assert result == {"buy": "A", "sell": "B", "edge": 0.055}

def test_best_opportunity_returns_none_without_edge() -> None:
    assert best_opportunity([VenueQuote("A", 100, 101, 10, 0.01)], 0.001) is None
