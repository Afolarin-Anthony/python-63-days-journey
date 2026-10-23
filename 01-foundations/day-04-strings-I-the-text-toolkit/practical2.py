import string


# String Manipulation
# First set

word = "Python is fun"
print(word[0], word[-1], word[2:5], word[::-1])
print(" ".join(["Python", "is", "powerful"]))
print(word.upper(), "|", word.split())


# Second set

password = "s3cure!"
is_strong = (any(c in string.ascii_letters for c in password) and
             any(c in string.digits for c in password) and
             any(c in string.punctuation for c in password))
print("Strong password?",is_strong)

from string import Template
t = Template("Hello, $name! You have $n new messages.")
print(t. safe_substitute(name="Ada", n=5))
