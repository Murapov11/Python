
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
txt = input()
x = re.findall("[A-Z]+[a-z]",txt)
if x:
  print(x)