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

def test_patterns(text, patterns):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print(" pattern: '{}', description: ({})\n".format(pattern, desc))
        print(" Text:\n '{}'".format(text))
        print(" Matches:")
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}' (number of . : {})".format(prefix, substr, prefix.count('.')))
        print()
    return

test_patterns(
'This is some text -- with punctuation.',
[(r'^\w+', 'word at start of string'),
(r'\A\w+', 'word at start of string'),
(r'\w+\S*$', 'word near end of string'),
(r'\w+\S*\Z', 'word near end of string'),
(r'\w*t\w*', 'word containing t'),
(r'\bt\w+', 't at start of word'),
(r'\w+t\b', 't at end of word'),
(r'\Bt\B', 't, not start or end of word')],
)