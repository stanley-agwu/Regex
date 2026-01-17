# Negative Look Ahead

# A negative lookahead asserts the regex to match if the regexp 
# ahead is not matching.

# regex_1(?!regex_2)

"""
The negative lookahead (?!) asserts regex_1 not to be immediately 
followed by regex_2. Lookahead is excluded from the match 
(do not consume matches of regex_2), but only assert whether a match 
is possible or not.
"""

"""
Task

You have a test String S.
Write a regex which can match all characters which are not immediately followed by that same character.

Example

If S = goooo, then regex should match goooo. Because the first g is not follwed by g and the last o is not followed by o.
"""

import re

pattern = r"(.)(?!\1)"

match = re.match(pattern, "goooooo.") is not None
match2 = re.match(pattern, "set off") is not None

print(str(match))
print(str(match2))
