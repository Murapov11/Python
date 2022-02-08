cnt1 = cnt2 = cnt3 =0
s = input()
a = []
for i in s:
    # first bracket
    if (i == '('):
        cnt1 += 1
        a.append(')')
    if (i == ')'):
        cnt1 -= 1
        if (cnt1 < 0  ):
          print("No")
          exit()
        if(a[-1] != ')'):
            print("No")
            exit()
        else:
            a.pop(-1)
    # second bracket
    if (i == '['):
        cnt2 += 1
        a.append(']')
    if (i == ']'):
        cnt2 -= 1
        if (cnt2 < 0 ):
          print("No")
          exit()
        if(a[-1] != ']'):
            print("No")
            exit()
        else:
            a.pop(-1)  
    # 3rd bracket          
    if (i == '{'):
        cnt3 += 1
        a.append('}')
    if (i == '}'):
        cnt3 -= 1
        if ( cnt3 < 0 ):
          print("No")
          exit()
        if(a[-1] != '}'):
            print("No")
            exit()
        else:
            a.pop()
      # final decision  
if (cnt1 == 0 and cnt2 == 0 and cnt3 == 0):
    print("Yes")
else:
    print("No")