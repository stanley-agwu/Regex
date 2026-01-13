# Matching Word Boundaries

# \b assert position at a word boundary.
"""
Three different positions qualify for word boundaries :
► Before the first character in the string, if the first character is a 
    word character.
► Between two characters in the string, where one is a word character and 
    the other is not a word character.
► After the last character in the string, if the last character is a word 
    character.
"""

"""
Task

You have a test String S.

- Your task is to write a regex which will match word starting with vowel 
(a,e,i,o, u, A, E, I , O or U).
- The matched word can be of any length. The matched word should consist 
    of letters (lowercase and uppercase both) only.
The matched word must start and end with a word boundary.
"""

import re

pattern = r"\b[aeiouAEIOU][a-zA-Z]*\b"

match = re.match(pattern, "Umbrella") is not None
match2 = re.match(pattern, "ice-cream") is not None
match3 = re.match(pattern, "apple_cidar") is not None

print(str(match))
print(str(match2))
print(str(match3))