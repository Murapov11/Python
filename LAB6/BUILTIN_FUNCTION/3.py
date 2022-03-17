s = input()
#print ("".join(reversed(s)))
if (s == "".join(reversed(s))): # reversed() --> built in function
    print("Palindrome")
else:
    print("Not a Palindrome")
# DONE