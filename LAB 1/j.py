s = input()
x = s.split()
z = ""
for y in x:
    if(len(y) >= 3):
       z += y
       z += " "
print (z)