from dataclasses import dataclass
from typing import List

@dataclass
class PortfolioModel:
    name: str
    symbols: List[str]
