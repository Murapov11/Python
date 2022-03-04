from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1) 

print('Yesterday is  : ',yesterday)
print('Today is : ',today)
print('Tomorrow is : ',tomorrow)