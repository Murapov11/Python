def f(s):
    if(s == "ONE"):
        return '1'
    if(s == "TWO"):
        return "2"
    if(s == "THR"):
        return "3"
    if(s == "FOU"):
        return '4'
    if(s == "FIV"):
        return "5"
    if(s == "SIX"):
        return "6"
    if(s == "SEV"):
        return '7'
    if(s == "EIG"):
        return "8"
    if(s == "NIN"):
        return "9"
    if(s == "ZER"):
        return "0"
def d(s):
    if(s == "1"):
        return 'ONE'
    if(s == "2"):
        return "TWO"
    if(s == "3"):
        return "THR"
    if(s == "4"):
        return 'FOU'
    if(s == "5"):
        return "FIV"
    if(s == "6"):
        return "SIX"
    if(s == "7"):
        return 'SEV'
    if(s == "8"):
        return "EIG"
    if(s == "9"):
        return "NIN"
    if(s == "0"):
        return "ZER"
s = input()
a = b = t = ""
for i in s:
    if(i == '+'):
        b = a
        a = ""
    else:
        t += i
    if (len(t) == 3):
        a += f(t)
        t = ""
c = int(a)+int(b)
c = str(c)
t=""
for i in c:
    t += d(i)
print(t)