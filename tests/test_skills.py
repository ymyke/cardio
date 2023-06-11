"""Tests for skills.

These tests rely on the `_fc` attribute being present in the `Card` class in order to
access the `FightCard` instance that was created for the fight and to verify that the
card's attributes such as health have been update correctly.
"""

import random
from typing import Optional
import pytest
from cardio import Card, CardList, gg, GridPos, skills, Grid
from cardio.computer_strategies import Round0OnlyStrategy
from cardio.fightcard import FightCard
from tests.utils.humanstrategyvnc import HumanStrategyVnC


@pytest.fixture(autouse=True)
def common_setup(mocker, request, gg_setup):
    if "skip_common_setup" in request.keywords:
        return


def do_the_fight(humancards: CardList, computercard: Optional[Card]) -> tuple:
    """Note that the assumption here is that `HumanStrategyVnC` will place new cards on
    the first free slot from the left, i.e., the very first human card gets placed on
    (2,0).
    """
    gg.humanplayer.deck.cards = humancards
    # Reset grid for good measure in case we run several fights in one test:
    grid = Grid(4)
    cs = Round0OnlyStrategy(grid=grid, cards=[(GridPos(1, 0), computercard)])
    gg.vnc = HumanStrategyVnC(grid=grid, computerstrategy=cs, whichrounds=[0])
    gg.vnc.handle_fight()
    return grid, gg.vnc.stateslogger


def test_vanilla_fight():
    hc = Card("Human Card", 3, 10, 1)
    cc = Card("Computer Card", 2, 5, 1)
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.power == 3
    assert hc._fc.health == 8
    assert cc._fc.power == 2
    assert cc._fc.health == 0
    assert gg.humanplayer.gems == 2
    assert grid[1][0] is None


def test_instant_death():
    hc = Card("Human Card", 1, 10, 1, skills=[skills.InstantDeath])
    cc = Card("Computer Card", 2, 3, 1)
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 10
    assert cc._fc.health == 0
    assert grid[1][0] is None


def test_soaring():
    hc = Card("Human Card", 1, 20, 1, skills=[skills.Soaring])
    cc = Card("Computer Card", 2, 3, 1)
    grid, _ = do_the_fight([hc], cc)
    # 12 not 10, bc fight-over conditions are checked after each line gets activated:
    assert hc._fc.health == 12
    assert cc._fc.health == 3
    assert grid[1][0] is cc._fc


def test_soaring_vs_airdefense():
    hc = Card("Human Card", 1, 20, 1, skills=[skills.Soaring])
    cc = Card("Computer Card", 2, 3, 1, skills=[skills.Airdefense])
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 16
    assert cc._fc.health == 0
    assert grid[1][0] is None


def test_soaring_and_instantdeath_vs_airdefense():
    hc = Card("Human Card", 1, 20, 1, skills=[skills.Soaring, skills.InstantDeath])
    cc = Card("Computer Card", 2, 3, 1, skills=[skills.Airdefense])
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 20
    assert cc._fc.health == 0
    assert grid[1][0] is None


def test_soaring_and_instantdeath_vs_no_airdefense():
    """INSTANTDEATH should have no effect and computer card should not suffer any damage
    at all bc of SOARING.
    """
    hc = Card("Human Card", 1, 20, 1, skills=[skills.Soaring, skills.InstantDeath])
    cc = Card("Computer Card", 2, 3, 1)
    grid, _ = do_the_fight([hc], cc)
    # 12 not 10, bc fight-over conditions are checked after each line gets activated:
    assert hc._fc.health == 12
    assert cc._fc.health == 3
    assert grid[1][0] is cc._fc


def test_spines():
    hc = Card("Human Card", 2, 10, 1)
    cc = Card("Computer Card", 2, 3, 1, skills=[skills.Spines])
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 6
    assert cc._fc.health == 0
    assert grid[1][0] is None


def test_spines_resulting_in_both_cards_dying_simultaneously():
    hc = Card("Human Card", 1, 1, 1)
    cc = Card("Computer Card", 0, 1, 1, skills=[skills.Spines])
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 0
    assert cc._fc.health == 0
    assert grid[1][0] is None
    assert grid[2][0] is None
    assert gg.humanplayer.lives == 1


def test_fertility():
    hc = Card("Human Card", 1, 1, 0, skills=[skills.Fertility])
    cc = Card("Computer Card", 1, 2, 1)
    do_the_fight([hc], cc)
    # The original card must be used:
    assert hc._fc in gg.vnc.decks.used.cards
    assert hc._fc.health == 0
    # The copy should be in the hand deck:
    non_hamsters_on_hand = [c for c in gg.vnc.decks.hand.cards if c.name != "Hamster"]
    assert len(non_hamsters_on_hand) == 1
    copy = non_hamsters_on_hand[0]
    assert isinstance(copy, FightCard)
    assert copy.name == "Human Card"
    assert copy.health == 1  # Make sure the health was reset
    assert copy.skills.get_types() == [skills.Fertility]
    # The copy should _not_ be in the player's main deck, since it is a temporary card:
    assert copy not in gg.humanplayer.deck.cards


def test_shield():
    # FIXME Once we have skills that break the shield, add that as a test case.

    # With shield:
    # The human card will survive bc the shield absorbs 1 damage in each round.
    hc = Card("Human Card", 2, 4, 1, skills=[skills.Shield])
    cc = Card("Computer Card", 2, 7, 1)
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 1
    assert cc._fc.health == 0
    assert grid[1][0] is None
    assert grid[2][0] is hc._fc
    assert hc._fc.skills.get(skills.Shield)._turns_used == [0, 1, 2]

    # Without shield:
    # The human card will die bc it no longer has the shield and therefore takes 2
    # damage per round.
    hc = Card("Human Card", 2, 4, 1)
    cc = Card("Computer Card", 2, 7, 1)
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 0
    assert cc._fc.health == 3
    assert grid[1][0] is cc._fc
    assert grid[2][0] is None

    # With shield and spines:
    # The human card will die bc while the shield absorbs 1 damage in each round, the
    # spines deal another damage, which will not be absorbed.
    hc = Card("Human Card", 2, 4, 1, skills=[skills.Shield])
    cc = Card("Computer Card", 2, 7, 1, skills=[skills.Spines])
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 0
    assert cc._fc.health == 3
    assert grid[1][0] is cc._fc
    assert grid[2][0] is None


def test_shield_resets_at_start_of_fight(mocker):
    def fake_post_init(self):
        self._turns_used = [0, 1, 2]

    post_init_orig = skills.Shield.__post_init__
    skills.Shield.__post_init__ = fake_post_init
    hc = Card("Human Card", 2, 4, 1, skills=[skills.Shield])
    cc = Card("Computer Card", 2, 7, 1)
    grid, _ = do_the_fight([hc], cc)
    assert hc._fc.health == 1
    assert cc._fc.health == 0
    assert grid[1][0] is None
    assert grid[2][0] is hc._fc
    assert hc._fc.skills.get(skills.Shield)._turns_used == [0, 1, 2]
    skills.Shield.__post_init__ = post_init_orig


def test_shield_deadlock():
    hc = Card("Procupine", 1, 2, 1, skills=[skills.Airdefense, skills.Shield])
    cc = hc.copy()
    do_the_fight([hc], cc)
    assert gg.vnc.damagestate.is_deadlocked()


def test_underdog():
    # With Underdog:
    hc = Card("Human Card", 1, 1, 1, skills=[skills.Underdog])
    cc = Card("Computer Card", 2, 2, 1)
    do_the_fight([hc], cc)
    assert hc._fc.health == 1  # hc wins bc it gets +1 power from Underdog
    assert cc._fc.health == 0

    # Without Underdog:
    hc = Card("Human Card", 1, 1, 1)
    cc = Card("Computer Card", 2, 2, 1)
    do_the_fight([hc], cc)
    assert hc._fc.health == 0
    assert cc._fc.health == 1  # cc wins bc it has more power


def test_packrat():
    # With Packrat:
    hc = Card("Human Card", 1, 1, 1, skills=[skills.Packrat])
    xc = Card("X", 1, 1, 1)
    cc = Card("Computer Card", 1, 2, 1)
    # 3 cards will get drawn at the beginning of the fight:
    _, log = do_the_fight([hc, hc.copy(), hc.copy(), xc], cc)
    assert "Draw: Xp1h1" in log.log.split("Starting round")[1]
    # `xc` gets drawn ealier:
    assert "Draw: Xp1h1" not in log.log.split("Starting round")[2]

    # Without Packrat:
    hc = Card("Human Card", 1, 1, 1)
    xc = Card("X", 1, 1, 1)
    cc = Card("Computer Card", 1, 2, 1)
    _, log = do_the_fight([hc, hc.copy(), hc.copy(), xc], cc)
    assert "Draw: Xp1h1" in log.log.split("Starting round")[1]
    assert "Draw: Xp1h1" in log.log.split("Starting round")[2]
    # `xc` gets drawn one round later:
    assert "Draw: Xp1h1" not in log.log.split("Starting round")[3]


def test_luckystrike():
    # LuckyStrike gets unlucky and kills itself:
    random.seed(0)
    hc = Card("Human Card", 10, 10, 1, skills=[skills.LuckyStrike])
    cc = Card("Computer Card", 1, 1, 1)
    do_the_fight([hc], cc)
    assert hc._fc.health == 0  # `hc` should have died immediately

    # LuckyStrike gets lucky and kills the opponent:
    random.seed(1)
    hc = Card("Human Card", 1, 1, 1, skills=[skills.LuckyStrike])
    cc = Card("Computer Card", 10, 10, 1)
    do_the_fight([hc], cc)
    assert cc._fc.health == 0  # `cc` should have died immediately

    # LuckyStrike gets lucky, but no opposing card:
    # (Computer will be defeated immediately bc `hc` has 3 power, which will get
    # doubled, for a power of 6.)
    random.seed(1)
    hc = Card("Human Card", 3, 1, 1, skills=[skills.LuckyStrike])
    _, log = do_the_fight([hc], None)
    assert hc._fc.health == 1  # `hc` should have survived
    assert "-6 damage," in log.log.split("Starting round")[1]


# TODO Add tests that directly test the more complex classes such as Shield and
# LuckyStrike. -- Also, add this step to the checklist in skills.py
