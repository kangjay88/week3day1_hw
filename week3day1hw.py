# Regex project
# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

# Hint: use with open() and readlines()

# """
# Expected Output
# Abraham Lincoln
# Andrew P Garfield
# Connor Milliken
# Jordan Alexander Williams
# None
# None
# """

import re

with open('week3hw/week3hw.txt') as f:
    data = f.read()
    print(data)

pattern5= re.compile('([A-Z][a-zA-Z ]*) ([A-Z][a-z]*)')

for name in data:
    match = pattern5.match(data)
    if match:
        print(match.group())
    else:
        print("None")