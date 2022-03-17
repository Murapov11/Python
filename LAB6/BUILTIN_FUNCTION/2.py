s = input()
cnt1=0
cnt2=0
for i in s:
      if(i.islower()): #islower --> build in function
            cnt1 = cnt1+1
      elif(i.isupper()): # isupper --> build in function.
            cnt2 = cnt2+1
print("lowercase characters :" , cnt1)
print("uppercase characters :" , cnt2)
#DONE
