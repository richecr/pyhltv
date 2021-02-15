# PyHltv

Repository to extract information from the HLTV website

### Table of contents

-   [Installation](#Installation)
-   [How to use](#how-to-use)
-   [Functions](#functions):
    -   [getMatches](###getMatches)

# Installation

It has not yet been published.

# How to use

```python3
# Import Matches features from the library
from py_hltv import Matches

# Return the List of Matches.
Matches.get_matches()
```

# Functions

### getMatches

> Gets all defined matches(https://www.hltv.org/matches). (1 request)

| Param | Type | Default | Description |
| ----- | ---- | ------- | ----------- |
| -     | -    | -       | -           |

```python3
# Import Matches features from the library
from py_hltv import Matches

# Return the List of Matches.
matches = Matches.get_matches()
print(matches)
```

See model [Matches](https://github.com/richecr/PyHltv/blob/master/py_hltv/models/Match.py)
