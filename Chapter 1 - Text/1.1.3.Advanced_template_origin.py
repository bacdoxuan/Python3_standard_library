import string

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

template_text = """
Delimiter : %%
Replaced : %with_underscore
Ignored : %notunderscored
"""

my_data = {
    'with_underscore': 'This is replaced',
    'notunderscored': 'This is ignored'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(my_data))

# The output will be:
"""
Modified ID pattern:

Delimiter : %
Replaced : This is replaced
Ignored : %notunderscored
"""