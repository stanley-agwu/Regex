# Matching Start and End

# The ^ symbol matches the position at the start of a string.
# The $ symbol matches the position at the end of a string.
# These are anchors --> [^, $]

"""
Task

You have a test string S. Your task is to match the pattern Xxxxx
Here, x denotes a word character, and X denotes a digit.
S must start with a digit X and end with . symbol.
S should be 6 characters long only.
"""

import re

pattern = r"^\d\w{4}\.$"

match = re.match(pattern, "2abc_.") is not None
match2 = re.match(pattern, "2hfgd.") is not None

print(str(match))
print(str(match2))