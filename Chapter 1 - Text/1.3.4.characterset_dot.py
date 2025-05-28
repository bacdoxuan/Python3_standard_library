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
'abbaabbba',
[('a.', 'a followed by any one character'),
('a.?', 'a followed by any one character - non-greedy'),
('b.', 'b followed by any one character'),
('a.*b', 'a followed by anything, ending in b'),
('a.*?b', 'a followed by anything - non greedy, ending in b')],
)