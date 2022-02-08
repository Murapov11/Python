s = input()
if (len(s) >= 3):
    n,x=map(int,s.split())
    a = []
    for i in range(n):
      a.append(x + 2 * i)
    b = 0
    for i in a :
        b ^= i
    print(b)
else:
    x = int(input())
    a = []
    for i in range(int(s)):
      a.append(x + 2 * i)
    b = 0
    for i in a :
        b ^= i
    print(b)

