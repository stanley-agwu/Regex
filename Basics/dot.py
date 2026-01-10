# Matching anything but a new line

# The dot (.) matches anything (except for a newline).

import re

"""
Task

You have a test string S.
Your task is to write a regular expression that matches only and exactly 
strings of form: abc.def.ghi.jkx, where each variable a, b, c, d, e, f, g, 
h, i, j, k, x, can be any single character except the newline.

"""

pattern = r"^.{3}\..{3}\..{3}\..{3}$"

match = re.match(pattern, "123.456.abc.def") is not None
match2 = re.match(pattern, "1234.456.abc.def") is not None

print(str(match))
print(str(match2))