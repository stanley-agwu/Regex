# Matching Ending Items

# The $ boundary matcher matches an occurrence of a character/character class/group at the end of a line.

"""
Task

Write a RegEx to match a test string, S, under the following conditions:

- S should consist of only lowercase and uppercase letters (no numbers or symbols).
- S should end in s.
"""

import re

pattern = r"^[a-zA-Z]*s$"

match = re.match(pattern, "Likes") is not None
match2 = re.match(pattern, "dog1s") is not None

print(str(match))
print(str(match2))