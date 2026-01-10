# Search Email, Phone Number Format and Match string

import re

email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|edu)"

def email_valid(str: str) -> str:
    return 'valid' if bool(re.search(email_pattern, str))\
        else 'In-valid'

print(email_valid("st@gmail.com"))
print(email_valid("stgmail.com"))
print(email_valid("st@gmailcom"))


int_phone_pattern = "(\d+)-(\d+)-(\d)"
phone_pattern = r"\1\2\3"

def format_phone_nr(number: str) -> str:
    return re.sub(int_phone_pattern, phone_pattern, number)

print(format_phone_nr('048-234-4567')) # 0482344567
print(format_phone_nr('234-834-4567')) # 2348344567


text = "The hackerrank team is on a mission to flatten the world by \
    restructuring the DNA of every company on the planet. We rank \
        programmers based on their coding skills, helping companies \
            source great programmers and reduce the time to hire. As " \
            "a result, we are revolutionizing the way companies discover \
                and evaluate talented engineers. The hackerrank platform \
                    is the destination for the best engineers to hone their \
                        skills and companies to find top engineers."
text_pattern = r"hackerrank"
result = re.findall(text_pattern, text)
print(f"result: {result}, Length: {len(result)}")

import re

txt = """There
aint much
rain in 
Spain"""

pattern = r"\b\w*ain\w*\b"

# Search for the sequence "ain", in the sentence:
print(re.findall(pattern, txt, re.MULTILINE)) # ['aint', 'rain', 'Spain']
