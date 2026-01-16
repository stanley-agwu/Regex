# Forward References

# Back reference to a group which appear later in regex

# NOTE - Forward reference is supported by JGsoft, .NET, Java, Perl, PCRE, 
#           PHP, Delphi and Ruby regex flavors.

"""
Forward reference creates a back reference to a regex that would appear later.
Forward references are only useful if they're inside a repeated group.
Then there may arise a case in which the regex engine evaluates the 
backreference after the group has been matched already.
"""

"""
Task

You have a test string S.
Your task is to write a regex which will match S, with following condition(s):

- S consists of tic or tac.
- tic should not be immediate neighbour of itself.
- The first tic must occur only when tac has appeared at least twice before.

Valid 
    tactactic
    tactactictactic

Invalid 
    tactactictactictictac
    tactictac
"""

import re

pattern = r"^(?:tac){2}(?:tac|tic(?=tac|$))*$"

"""
(?=tac|$) — positive lookahead
A positive lookahead checks what's immediately next in the string without consuming it.
(?=tac|$) means:

Right after the characters tic, the next characters must be either:
- tac (i.e., the next token is tac)
- OR end of string $
"""

match = re.match(pattern, "tactactictactictactictactactic") is not None
match2 = re.match(pattern, "tactactictactictic") is not None

print(str(match))
print(str(match2))