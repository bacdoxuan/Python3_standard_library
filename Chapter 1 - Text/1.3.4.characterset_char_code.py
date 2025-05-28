"""
Code Meaning
\d A digit
\D A non-digit
\s Whitespace (tab, space, newline, etc.)
\S Non-whitespace
\w Alphanumeric
\W Non-alphanumeric
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

print('Test 1:')
test_patterns(
'A prime #1 $ 23 ^^456 b.7 8*9 example!',
[(r'\d+', 'sequence of digits'),
(r'\D+', 'sequence of non-digits'),
(r'\s+', 'sequence of whitespace'),
(r'\S+', 'sequence of non-whitespace'),
(r'\w+', 'alphanumeric characters'),
(r'\W+', 'non-alphanumeric')],
)