from typing import Optional
import pytest
from . import conftest
from cardio import Card, CardList, Skill, gg, GridPos
from cardio.computer_strategies import Round0OnlyStrategy
from cardio.humanstrategyvnc import HumanStrategyVnC


@pytest.fixture(autouse=True)
def common_setup(mocker, gg_setup):
    # Do not reset cards  so we can verify the effects of fights:
    mocker.patch("cardio.Deck.reset_cards")


def do_the_fight(humancards: CardList, computercard: Optional[Card]) -> None:
    """Note that the assumption here is that `HumanStrategyVnC` will place new cards on
    the first free slot from the left, i.e., the very first human card gets placed on
    (2,0).
    """
    gg.humanplayer.deck.cards = humancards
    cs = Round0OnlyStrategy(grid=gg.grid, cards=[(GridPos(1, 0), computercard)])
    gg.vnc = HumanStrategyVnC(grid=gg.grid, computerstrategy=cs, whichrounds=[0])
    gg.vnc.handle_fight()


def test_vanilla_fight():
    hc = Card("Human Card", 2, 10, 1)
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight([hc], cc)
    assert hc.power == 2
    assert hc.health == 8
    assert cc.power == 2
    assert cc.health == 0
    assert gg.humanplayer.gems == 1
    assert gg.grid[1][0] is None


def test_vanilla_with_power_0():
    """Should fail immediately bc human has no chance to win bc all her cards are
    powerless.
    """
    hc = Card("Human Card", 0, 10, 1)
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight([hc], cc)
    assert hc.health == 10  # full health remaining
    assert cc.health == 3
    assert gg.humanplayer.lives == 0
    assert gg.grid[2][0] is hc  # card remains in grid


def test_vanilla_with_power_0_and_additional_card_in_hand():
    """In contrast to  to `test_vanilla_with_power_0`, here the human has an additional
    card w power in her hand, therefore the fight shoud take place and the card in the
    grid suffer damage and vanish.
    """
    hc = Card("Human Card", 0, 10, 1)
    hc2 = Card("Human Card 2", 1, 10, 1)
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight([hc, hc2], cc)
    assert hc.health == 0  # health depleted
    assert cc.health == 3
    assert gg.humanplayer.lives == 0
    assert gg.grid[2][0] is None  # human card removed from grid


def test_vanilla_with_no_opponent():
    hc = Card("Human Card", 1, 10, 1)
    do_the_fight([hc], None)
    assert hc.health == 10


def test_instant_death():
    hc = Card("Human Card", 1, 10, 1, skills=[Skill.INSTANTDEATH])
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight([hc], cc)
    assert hc.health == 10
    assert cc.health == 0
    assert gg.grid[1][0] is None


def test_soaring():
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING])
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight([hc], cc)
    # 12 not 10, bc fight-over conditions are checked after each line gets activated:
    assert hc.health == 12
    assert cc.health == 3
    assert gg.grid[1][0] is cc


def test_soaring_vs_airdefense():
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING])
    cc = Card("Computer Card", 2, 3, 1, skills=[Skill.AIRDEFENSE])
    do_the_fight([hc], cc)
    assert hc.health == 16
    assert cc.health == 0
    assert gg.grid[1][0] is None


def test_soaring_and_instantdeath_vs_airdefense():
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING, Skill.INSTANTDEATH])
    cc = Card("Computer Card", 2, 3, 1, skills=[Skill.AIRDEFENSE])
    do_the_fight([hc], cc)
    assert hc.health == 20
    assert cc.health == 0
    assert gg.grid[1][0] is None


def test_soaring_and_instantdeath_vs_no_airdefense():
    """INSTANTDEATH should have no effect and computer card should not suffer any damage
    at all bc of SOARING.
    """
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING, Skill.INSTANTDEATH])
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight([hc], cc)
    # 12 not 10, bc fight-over conditions are checked after each line gets activated:
    assert hc.health == 12
    assert cc.health == 3
    assert gg.grid[1][0] is cc


def test_spines():
    hc = Card("Human Card", 2, 10, 1)
    cc = Card("Computer Card", 2, 3, 1, skills=[Skill.SPINES])
    do_the_fight([hc], cc)
    assert hc.health == 6
    assert cc.health == 0
    assert gg.grid[1][0] is None


def test_spines_resulting_in_both_cards_dying_simultaneously():
    hc = Card("Human Card", 1, 1, 1)
    cc = Card("Computer Card", 0, 1, 1, skills=[Skill.SPINES])
    do_the_fight([hc], cc)
    assert hc.health == 0
    assert cc.health == 0
    assert gg.grid[1][0] is None
    assert gg.grid[2][0] is None
    assert gg.humanplayer.lives == 0


def test_fertility():
    hc = Card("Human Card", 1, 1, 0, skills=[Skill.FERTILITY])
    cc = Card("Computer Card", 1, 2, 1)
    do_the_fight([hc], cc)
    # The original card must be used:
    assert hc in gg.vnc.decks.used.cards
    # The copy should be in the hand deck and it should be flagged as temporary:
    non_hamsters_on_hand = [c for c in gg.vnc.decks.hand.cards if c.name != "Hamster"]
    assert len(non_hamsters_on_hand) == 1
    copy = non_hamsters_on_hand[0]
    assert copy.name == "Human Card"
    assert copy.health == 1  # Make sure the health was reset
    assert copy.skills == [Skill.FERTILITY]
    assert copy.is_temporary
    # The copy should _not_ be in the player's main deck, since it is a temporary card:
    assert copy not in gg.humanplayer.deck.cards
