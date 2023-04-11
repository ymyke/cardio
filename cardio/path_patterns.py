# LIXME: (2-3/3-2 etc. could also be mirrored rather than duplicated.)

from typing import List, NamedTuple


class PathPattern(NamedTuple):
    paths: List[List[int]]
    pattern: str


PATH_PATTERNS = {
    "1-1": [
        PathPattern(
            paths=[[0]],
            pattern="""
    xxx
     |    
     |
     |
     |
     |
    xxx    
""",
        )
    ],
    "1-2": [
        PathPattern(
            paths=[[0, 1]],
            pattern="""
xxx     xxx
 |       |
 |       |
 +--+ +--+
    | |   
    | |   
    xxx    
""",
        )
    ],
    "2-1": [
        PathPattern(
            paths=[[0], [0]],
            pattern="""
    xxx    
    | |   
    | |   
 +--+ +--+
 |       |
 |       |
xxx     xxx
""",
        )
    ],
    "2-2": [
        PathPattern(
            paths=[[0], [1]],
            pattern="""
xxx     xxx
 |       |
 |       |
 |       |
 |       |
 |       |
xxx     xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [1]],
            pattern="""
xxx     xxx
 |      ||
 |      ||
 |+-----+|
 ||      |
 ||      |
xxx     xxx
""",
        ),
        PathPattern(
            paths=[[0], [0, 1]],
            pattern="""
xxx     xxx
 ||      |
 ||      |
 |+-----+|
 |      ||
 |      ||
xxx     xxx
""",
        ),
    ],
    "2-3": [
        PathPattern(
            paths=[[0], [1, 2]],
            pattern="""
xxx xxx xxx
 |   |   |
 |   |   |
 |   +--+|
 |      ||
 |      ||
xxx     xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [2]],
            pattern="""
xxx xxx xxx
 |   |   |
 |   |   |
 |+--+   |
 ||      |
 ||      |
xxx     xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [1, 2]],
            pattern="""
xxx xxx xxx
 |  | |  |
 |  | |  |
 |+-+ +-+|
 ||     ||
 ||     ||
xxx     xxx
""",
        ),
        PathPattern(
            paths=[[0, 1, 2], [2]],
            pattern="""
xxx xxx xxx
|    |  ||
|+---+  || 
||+-----+| 
|||      | 
|||      | 
xxx     xxx
""",
        ),
        PathPattern(
            paths=[[0], [0, 1, 2]],
            pattern="""
xxx xxx xxx
 ||  |    |
 ||  +---+|
 |+-----+||
 |      |||
 |      |||
xxx     xxx
""",
        ),
    ],
    "3-2": [
        PathPattern(
            paths=[[0], [1], [1]],
            pattern="""
xxx     xxx
 |      ||
 |      ||
 |   +--+|
 |   |   |
 |   |   |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [0], [1]],
            pattern="""
xxx     xxx
 ||      |
 ||      |
 |+--+   |
 |   |   |
 |   |   |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [0, 1], [1]],
            pattern="""
xxx     xxx
 ||     ||
 ||     ||
 |+-+ +-+|
 |  | |  |
 |  | |  |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [0], [0, 1]],
            pattern="""
xxx     xxx
|||      | 
|||      | 
||+-----+| 
|+---+  || 
|    |  ||
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [1], [1]],
            pattern="""
xxx     xxx
 |      |||
 |      |||
 |+-----+||
 ||  +---+|
 ||  |    |
xxx xxx xxx
""",
        ),
    ],
    "1-3": [
        PathPattern(
            paths=[[0, 1, 2]],
            pattern="""
xxx xxx xxx
 |   |   |
 |   |   |
 +--+++--+
    |||   
    |||   
    xxx    
""",
        )
    ],
    "3-1": [
        PathPattern(
            paths=[[0], [0], [0]],
            pattern="""
    xxx    
    |||   
    |||   
 +--+++--+
 |   |   |
 |   |   |
xxx xxx xxx
""",
        )
    ],
    "3-3": [
        PathPattern(
            paths=[[0], [1], [2]],
            pattern="""
xxx xxx xxx
 |   |   |
 |   |   |
 |   |   |
 |   |   |
 |   |   |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [1], [2]],
            pattern="""
xxx xxx xxx
 |  ||   |
 |  ||   |
 |+-+|   |
 ||  |   |
 ||  |   |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [1, 2], [2]],
            pattern="""
xxx xxx xxx
 |  ||  ||
 |  ||  ||
 |+-+|+-+|
 ||  ||  |
 ||  ||  |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [0, 1], [2]],
            pattern="""
xxx xxx xxx
 ||  |   |
 ||  |   |
 |+-+|   |
 |  ||   |
 |  ||   |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [1], [1, 2]],
            pattern="""
xxx xxx xxx
 |   ||  |
 |   ||  |
 |   |+-+|
 |   |  ||
 |   |  ||
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [1, 2], [2]],
            pattern="""
xxx xxx xxx
 |   |  ||
 |   |  ||
 |   |+-+|
 |   ||  |
 |   ||  |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [0, 1], [1, 2]],
            pattern="""
xxx xxx xxx
 ||  ||  |
 ||  ||  |
 |+-+|+-+|
 |  ||  ||
 |  ||  ||
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0], [0, 1, 2], [2]],
            pattern="""
xxx xxx xxx
 ||  |  ||
 ||  |  ||
 |+-+|+-+|
 |  |||  |
 |  |||  |
xxx xxx xxx
""",
        ),
        PathPattern(
            paths=[[0, 1], [1], [1, 2]],
            pattern="""
xxx xxx xxx
 |  |||  |
 |  |||  |
 |+-+|+-+|
 ||  |  ||
 ||  |  ||
xxx xxx xxx
""",
        ),
    ],
}
