# Negative Look Behind

# It asserts the regex to match if regexp behind is not matching.

# (?<!regex_2)regex_1

"""
The negative lookbehind (?<!) asserts regex_1 not to be immediately preceded by regex_2. 
Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert 
whether a match is possible or not.
"""

"""
Task

You have a test String S.

Write a regex which can match all the occurences of characters which are not 
immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).
"""

import re

pattern = r"(?<![aeiouAEIOU])."

match = re.match(pattern, "lols") is not None
match2 = re.match(pattern, "fright") is not None

print(str(match))
print(str(match2))

