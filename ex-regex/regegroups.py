import re

my_string = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

pattern = re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)")

matches = pattern.finditer(my_string)

for match in matches:
    print(match)
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

    my_string = my_string.replace(match.group(1), "xxx")

    print(my_string)