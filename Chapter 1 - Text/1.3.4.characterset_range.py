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
'This is some text -- with punctuation.',
[('[a-z]+', 'sequences of lowercase letters'),
('[A-Z]+', 'sequences of uppercase letters'),
('[a-zA-Z]+', 'sequences of lower- or uppercase letters'),
('[A-Z][a-z]+', 'one uppercase followed by lowercase')],
)