from dataclasses import dataclass
from enum import Enum
from typing import List

# QQ: Maybe use a subclass such as TemporarySigil to implement things like temporary
# buffs like the power buff thanks to the Leader sigil.


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
        # QQ: Maybe REACHHIGH instead of AIRDEFENSE? With an arm symbol?
    )


SigilList = List[Sigil]

# Ideas for more sigils:
# - Poisonous? -> opponent gets poisoned and loses 1 health each round.
# - Viral? -> line poisonous, but spreads?
# - Pregnant? -> One-time fertility?
# - Persevering? / Final Blow? -> hits one more time in dying.
# - Healing? -> itself or others around it?
# - Annihilator? -> Destroys a card for good. Not just for this fight but for the entire
#   game. (Only makes sense for the human player maybe?)
# - Bless and curse or similar? -> Affect cards negatively or positively for an entire
#   run? E.g., poisoned or so, or added strength for cards left & right for longer than
#   a fight? -- That could be a way to be more strategic around building a deck. In the
#   negative cases, the player would try to get rid of a card. Or heal it?
# - Recruit? -- Recruit one of the opponent's cards that you killed at the end of the
#   fight.
