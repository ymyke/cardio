import pytest
from cardio.run import Run
from cardio.locations.location import Location


def test_get_locations():
    run = Run("someseed")
    locs = run.get_locations(10)
    assert all(isinstance(l, Location) for l in locs)

    # Same seed, same locations:
    run2 = Run("someseed")
    locs2 = run2.get_locations(10)
    assert all(isinstance(l, Location) for l in locs2)
    assert [l.paths for l in locs] == [l.paths for l in locs2]
    assert [l.id for l in locs] == [l.id for l in locs2]

    # Different seed, different locations:
    run3 = Run("some_NEW_seed")
    locs3 = run3.get_locations(10)
    assert all(isinstance(l, Location) for l in locs3)
    assert [l.paths for l in locs] != [l.paths for l in locs3]
    assert [l.id for l in locs] != [l.id for l in locs3]


def test_move_to():
    run = Run("0")

    # Valid move:
    goto_loc = run.get_locations(1)[0]
    run.move_to(goto_loc)
    assert run.get_current_location().id == goto_loc.id
    assert run.current_rung == 1
    assert run.current_index == 0

    # Invalid move:
    with pytest.raises(AssertionError):
        run.move_to(run.get_locations(3)[0])


def test_get_accessible_locations():
    run = Run("0")
    run.current_rung = 2
    run.current_index = 2
    assert [l.id for l in run.get_accessible_locations(5)] == [
        "UP*_3_1",
        "FFF_4_0",
        "FFF_5_0",
        "···_5_1",
        "SL⚀_5_2",
        "FFF_6_0",
        "···_6_1",
        "S→→_7_0",
    ]


def test_run_pattern():
    run = Run("0")

    target = """\
FFF               UP*     ← 3
 ||                | 
 ||                | 
 |+-------+        | 
 |        |        | 
 |        |        | 
UHU      FFF      ···     ← 2
 |        |        | 
 |        |        | 
 +-------+++-------+ 
         |||         
         |||         
         UP*              ← 1
          |          
          |          
          |          
          |          
          |          
         ···              ← 0
"""
    assert run.get_string(0, 3, debug=True) == target
