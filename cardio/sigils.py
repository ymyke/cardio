from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass(frozen=True)
class SigilSpec:
    name: str
    symbol: str
    description: str


class Sigil(Enum):
    INSTANTDEATH = SigilSpec(
        name="Instant Death",
        symbol="☠️",
        description="A card with Instant Death kills a card it damages in one hit. If the attack strikes the opponent directly, the sigil has no effect and the attack does damage according to its power, as usual. If a card has 0 Power, it will not attack and this sigil has no effect.",
    )
    FERTILITY = SigilSpec(
        name="Fertility",
        symbol="🐭",
        description="A fertile card creates a copy of itself in your hand when it is played.",
    )  # FIXME Still needs to be implemented when we have decks and a hand deck
    SOARING = SigilSpec(
        name="Soaring",
        symbol="🪁",
        description="A soaring card will ignore opposing cards and strike an opponent directly.",
    )
    SPINES = SigilSpec(
        name="Spines",
        symbol="🦔",
        description="When a card with spines is struck, the striker is dealt 1 damage.",
    )
    AIRDEFENSE = SigilSpec(
        name="Air Defense",
        symbol="🚀",
        description="A card with Air Defense blocks opposing Soaring creatures.",
    )


SigilList = List[Sigil]

# Ideas for more sigils:
# - Poisonous? -> opponent gets poisoned and loses 1 health each round.
# - Viral? -> line poisonous, but spreads?
# - Pregnant? -> One-time fertility?
