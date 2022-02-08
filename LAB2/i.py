n = int (input())
a = []
for i in range(n):
    s = input()
    if len(s) == 1:
      print(a[0],end = " ")
      a.pop(0)
    else:
      c,b=map(str,s.split())
      a.append(b)
     