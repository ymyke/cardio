# TODO: Note, I know which columns are the "stretch" columns and can just multiply
# whichever character is at that position. – But does that also work with non-3-3
# patterns?

# (2-3/3-2 etc. could also be mirrored rather than duplicated.)

PATH_PATTERNS = {
    "1-1": [
        {
            "paths": [[0]],
            "pattern": """
    xxx    
     |
     |
     |
    xxx    
""",
        }
    ],
    "1-2": [
        {
            "paths": [[0, 1]],
            "pattern": """
xxx     xxx
 |       |
 +--+ +--+
    | |   
    xxx    
""",
        }
    ],
    "2-1": [
        {
            "paths": [[0], [0]],
            "pattern": """
    xxx    
    | |   
 +--+ +--+
 |       |
xxx     xxx
""",
        }
    ],
    "2-2": [
        {
            "paths": [[0], [1]],
            "pattern": """
xxx     xxx
 |       |
 |       |
 |       |
xxx     xxx
""",
        },
        {
            "paths": [[0, 1], [1]],
            "pattern": """
xxx     xxx
 |      ||
 |+-----+|
 ||      |
xxx     xxx
""",
        },
        {
            "paths": [[0], [0, 1]],
            "pattern": """
xxx     xxx
 ||      |
 |+-----+|
 |      ||
xxx     xxx
""",
        },
    ],
    "2-3": [
        {
            "paths": [[0], [1, 2]],
            "pattern": """
xxx xxx xxx
 |   |   |
 |   +--+|
 |      ||
xxx     xxx
""",
        },
        {
            "paths": [[0, 1], [2]],
            "pattern": """
xxx xxx xxx
 |   |   |
 |+--+   |
 ||      |
xxx     xxx
""",
        },
        {
            "paths": [[0, 1], [1, 2]],
            "pattern": """
xxx xxx xxx
 |  | |  |
 |+-+ +-+|
 ||     ||
xxx     xxx
""",
        },
        {
            "paths": [[0, 1, 2], [2]],
            "pattern": """
xxx xxx xxx
|+---+  || 
||+-----+| 
|||      | 
xxx     xxx
""",
        },
        {
            "paths": [[0], [0, 1, 2]],
            "pattern": """
xxx xxx xxx
 ||  +---+|
 |+-----+||
 |      |||
xxx     xxx
""",
        },
    ],
    "3-2": [
        {
            "paths": [[0], [1], [1]],
            "pattern": """
xxx     xxx
 |      ||
 |   +--+|
 |   |   |
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [0], [1]],
            "pattern": """
xxx     xxx
 ||      |
 |+--+   |
 |   |   |
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [0, 1], [1]],
            "pattern": """
xxx     xxx
 ||     ||
 |+-+ +-+|
 |  | |  |
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [0], [0, 1]],
            "pattern": """
xxx     xxx
|||      | 
||+-----+| 
|+---+  || 
xxx xxx xxx
""",
        },
        {
            "paths": [[0, 1], [1], [1]],
            "pattern": """
xxx     xxx
 |      |||
 |+-----+||
 ||  +---+|
xxx xxx xxx
""",
        },
    ],
    "1-3": [
        {
            "paths": [[0, 1, 2]],
            "pattern": """
xxx xxx xxx
 |   |   |
 +--+++--+
    |||   
    xxx    
""",
        }
    ],
    "3-1": [
        {
            "paths": [[0], [0], [0]],
            "pattern": """
    xxx    
    |||   
 +--+++--+
 |   |   |
xxx xxx xxx
""",
        }
    ],
    "3-3": [
        {
            "paths": [[0], [1], [2]],
            "pattern": """
xxx xxx xxx
 |   |   |
 |   |   |
 |   |   |
xxx xxx xxx
""",
        },
        {
            "paths": [[0, 1], [1], [2]],
            "pattern": """
xxx xxx xxx
 |  ||   |
 |+-+|   |
 ||  |   |
xxx xxx xxx
""",
        },
        {
            "paths": [[0, 1], [1, 2], [2]],
            "pattern": """
xxx xxx xxx
 |  ||  ||
 |+-+|+-+|
 ||  ||  |
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [0, 1], [2]],
            "pattern": """
xxx xxx xxx
 ||  |   |
 |+-+|   |
 |  ||   |
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [1], [1, 2]],
            "pattern": """
xxx xxx xxx
 |   ||  |
 |   |+-+|
 |   |  ||
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [1, 2], [2]],
            "pattern": """
xxx xxx xxx
 |   |  ||
 |   |+-+|
 |   ||  |
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [0, 1], [1, 2]],
            "pattern": """
xxx xxx xxx
 ||  ||  |
 |+-+|+-+|
 |  ||  ||
xxx xxx xxx
""",
        },
        {
            "paths": [[0], [0, 1, 2], [2]],
            "pattern": """
xxx xxx xxx
 ||  |  ||
 |+-+|+-+|
 |  |||  |
xxx xxx xxx
""",
        },
        {
            "paths": [[0, 1], [1], [1, 2]],
            "pattern": """
xxx xxx xxx
 |  |||  |
 |+-+|+-+|
 ||  |  ||
xxx xxx xxx
""",
        },
    ],
}
