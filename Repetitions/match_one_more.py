# Matching One or More Repetitions

# The + tool will match one or more repetitions of character/character class/group.

"""
For Example:

w+ : It will match the character w 1 or more times.
[xyz]+ : It will match the character x, y or z 1 or more times.
\d+ : It will match any digit 1 or more times.
"""

"""
Task

You have a test string S.
Your task is to write a regex that will match  using the following conditions:

- S should begin with 1 or more digits.
- After that, S should have 1 or more uppercase letters.
- S should end with 1 or more lowercase letters
"""

import re

pattern = r"^\d+[A-Z]+[a-z]+$"

match = re.match(pattern, "36Qr") is not None
match2 = re.match(pattern, "4Q") is not None

print(str(match))
print(str(match2))