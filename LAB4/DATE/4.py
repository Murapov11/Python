from datetime import datetime, timedelta
inittime = datetime(2022,3,3,20,15,30,1)
curtime = datetime.now()
timedelta = curtime - inittime 
x = timedelta.seconds + timedelta.days * 24 * 60 * 3600 
print (x)
