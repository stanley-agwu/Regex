# Positive Look Ahead

# A positive lookahead asserts the regex to match if the regexp 
# ahead is matching.

# regex_1(?=regex_2)
"""
The positive lookahead (?=) asserts regex_1 to be immediately followed by regex_2. 
The lookahead is excluded from the match. It does not return matches of regex_2. 
The lookahead only asserts whether a match is possible or not.
"""

"""
Task

You have a test string S.
Write a regex that can match all occurrences of o followed immediately 
by oo in S.
"""

import re

pattern = r"o(?=oo)"

match = re.match(pattern, "training ooo wooo gooofooo") is not None
match2 = re.match(pattern, "setooowooog ooo oooo") is not None
match3 = re.match(pattern, "oooooo") is not None

print(str(match))
print(str(match2))
print(str(match3))