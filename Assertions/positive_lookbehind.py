# Positive Look Behind

# It asserts the regex to match if regexp behind is matching

# (?<=regex_2)regex_1

"""
The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2. 
Lookbehind is excluded from the match (do not consume matches of regex_2), 
but only assert whether a match is possible or not.
"""

"""
Task

You have a test String S.

Write a regex which can match all the occurences of digit which are immediately 
preceded by odd digit.
"""

import re

pattern = r"(?<=[13579])\d"

match = re.match(pattern, "0123456789") is not None
match2 = re.match(pattern, "1256Great") is not None

print(str(match))
print(str(match2))