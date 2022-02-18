def permute(x, i, length): 
    if i==length: 
        print(''.join(x) )
    else: 
        for j in range(i,length): 
            x[i], x[j] = x[j], x[i] 
            permute(x, i+1, length) 
            x[i], x[j] = x[j], x[i]  
''' 
s = input()
n = len(s) 
x = list(s) 
permute(x, 0, n)
'''