def my_gen(n):
   for i in range (n):
       if (i % 2 == 0):
           yield i
n = int(input())
a = my_gen(n)
#print(next(a))


'''
for i in range(n):
    print(next(a))
'''

print (list(a))