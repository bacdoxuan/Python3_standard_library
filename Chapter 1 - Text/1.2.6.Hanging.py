sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
'''

import textwrap

dedented_text = textwrap.dedent(sample_text).strip()

print(textwrap.fill(dedented_text,initial_indent='->',subsequent_indent=' ' * 4,width=60,))