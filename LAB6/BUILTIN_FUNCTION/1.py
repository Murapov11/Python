# 1st way: 

mylist1 = [1,2,3,4,5]
x = len (mylist1) # len() is the builtin function
p =1
for i in range(x): # range() is the builtin function
    p *= mylist1[i]
print(p) # print() is the builtin function 

'''
# 2nd way  -->> WITH MATH Import 
# Importing math module
import math
mylist2 = [1, 2, 3, 4, 5,10]
product = math.prod(mylist2)
print(product)
'''
