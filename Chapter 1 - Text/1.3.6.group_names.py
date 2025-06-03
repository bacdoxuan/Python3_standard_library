"""
Code Meaning
\d A digit
\D A non-digit
\s Whitespace (tab, space, newline, etc.)
\S Non-whitespace
\w Alphanumeric
\W Non-alphanumeric

Code Meaning
^ Start of string, or line
$ End of string, or line
\A Start of string
\Z End of string
\b Empty string at the beginning or end of a word
\B Empty string not at the beginning or end of a words
"""

import re

text = 'This is some text -- with punctuation.'

print(text)
print()

patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b',
]

for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()