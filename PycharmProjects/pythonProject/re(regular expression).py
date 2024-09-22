# import re
# regular expression work with text data and search,match and manipulate    (read the all txt that i've entered)
# search is used to specific pattern of txt within large part or txt data search
# Data validation(valid email add , phone), Text extraction(data mining by extracting), parsing text files (pass txt file through configration and log file), pattern matching
# 
import re
# txt = "my  friend job@gmail.com talks with alice@gmail.com a lot"
# emails = re.findall(r'[\w\.-]+@[\w\.-]+',txt)
#
# for email in emails:
#     print(email)

# import re
#
# print()
#
# txt = "apple"
# pattern = "p"
#
# gathering = re.search(pattern,txt)
#
# if gathering:
#     print(" Match found - " "%s" %gathering.group()) # is used to find the match from the text
#
# else:
#     print( "No Match")
#
#
# text = "The price is $49-98-989"
#
# pattern = re.compile(r'\$(\d{2})-(\d{2})-(\d{3})')
#
#
# match = pattern.search(text)
#
# if match:
#     print(f"Entire match: {match.group()}")
#     print(f"Capture group 1: {match.group(2)}")
# else:
#     print("No match found.")
#
#
# import re
# import sys
# txt = "apple"
# pattern = "[aeiou]"
#
# match = re.search(pattern,txt)
#
# if match:
#     print(f"found match {match.group()}")
#
# print(sys.platform)
#
#
#
#
# pattern = re.compile(r'hello', re.IGNORECASE)
#
# match = pattern.search('Hello, world!')
# if match:
#     print(f"Found a match: {match.group()}")

pattern = re.compile(r"\d{4}-\d{2}-\d{2}")

text = "The date is 2024-07-07"
match = pattern.search(text)
print(match.start())
if match:
    print(f"{text}")
else:
    print(f"'{text}' does not fully match the pattern")