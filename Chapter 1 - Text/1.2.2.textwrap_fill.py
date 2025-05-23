import textwrap

sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

print("textwrap width = 50:\n")
print(textwrap.fill(sample_text, width=50))

print("\ntextwrap width = 80:\n")
print(textwrap.fill(sample_text, width=80))