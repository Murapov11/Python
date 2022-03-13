# Write a Python program to split a string at uppercase letters.
import re
str = input()
x = re.findall('[A-Z][^A-Z]*', str)
if x:
  print(x)