import textwrap

sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
'''

dedent_text = textwrap.dedent(sample_text)

print(f"Normal text:\n {sample_text}")
print(f"\nDedent text:\n {dedent_text}")