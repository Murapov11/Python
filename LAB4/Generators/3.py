def my_gen(n):
    for i in range (n):
        if ( i % 3 == 0 and i % 4 == 0):
            yield i
n = int (input())
a = my_gen(n)

#print(next(a))

'''
for i in range(n+1):
    print(next(a))
'''
print (list(a))