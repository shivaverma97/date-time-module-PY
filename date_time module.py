import datetime
import pytz

date_print = datetime.date(2016,9,12)
print(date_print)



time_now  = datetime.time(12,30,47)
print(time_now)
print(time_now.hour)



date_today = datetime.date.today()
print(date_today)



week_day_1 = date_today.weekday() # takes date_today as arg, wed is the day so it will print 0(mon) 1(tue) 2(wed) and so on
print(week_day_1)



week_day_2 = date_today.isoweekday() # same as weekday() but iso is used so it will take monday value as 1 and so on 
print(week_day_2)



time_delta = datetime.timedelta(days=7,hours=23 )
future_date = time_delta + date_today  # similarly minus(-) can be used to go in past
print(future_date)


bday = datetime.date(2021,9,12) # gives difference between dates
till_bday = bday - date_today
print(till_bday)


date_today_today = datetime.datetime.today()  # it prints todays date and takes timezone arg as none
print(date_today_today)

date_today_utcnow = datetime.datetime.now(tz=pytz.utc) # takes timezone arg as tz value and if nothing is passed then takes none as default
print(date_today_utcnow)

date_today_now = date_today_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))  # converting a time to any diff timezone
print(date_today_now)

for timezones in pytz.all_timezones : # priting all the available timezones 
    print(timezones)



any_date = datetime.datetime.now() # in many cases this may throw an error if error is found try below code
# print(any_date)
# converting_date = any_date.astimezone(pytz.timezone('Asia/Kolkata'))
# print(converting_date)

any_date_tz = pytz.timezone('Asia/Karachi')
any_date = any_date_tz.localize(any_date)
print(any_date)
converting_date = any_date.astimezone(pytz.timezone('Asia/Kolkata'))
print(converting_date)



# strftime = converts date into string or whatever format you want
# strptime = converts string into datetime format
date_isoFormat = datetime.datetime.today() 
print(date_isoFormat.isoformat())
print(date_isoFormat.strftime("%B %d,%Y"))

str_date = 'July 23,2021'
str_date_converted = datetime.datetime.strptime(str_date,'%B %d,%Y')
print(str_date_converted)