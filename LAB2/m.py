a = []
while 1:
    s = input()
    if (s == "0"):
        break
    x = s.split()
    x.reverse()
    a.append(x)
a.sort()
for i in range(len(a)):
    for j in range(3):
        print (a[i][3-j-1],end = " ")
    print()
     