import math
'''
The formula to calculate the area of a regular polygon is, Area = (number of sides × length of one side × apothem)/2,
 where the value of apothem can be calculated using the formula, Apothem = [(length of one side)/{2 ×(tan(180/number of sides))}].
'''
ns = int(input())
l = int(input())
print(round(ns * l *(l / (2 * math.tan(math.pi/ns)))/ 2))
'''
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''