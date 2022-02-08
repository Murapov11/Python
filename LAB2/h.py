import math
def l(a1,b1,a2,b2):
    return math.sqrt((a2-a1)*(a2-a1)+(b2-b1) *(b2-b1)) 



a,b=map(int,input().split())
n = int(input())
c = dict()
d = []
for i in range(n):
    s = input()
    a1,b1=s.split()
    d.append(l(a,b,int(a1),int(b1)))
    c[l(a,b,int(a1),int(b1))] = s
d.sort()
for i in d:
    print(c[i])