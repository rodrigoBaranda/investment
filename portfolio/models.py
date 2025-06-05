from dataclasses import dataclass, field
from typing import List


@dataclass
class Holding:
    symbol: str
    shares: float
    price: float = 0.0


@dataclass
class Portfolio:
    holdings: List[Holding] = field(default_factory=list)
