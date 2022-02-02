n = int(input())
for x in range(n):
    s = input()
    t = s.find("@gmail.com")# string function
    if (t != -1):
        z = ""
        for y in range(t):
            z += s[y]
        print (z)