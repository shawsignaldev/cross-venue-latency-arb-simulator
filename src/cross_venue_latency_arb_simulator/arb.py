from dataclasses import dataclass

@dataclass(frozen=True)
class VenueQuote:
    venue: str
    bid: float
    ask: float
    latency_us: float
    fee: float

def best_opportunity(quotes: list[VenueQuote], latency_penalty_per_us: float) -> dict[str, object] | None:
    best: dict[str, object] | None = None
    for buy in quotes:
        for sell in quotes:
            if buy.venue == sell.venue:
                continue
            edge = sell.bid - buy.ask - buy.fee - sell.fee - latency_penalty_per_us * (buy.latency_us + sell.latency_us)
            edge = round(edge, 6)
            if edge > 0 and (best is None or edge > best["edge"]):
                best = {"buy": buy.venue, "sell": sell.venue, "edge": edge}
    return best
