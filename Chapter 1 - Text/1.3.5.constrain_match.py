import re
text = 'This is some text -- with punctuation.'
pattern = 'is'

print("Text : {}".format(text))
print("Pattern : {}".format(pattern))

m = re.match(pattern,text)
print('Match :', m)

s = re.search(pattern, text)
print('Search :', s)

m_full = re.fullmatch(pattern, text)
print('Full match :', m_full)
