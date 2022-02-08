n = int(input())
a = dict()
for i in range (n):
    s = input()
    c,b = s.split()
    if c in a:
        a[c] += int(b)
    else:
        a[c] = int(b)

max = 0
for i in a:
   if(a[i] > max):
       max = a[i]

b = sorted(a)
for i in b:
    if(a[i] == max):
        print(i,"is lucky!")    
    else:
        print(i,"has to receive",max-a[i],"tenge")