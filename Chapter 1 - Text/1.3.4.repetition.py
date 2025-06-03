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
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count("\\")
            prefix = "." * (s + n_backslashes)
            print(
                "  {}'{}' (number of . : {})".format(prefix, substr, prefix.count("."))
            )
        print()
    return


test_patterns(
    "abbaabbba",
    [
        ("ab*", "a followed by zero or more b"),
        ("ab+", "a followed by one or more b"),
        ("ab?", "a followed by zero or one b"),
        ("ab{3}", "a followed by three b"),
        ("ab{2,3}", "a followed by two to three b"),
    ],
)
