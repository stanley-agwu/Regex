# Matching Whitespace and Non-Whitespace Character

# \s matches any whitespace character [ \r\n\t\f ].
# \S matches any non-white space character.

import re

"""
Task

You have a test string S. Your task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters, and X denotes non-white space characters.
"""

pattern = r"\S{2}\s\S{2}\s\S{2}"

match = re.match(pattern, "22 45 67") is not None
match2 = re.match(pattern, "44 55  67") is not None

print(str(match))
print(str(match2))
