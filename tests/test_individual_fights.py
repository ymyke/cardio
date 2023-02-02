from typing import List, Optional
from cardio import Card, Skill, session
from cardio.computer_strategies import Round0OnlyStrategy

# FIXME Should this rather be test_skills?


def do_the_fight(
    humancard: Optional[Card],
    computercard: Optional[Card],
    playerhand: Optional[List[Card]] = None,
) -> None:
    session.setup()
    session.humanplayer.deck.cards = playerhand or []
    cs = Round0OnlyStrategy(
        grid=session.grid, cards=[((1, 0), computercard), ((2, 0), humancard)]  # type: ignore
    )
    session.view.handle_fight(computerstrategy=cs)


def test_vanilla_fight():
    hc = Card("Human Card", 2, 10, 1)
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight(hc, cc)
    assert hc.power == 2
    assert hc.health == 8
    assert cc.power == 2
    assert cc.health == 0
    assert session.humanplayer.gems == 1
    assert session.grid[1][0] is None


def test_vanilla_with_power_0():
    """Should fail immediately bc human has no chance to win bc all her cards are
    powerless.
    """
    hc = Card("Human Card", 0, 10, 1)
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight(hc, cc)
    assert hc.health == 10  # full health remaining
    assert cc.health == 3
    assert session.humanplayer.lives == 0
    assert session.grid[2][0] is hc  # card remains in grid


def test_vanilla_with_power_0_and_additional_card_in_hand():
    """In contrast to  to `test_vanilla_with_power_0`, here the human has an additional
    card w power in her hand, therefore the fight shoud take place and the card in the
    grid suffer damage and vanish.
    """
    hc = Card("Human Card", 0, 10, 1)
    hc2 = Card("Human Card 2", 1, 10, 1)
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight(hc, cc, playerhand=[hc2])
    assert hc.health == 0  # health depleted
    assert cc.health == 3
    assert session.humanplayer.lives == 0
    assert session.grid[2][0] is None  # human card removed from grid


def test_vanilla_with_no_opponent():
    hc = Card("Human Card", 1, 10, 1)
    do_the_fight(hc, None)
    assert hc.health == 10


def test_instant_death():
    hc = Card("Human Card", 1, 10, 1, skills=[Skill.INSTANTDEATH])
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight(hc, cc)
    assert hc.health == 10
    assert cc.health == 0
    assert session.grid[1][0] is None


def test_soaring():
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING])
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight(hc, cc)
    # 12 not 10, bc fight-over conditions are checked after each line gets activated:
    assert hc.health == 12
    assert cc.health == 3
    assert session.grid[1][0] is cc


def test_soaring_vs_airdefense():
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING])
    cc = Card("Computer Card", 2, 3, 1, skills=[Skill.AIRDEFENSE])
    do_the_fight(hc, cc)
    assert hc.health == 16
    assert cc.health == 0
    assert session.grid[1][0] is None


def test_soaring_and_instantdeath_vs_airdefense():
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING, Skill.INSTANTDEATH])
    cc = Card("Computer Card", 2, 3, 1, skills=[Skill.AIRDEFENSE])
    do_the_fight(hc, cc)
    assert hc.health == 20
    assert cc.health == 0
    assert session.grid[1][0] is None


def test_soaring_and_instantdeath_vs_no_airdefense():
    """INSTANTDEATH should have no effect and computer card should not suffer any damage
    at all bc of SOARING.
    """
    hc = Card("Human Card", 1, 20, 1, skills=[Skill.SOARING, Skill.INSTANTDEATH])
    cc = Card("Computer Card", 2, 3, 1)
    do_the_fight(hc, cc)
    # 12 not 10, bc fight-over conditions are checked after each line gets activated:
    assert hc.health == 12
    assert cc.health == 3
    assert session.grid[1][0] is cc


def test_spines():
    hc = Card("Human Card", 2, 10, 1)
    cc = Card("Computer Card", 2, 3, 1, skills=[Skill.SPINES])
    do_the_fight(hc, cc)
    assert hc.health == 6
    assert cc.health == 0
    assert session.grid[1][0] is None


def test_spines_resulting_in_both_cards_dying_simultaneously():
    hc = Card("Human Card", 1, 1, 1)
    cc = Card("Computer Card", 0, 1, 1, skills=[Skill.SPINES])
    do_the_fight(hc, cc)
    assert hc.health == 0
    assert cc.health == 0
    assert session.grid[1][0] is None
    assert session.grid[2][0] is None
    assert session.humanplayer.lives == 0
