#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
txt = input()
x = re.sub("[ ,.]", ":", txt)
print(x)
#print(type(x))