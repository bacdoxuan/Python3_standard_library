"""
Matched values can be used in later parts of an expression.
For example, the email example can be updated to match only addresses
composed of the first and last names of the person by including 
back-references to those groups. 
The easiest way to achieve this is by referring to the 
previously matched group by ID number, using \num.
"""

import re

address = re.compile(
    r'''

    # The regular name
    (\w+)               # first name (1)
    \s+
    (([\w.]+)\s+)?      # optional middle name or initial
    (\w+)               # last name (4)

    \s+

    <

    # The address: first_name.last_name@domain.tld
    (?P<email>
      \1               # first name --> (\w+)
      \.
      \4               # last name --> (\w+)
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
    )

    >
    ''',
    re.VERBOSE | re.IGNORECASE)

candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('  Match name :', match.group(1), match.group(4))
        print('  Match email:', match.group(5))
    else:
        print('  No match')