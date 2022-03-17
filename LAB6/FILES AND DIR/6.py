s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    f = open(f'{s[i]}.txt','x')
f.close()
#DONE