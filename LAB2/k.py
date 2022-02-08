s = input()
x = s.split()
a = []
for i in x :
    for j in i:#loop in string
        if((j >= 'a' and j <= 'z') or (j >= 'A' and j <= 'Z')):
            continue
        else:
            i = i.replace(j,'')
    ok = True
    for y in a:
        if(y == i):
            ok = False
            break
    if(ok):
      a.append(i)
print(len(a)) 
a.sort()
for x in a:
    print(x)