# (iii). a Python program to extract year, month, date and time using Lambda.    

import datetime

currentDateTime =  datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print('Year - ',year(currentDateTime))
print('Month - ',month(currentDateTime))
print('Day - ',day(currentDateTime))
print('Time - ',time(currentDateTime))
