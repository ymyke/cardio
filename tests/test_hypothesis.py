# Great resource: https://www.hillelwayne.com/post/property-testing-complex-inputs/

from hypothesis import given, settings, HealthCheck, Verbosity
import hypothesis.strategies as st
from cardio.card import Card
from cardio.grid import Grid, Line
import cardio.session as session
import cardio.handlers as handlers


def slotlist_strategy():
    return st.lists(
        st.one_of(
            st.builds(
                Card,
                initial_power=st.integers(min_value=0),
                initial_health=st.integers(min_value=0),
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
    # Set up session:
    session.bootstrap(prefill=False)
    mocker.patch("cardio.session.view")  # Deactivate the view to improve performance

    # Set up the grid:
    grid = Grid()
    grid.prepline = Line(4)
    grid.prepline.slots = slotlist[:4]
    grid.opponentline = Line(4)
    grid.opponentline.slots = slotlist[4:8]
    grid.playerline = Line(4)
    grid.playerline.slots = slotlist[8:]
    grid.lines = [grid.prepline, grid.opponentline, grid.playerline]
    session.grid = grid

    before_nof_cards = len([c for slots in grid for c in slots if c is not None])

    for _ in range(100):
        # FIXME Just run until game over once we have game over in place.
        handlers.handle_turn()

    after_nof_cards = len([c for slots in grid for c in slots if c is not None])

    assert after_nof_cards <= before_nof_cards
    if after_nof_cards < before_nof_cards:
        session.view.update.assert_called()
        session.view.activate_card.assert_called()
        session.view.get_attacked.assert_called()
