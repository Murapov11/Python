import re
txt = input()
x = re.findall("ab+",txt)
if x:
 print (x)