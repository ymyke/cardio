from cardio.run import Run
from cardio.location import Location


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


def test_run_pattern():
    run = Run("0")

    target = """\
FFF               FFF     ← 3
 ||                | 
 ||                | 
 |+-------+        | 
 |        |        | 
 |        |        | 
···      FFF      ···     ← 2
 |        |        | 
 |        |        | 
 +-------+++-------+ 
         |||         
         |||         
         FFF              ← 1
          |          
          |          
          |          
          |          
          |          
         ···              ← 0
"""
    assert run.get_string(0, 3) == target
