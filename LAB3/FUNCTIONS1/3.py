def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads)/2
    x = numheads - y
    a =[]
    a.append(int(y))
    a.append(int(x))
    return a    # LIST[Number of rabits,Number of chickens]
    
#numheads = int(input())
#numlegs = int(input())
#print(solve(numheads,numlegs))
'''
def solve(35, 94):
    y = (94 - 2 * 35)/2
    x = 35 - y
    a =[]
    a.append(int(y))
    a.append(int(x))
    return a
'''