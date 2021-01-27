import datetime
import calendar

balance = 10000
rate_of_interest = 0.13
monthly_payment =110

date_today = datetime.date(2018, 1 , 16)
current_monthInfo = calendar.monthrange(date_today.year, date_today.month)[1]
day_tillEndOfMonth = current_monthInfo - date_today.day
start_day = date_today + datetime.timedelta(day_tillEndOfMonth + 1)
print(start_day)

refund = 0 

while balance > 0 :
    balance = balance + balance * ( rate_of_interest / 12)
    balance = balance - monthly_payment
    if balance == 0 :
        break 
    elif balance < 0 :
        refund = (-1)*balance
        balance = 0
    
    print(start_day, balance)
    

    current_monthInfo_loop = calendar.monthrange(start_day.year, start_day.month)[1]
    start_day = start_day + datetime.timedelta(current_monthInfo_loop)

print('refunded money =', refund)