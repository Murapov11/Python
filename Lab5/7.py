import re
str = input()
x = re.split("_",str)
result = x[0] + ''.join(a.title() for a in x[1:]) #x[0].title()
print (result)
# yerkhan_rek_ter_hard_work_patient_patience_happy

