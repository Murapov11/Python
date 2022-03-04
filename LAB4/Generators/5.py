def my_gen(n):
    for i in range(n,-1,-1):
        yield i

n = int(input())
a = my_gen(n)

#1)print(next(a))

'''
2)
for i in range(n+1):
    print(next(a))
'''
print (list(a))

    