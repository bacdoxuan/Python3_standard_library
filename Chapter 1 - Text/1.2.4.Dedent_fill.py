sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
'''

import textwrap

dedented_text = textwrap.dedent(sample_text).strip()

for width in [45, 60, 80]:
    print('Dedent and fill - {} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()