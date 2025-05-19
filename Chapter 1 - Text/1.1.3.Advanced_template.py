import string

# Advanced template example using string.Template

template_text = """
Hello, ${name}!
You have ${count} new messages.
Your balance is: ${balance}
"""

data = {
    'name': 'Alice',
    'count': 5,
    'balance': '$123.45'
}

template = string.Template(template_text)
result = template.substitute(data)

print(result)

"""
Output:
Hello, Alice!
You have 5 new messages.
Your balance is: ${balance}
"""