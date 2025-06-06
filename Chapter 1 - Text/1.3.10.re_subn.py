"""
subn() works just like sub() except that it returns both the modified string and the count of substitutions made.
"""

import re

bold = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **bold**.  This **too**. Last one **last one**'

print('Text:', text)
print('Bold:', bold.subn(r'<b>\1</b>', text))