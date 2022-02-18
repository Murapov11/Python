def unique(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
#print(unique([1,2,3,7,6,4,5,6,7,8]))