a = []
while 1:
    b = input()
    if b == '0':
        break
    a.append(b)
if(len(a) % 2 == 0):
       for i in range(int(len(a)/2)):
           print( int(a[i])+int(a[len(a)-i-1]) ,end=" " )
else:
        for i in range(int(len(a)/2)):
           print( int(a[i])+int(a[len(a)-i-1]) ,end=" " )
        c = int(len(a)/2)
        print(a[c])