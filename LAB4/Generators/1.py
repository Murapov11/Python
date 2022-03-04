def gen(n):
    for i in range(n+1):
        yield i * i 
    
n = int (input())
a = gen(n)
#1)print(next(a))


'''
2)
for i in range(n+1):
    print(next(a))
'''

print (list(a))