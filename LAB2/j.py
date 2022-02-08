n = int(input())
a=[]
for i in range(n):
    s = input()
    b1 = b2 = b3 = False
    for x in s:
        if(ord(x) >= 48 and ord(x) <= 57):
            b1 = True
        if (x >= 'a' and x <= 'z'):
            b2 = True
        if (x >= 'A'  and x <= 'Z'):
            b3 = True
    if(b1 and b2 and b3):
        ok = True
        for x in a:
            if(x == s):
                ok = False
                break
        if(ok):
            a.append(s)
print(len(a)) 
a.sort()
for x in a:
    print(x)  