#Write a Python program to list(перечислять) only directories, files and all directories, files in a specified path.
import os
path_ = os.getcwd() # current path  and specified path
'''
1) only dir
2) only file
3) all file and dir
'''


# WITH LIST COMPREHENSION!!!

a = [ x for x in os.listdir(path_) if os.path.isdir(os.path.join(path_, x)) ]
print (a)

b = [ x for x in os.listdir(path_) if not os.path.isdir(os.path.join(path_, x)) ]
print(b)


c = [ x for x in os.listdir(path_)]
print(c)
# DONE

