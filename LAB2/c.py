n = int(input())
a =[[0 for i in range (n)] for j in range(n)]
for i in range (n):
    for j in range(n):
        if (i == j):
            a[i][j] = i * j
        if(i == 0):
            a[i][j] = j
        if (j == 0):
            a[i][j] = i
for i in range (n):
    for j in range(n):
        print(a[i][j],end = " ")        
    print()