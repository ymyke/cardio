# Great resource: https://www.hillelwayne.com/post/property-testing-complex-inputs/

from hypothesis import given, settings, HealthCheck, Verbosity, assume
import hypothesis.strategies as st
from cardio.card import Card
import cardio.session as session
import cardio.handlers as handlers
from cardio.agent_strategies import Turn0OnlyStrategy


def slotlist_strategy():
    return st.lists(
        st.one_of(
            st.builds(
                Card,
                initial_power=st.integers(min_value=0, max_value=100),
                initial_health=st.integers(min_value=0, max_value=100),
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
def test_game_hypo(mocker, slotlist):
    # We want at least one card with power that is not in the prepper line in order to
    # prevent an endless loop when running the game:
    # FIXME The requirement re the prepper line can be relaxed once there is code in
    # place that makes cards from the prepper line.
    assume(any(c.power > 0 for c in slotlist[4:] if c is not None))

    session.setup()
    mocker.patch("cardio.session.view")  # Deactivate the view to improve performance

    # FIXME No need to use the humanstrategy -- can do everything with the
    # computerstrategy!!

    before_nof_cards = len([c for c in slotlist if c is not None])
    cs = Turn0OnlyStrategy([((i // 4, i % 4), c) for i, c in enumerate(slotlist)])
    handlers.handle_fight(computerstrategy=cs)
    after_nof_cards = len([c for slots in session.grid for c in slots if c is not None])

    assert after_nof_cards <= before_nof_cards
    if after_nof_cards < before_nof_cards:
        session.view.update.assert_called()
        session.view.activate_card.assert_called()
        session.view.get_attacked.assert_called()