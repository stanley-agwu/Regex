# Matching Word and Non-word Character

"""
\w
The expression \w will match any word character.
Word characters include alphanumeric characters (a-z, A-Z and 0-9) 
and underscores (_).

\W matches any non-word character.
Non-word characters include characters other than alphanumeric characters 
(a-z, A-Z and 0-9) and underscore (_).
"""
import re

"""
Task

You have a test string S. Your task is to match the pattern xxXxxxxxxxxxXxxx
Here x denotes any word character and X denotes any non-word character.
"""

pattern = r"\w{3}\W\w{9}\W\w{3}"

match = re.match(pattern, "www.microsoft.com") is not None
match2 = re.match(pattern, "www.google.com") is not None

print(str(match))
print(str(match2))
