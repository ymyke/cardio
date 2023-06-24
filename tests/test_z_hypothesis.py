# Great resource: https://www.hillelwayne.com/post/property-testing-complex-inputs/

import itertools
from hypothesis import given, settings, HealthCheck, Verbosity
import hypothesis.strategies as st
from cardio import Card, FightVnC, skills
from cardio.computer_strategies import Round0OnlyStrategy

all_skill_subsets = []
for i in range(len(skills.get_skilltypes()) + 1):
    for subset in itertools.combinations(skills.get_skilltypes(), i):
        all_skill_subsets.append(subset)


def slotlist_strategy():
    return st.lists(
        st.one_of(
            st.builds(
                Card,
                name=st.text(min_size=1),
                power=st.integers(min_value=0, max_value=100),
                health=st.integers(min_value=0, max_value=100),
                costs_fire=st.integers(min_value=0, max_value=100),
                skills=st.sampled_from(all_skill_subsets),
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
def test_game_hypo(mocker, tt_setup, slotlist):
    # Need to reset the following two variables because hypothesis won't rerun fixtures:
    # See also https://hypothesis.works/articles/hypothesis-pytest-fixtures/
    human, grid, vnc, _ = tt_setup
    vnc = FightVnC(grid, None, human)
    card_activate_spy = mocker.spy(vnc, "show_card_activate")

    before_nof_cards = len([c for c in slotlist if c is not None])
    pos_and_cards = [((i // 4, i % 4), c) for i, c in enumerate(slotlist)]
    vnc.computerstrategy = Round0OnlyStrategy(grid=grid, cards=pos_and_cards)

    # Print the cards: (Use `pytest -vv -s` to show output.)
    for pos, c in pos_and_cards:
        cardstr = f"{c.power}/{c.health}" if c is not None else "None"
        print(f"{pos}: {cardstr:7s}", end=" | ")
        if pos[1] == 3:
            print()
    print()

    vnc.handle_fight()
    after_nof_cards = len([c for slots in grid for c in slots if c is not None])

    assert after_nof_cards <= before_nof_cards
    if after_nof_cards < before_nof_cards:
        card_activate_spy.assert_called()
