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

print('Input text            :', text)

# word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print('Pattern               :', regex.pattern)

match = regex.search(text)
print('Entire match          :', match.group(0))
print('Word starting with "t":', match.group(1))
print('Word after "t" word   :', match.group(2))