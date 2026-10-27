import textwrap

# The long sentence being declared in the variable text

text = "Python is a powerful programming language that is easy to learn and widely used"

# Wrapping text
print(textwrap.fill(text, width=30))
print("\n")

# Wrapping text but presenting them as lists
print(textwrap.wrap(text, width=30))
print("\n")

# Shortening the sentence
print(textwrap.shorten(text, width=20))
print("\n")

# Removing indentation
message = """
        Hello World
        Welcome to python
"""

print(textwrap.dedent(message))
print("\n")


# Adding indentation
text2 = "Python is fun"
print(textwrap.indent(text2, ">>> "))
