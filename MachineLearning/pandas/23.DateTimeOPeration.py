import pandas as pd 

#current data and time 
#  1 -timestamp.now()

print("Current data and time:\n ",pd.Timestamp.now())


#  2 - day of the week 

timeStamp=pd.Timestamp(year=2026,month=12,day=31,hour=12,minute=27)
print("\n Data and time:\n",timeStamp)

#Display the day of the week 
print("\n Day of week:\n",timeStamp.dayofweek)

# 3 - Day of year 

print("\n Day of year:\n",timeStamp.dayofyear)

# 4 - get the number of days in month

print("\n Get the number of day in month:\n",timeStamp.daysinmonth)

# 5- ckeck if the year is a leap year

print("\n Leap year :\n",timeStamp.is_leap_year)

# 6- ckeck if date is last day of month 
print("\n Last day of month:\n",timeStamp.is_month_end)

# 7- first day of month

print("\n First day of month:\n",timeStamp.is_month_start)

# 8 - last day of year
print("\n Last day of year :\n",timeStamp.is_year_end)

# 9 - first day of year
print("\n 1st day of year :\n",timeStamp.is_year_start)