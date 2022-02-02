"""
WITHOUT RECURSION 
s = input()
cnt = len(s)-1
sum = 0
for x in s:
    if(x == '0'):
        cnt -= 1
    else:
        sum += pow(2,cnt)
        cnt -= 1        
print (sum)
"""
# WITH RECURSION
def sum_1(s, n):
    i = len(s)-1-n
    if(i == len(s)-1):
       return ord(s[i])-48
    else:       
       return pow(2,n)*(ord(s[i])-48)+sum_1(s,n-1)
  


s = input()
n = len(s)-1
res = sum_1(s,n)
print(res)