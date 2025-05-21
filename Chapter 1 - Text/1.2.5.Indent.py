sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired. It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
'''

import textwrap

dedented_text = textwrap.dedent(sample_text)

filled_text = textwrap.fill(dedented_text, width= 80)
wrapped_text = filled_text + '\n\nSecond paragraph after a blank line.'
final_text = textwrap.indent(wrapped_text, '> ')

print(final_text)