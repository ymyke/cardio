# Great resource: https://www.hillelwayne.com/post/property-testing-complex-inputs/

from hypothesis import given, settings, HealthCheck, Verbosity, assume
import hypothesis.strategies as st
from cardio import Card, HumanPlayer, FightVnC
import cardio.gg as gg
from cardio.computer_strategies import Round0OnlyStrategy


def slotlist_strategy():
    return st.lists(
        st.one_of(
            st.builds(
                Card,
                name=st.text(min_size=1),
                initial_power=st.integers(min_value=0, max_value=100),
                initial_health=st.integers(min_value=0, max_value=100),
                costs_fire=st.integers(min_value=0, max_value=100),
                health=st.just(0),
                power=st.just(0),
            ),
            st.none(),
        ),
        min_size=3 * 4,
        max_size=3 * 4,
    )


@given(slotlist=slotlist_strategy())
@settings(
    suppress_health_check=[HealthCheck.function_scoped_fixture],
    verbosity=Verbosity.normal,
)
def test_game_hypo(mocker, session_setup, slotlist):
    # We want at least one card with power that is not in the prepper line in order to
    # prevent an endless loop when running the game:
    assume(any(c.power > 0 for c in slotlist[4:] if c is not None))

    # Need to reset the following two variables because hypothesis won't rerun fixtures:
    # See also https://hypothesis.works/articles/hypothesis-pytest-fixtures/
    gg.humanplayer = HumanPlayer(name="Schnuzgi", lives=1)
    gg.vnc = FightVnC(gg.grid, None)

    card_activate_spy = mocker.spy(gg.vnc, "card_activate")
    getting_attacked_spy = mocker.spy(gg.vnc, "card_getting_attacked")

    before_nof_cards = len([c for c in slotlist if c is not None])
    gg.vnc.computerstrategy = Round0OnlyStrategy(
        grid=gg.grid, cards=[((i // 4, i % 4), c) for i, c in enumerate(slotlist)]
    )
    gg.vnc.handle_fight()
    after_nof_cards = len([c for slots in gg.grid for c in slots if c is not None])

    assert after_nof_cards <= before_nof_cards
    if after_nof_cards < before_nof_cards:
        card_activate_spy.assert_called()
        getting_attacked_spy.assert_called()
