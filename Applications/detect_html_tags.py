# Detect HTML Tags

"""
In this challenge, we're using regular expressions to detect the various 
tags used in an HTML document.

• Tags come in pairs. Some tag name, t, will have an opening tag, <t>, 
    followed by some intermediate text, followed by a closing tag, </t>. 
    The forward slash in a closing tag will always come before the tag name.
• The exception to this is self-closing tags, which consist of a single 
    tag (not a pair) with a forward slash after the tag name: <p/>

Here are a few examples of tags:
• The p tag is for paragraphs: <p>This is a paragraph</p>
• There may be 1 or more spaces before or after a tag name: 
    < p >This is also a paragraph</p>
• A void or empty tag involves an opening and closing tag with no 
    intermediate characters: <p></p>

Some tags can also have attributes, such as the a tag, which is used to add a hyperlink to another document:

<a href="http://www.google.com">Google</a>

In the above case, a is the tag name and href is an attribute having the value http://www.google.com.

Task

Given N lines of HTML, find the tag names (ignore any attributes) and print 
them as a single line of lexicographically ordered semicolon-separated values 
(e.g.: tag1;tag2;tag3).
Input Format

The first line contains an integer, N, the number of HTML fragments.

Each of the N subsequent lines contains a fragment of an HTML document.

Constraints

• 1 ≤ N ≤ 100
• Each fragment contains < 10000 ASCII characters.
• The fragments are chosen from Wikipedia, so analyzing and observing their markup structure may help.
• Leading and trailing spaces/indentation have been trimmed from the HTML fragments.

Output Format

Print a single line containing all of the unique tag names found in the input. Your output tags should be semicolon-separated and ordered lexicographically (i.e.: alphabetically). Do not print the same tag name more than once.
"""

# Key idea
"""
Find every opening or self-closing tag name and ignore:
1. attributes (class=..., href=...)
2. closing tags (</tag>)
3. special tags like comments/doctype (<!-- ... -->, <!DOCTYPE ...>)

A clean regex for the tag name is:
-> r"<\s*(?!/)([a-zA-Z0-9]+)"

Explanation:
-> <\s* matches < and optional spaces
-> (?!/) rejects closing tags </...
-> ([a-zA-Z0-9]+) captures the tag name
"""

import re
import sys

pattern = re.compile(r"<\s*(?!/)([a-zA-Z0-9]+)")

n = int(sys.stdin.readline().strip())
tags = set()

for _ in range(n):
    line = sys.stdin.readline().rstrip("\n")
    tags.update(pattern.findall(line))

print(";".join(sorted(tags)))
