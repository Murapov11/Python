import os
print('Exist:', os.access('/Users/murap/Desktop/LAB6/BUILTIN_FUNC/test.cpp', os.F_OK))
print('Readable:', os.access('/Users/murap/Desktop/LAB6/BUILTIN_FUNC/test.cpp', os.R_OK))
print('Writable:', os.access('/Users/murap/Desktop/LAB6/BUILTIN_FUNC/test.cpp', os.W_OK))
print('Executable:', os.access('/Users/murap/Desktop/LAB6/BUILTIN_FUNC/test.cpp', os.X_OK))
# DONE
