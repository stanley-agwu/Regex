# Capturing and Non-Capturing Group

# Capturing Group - ()
"""
Parenthesis ( ) around a regular expression can group that part of regex 
together. This allows us to apply different quantifiers to that group.
These parenthesis also create a numbered capturing. It stores the part of 
string matched by the part of regex inside parentheses.
These numbered capturing can be used for backreferences.
"""

# Non-Capturing Group - (?: )
"""
(?: ) can be used to create a non-capturing group. It is useful if we do 
not need the group to capture its match.
"""

# NOTE:
# In Group, \. -> Literal dot (.) E.g (?: Mr\.)
# In Character class . -> Literal dot (.) E.g [Mr.]

"""
Task

You have a test String S.

Your task is to write a regex which will match  with the following condition:

- S should have 3 or more consecutive repetitions of ok.
"""

import re

pattern = r"(?:ok){3,}"

match = re.match(pattern, "okokok cyan!") is not None
match2 = re.match(pattern, "okok") is not None

print(str(match))
print(str(match2))


# If the entire string must be ONLY those repetitions
# Use anchors:

pattern = r"^(?:ok){3,}$"

match3 = re.match(pattern, "okokokokok") is not None
match4 = re.match(pattern, "okokokok free") is not None

print(str(match3))
print(str(match4))