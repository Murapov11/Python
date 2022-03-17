import os
mypath = os.getcwd() # or with input()
print(mypath)
if os.path.exists(mypath):
   print(os.path.basename(mypath))
   print(os.path.dirname(mypath))
else:
    print("This file does not exists")
# DONE
