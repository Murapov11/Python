a = [int (n) for n in input().split(' ')]
cnt = 0
for x in a:
   if(cnt < 0):
      print(0)
      exit()
   if(cnt < x):
      cnt = x
   cnt -= 1
print(1)