import time
number = int(input())
time_ = int (input())
a = pow (number,1/2) # pow BUILTIN function
time.sleep(time_ * 0.001)
print(f'Square root of {number} after {time_} miliseconds is {a}')
# 9,2000;
# DONE 