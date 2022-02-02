a,b=map(int,input().split()) # to get 2 numbers separated by space 
prime = True
for x in range (2,a):
   if (a % x == 0):
       prime = False
if (prime and a <= 500 and b % 2 == 0):
    print("Good job!")
else:
    print("Try next time!")