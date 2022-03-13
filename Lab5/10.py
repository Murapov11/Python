import re
txt = input()
result = [txt[0].lower()]
for c in txt[1:]:
    if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            result.append('_')
            result.append(c.lower())
    else:
            result.append(c)
x = "".join(result)
print(x)
     
