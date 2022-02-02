s = str(input())
sum =0
for x in s:
  sum += ord(x)#ASCII CODE

if (sum > 300):
    print("It is tasty!")
else:
    print("Oh, no!")
   