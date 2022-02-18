def filter_prime(a):
    b = []
    for i in (a):
        cnt = 0
        for j in range(2,i):
          if i % j == 0:
              cnt += 1
        if(cnt == 0):
           b.append(i)
    return b
'''  
a = [int (n) for n in input().split(' ')]
print(filter_prime(a))
'''


