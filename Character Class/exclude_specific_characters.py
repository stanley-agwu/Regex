# Excluding Specific Characters

# [^]
# The negated character class [^] matches any character that is not in 
# the square brackets.

"""
Task

You have a test string .
Your task is to write a regex that will match S with the following conditions:

- S must be of length 6.
- First character should not be a digit (1, 2, 3, 4, 5, 6, 7, 8, 9 or 0).
- Second character should not be a lowercase vowel (a, e, i, o or u).
- Third character should not be b, c, D or F.
- Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
- Fifth character should not be a uppercase vowel (A, E, I, O or U).
- Sixth character should not be a . or , symbol.
"""

import re

pattern = r"^\D[^aeiou][^bcDF][^\r\n\t\f][^AEIOU][^\.,]$"

match = re.match(pattern, "think?") is not None
match2 = re.match(pattern, "friend") is not None

print(str(match))
print(str(match2))