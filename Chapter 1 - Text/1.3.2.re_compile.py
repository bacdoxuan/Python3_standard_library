import re

#precompile patterns

regexes = [re.compile(p) for p in ['this','that']]

text = 'Does this text match the patterns?'

print('Text: {!r}n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match!')
