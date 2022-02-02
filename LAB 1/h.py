s = input()
c = str(input())
i = j = -1
for x in range(len(s)):
    if(s[x] == c):
        i = x
        break
for x in range (len(s)-1,-1,-1):
    if(s[x] == c):
        j = x
        break
if (i == j):
    print(i)
elif(i != -1 and j != -1):
    print(i,j)
