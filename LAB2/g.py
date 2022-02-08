n = int(input())
c = dict()
for i in range(n) :
    s,t=input().split()
    if t in c:
        c[t] += 1
    else:
        c[t] = 1        
m = int(input())
for i in range(m):
    x,y,z = input().split()
    if y in c:
        c[y] -= int(z)
r =0
for x in c:
  if (c[x] > 0):
      r += c[x]
print("Demons left:",r)