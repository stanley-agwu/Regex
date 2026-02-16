# Detect HTML Links

"""
Charlie has been given an assignment by his Professor to strip the links and 
the text name from the html pages. A html link is of the form:

<a href="http://www.hackerrank.com">HackerRank</a>  
Where a is the tag and href is an attribute which holds the link charlie is 
interested in. The text name is HackerRank.

Charlie notices that the text name can sometimes be hidden within multiple 
tags:

<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
Here, the text name is hidden inside the tags h1 and b.

Help Charlie in listing all the links and the text name of the links.

Input Format:
The first line contains the number of lines in the fragment (N). 
This is followed by N lines from a valid HTML document or fragment.
Constraints:

N < 100
Number of characters in the test fragments <= 10000 characters.
Characters will be restricted to ASCII. Fragments for the tests will be picked up from Wikipedia. Also, some tests might not have text or names on the links.

Output Format:
If there are M links in the document, display each of them in a new line. The link and the text name must be separated by a "," (comma) with no spaces between them.
Strip out any extra spaces at the start and end position of both the link and the text name before printing.

link-1,text name-1
link-2,text name-2
link-3,text name-3
....
link-n,text name-M
Sample Input

Sample Input:1

2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

Sample Input:2

13
<div class="portal" role="navigation" id='p-navigation'>
<h3>Navigation</h3>
<div class="body">
<ul>
 <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>
 <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>
 <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>
<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>
<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>
<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>
</ul>
</div>
</div>    

Sample Output

Sample Output:1
http://www.quackit.com/html/tutorial/html_links.cfm,Example Link
http://www.quackit.com/html/examples/html_links_examples.cfm,More Link Examples...

Sample Output:2
/wiki/Main_Page,Main page
/wiki/Portal:Contents,Contents
/wiki/Portal:Featured_content,Featured content
/wiki/Portal:Current_events,Current events
/wiki/Special:Random,Random article
//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en,Donate to Wikipedia    
"""

# Key idea
"""
1. Find each anchor block: <a ... href="..."> ... </a>
2. Extract the href
3. Remove all tags inside the anchor content to get plain text
4. Normalize whitespace (turn multiple spaces/newlines into a single space)
"""

import re
import sys

def strip_tags(html: str) -> str:
    # Remove tags, then normalize whitespace
    text = re.sub(r'<[^>]+>', '', html)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    n = int(sys.stdin.readline().strip())
    html = ''.join(sys.stdin.readline() for _ in range(n))

    # Capture:
    #   group(1) = href value (double-quoted)
    #   group(2) = inner HTML between <a ...> and </a> (can include nested tags/newlines)
    pattern = re.compile(
        r'<a\b[^>]*\bhref="([^"]*)"[^>]*>(.*?)</a>',
        re.IGNORECASE | re.DOTALL
    )

    for href, inner in pattern.findall(html):
        name = strip_tags(inner)
        print(f"{href.strip()},{name}")

if __name__ == "__main__":
    main()

def detect_links():
    n = int(sys.stdin.readline().strip())
    html = "\n".join(sys.stdin.readline().rstrip("\n") for _ in range(n))

    # 1) capture href + inner content (supports " or ' quotes, supports nested tags)
    a_pat = re.compile(r'<a\b[^>]*\bhref\s*=\s*(["\'])(.*?)\1[^>]*>(.*?)</a>', re.I | re.S)

    # 2) remove any tags from inside anchor to get visible text
    tag_pat = re.compile(r'<[^>]+>')

    for _, href, inner in a_pat.findall(html):
        text = tag_pat.sub('', inner)          # strip nested tags
        text = re.sub(r'\s+', ' ', text).strip()  # normalize whitespace + trim
        href = href.strip()
        print(f"{href},{text}")

