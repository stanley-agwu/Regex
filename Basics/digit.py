# Matching Digits and Non-Digits Characters

# The expression \d matches any digit [0 - 9].
# The expression \D matches any character that is not a digit.

import re

"""
Task

You have a test string S. Your task is to match the pattern xxXxxXxxxx
Here x denotes a digit character, and X denotes a non-digit character
"""

pattern = r"\d{2}\D\d{2}\D\d{4}"

match = re.match(pattern, "06-11-2015") is not None
match2 = re.match(pattern, "06-6-2015") is not None

print(str(match))
print(str(match2))
