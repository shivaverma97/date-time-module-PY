import datetime 
import calendar

current_weight =  100
target_weight = 60
loss_perMOnth = 2

date_today = datetime.date.today()
month_info = calendar.monthrange(date_today.year , date_today.month)[1]

till_end = month_info - date_today.day

start_date = date_today + datetime.timedelta(till_end +1)
start_exercise = start_date

weight_coundtown = []

while current_weight > target_weight :
    current_weight = current_weight - loss_perMOnth
    weight_coundtown.append(current_weight)
    print(f'{start_exercise} , {current_weight}kg')

    month_info_ex = calendar.monthrange(start_exercise.year , start_exercise.month)[1]
    till_end_ofMOnth = month_info_ex - start_exercise.day
    start_exercise = start_exercise + datetime.timedelta(till_end_ofMOnth +1)

print(f'Reached goal in {len(weight_coundtown)} months')


########  FOR PER WEEK ########

# date_of_check = start_date
# loss_perWeek = 1 
# while current_weight > target_weight :
#     current_weight = current_weight - loss_perWeek
#     print(f'{date_of_check} , {current_weight}kg')
#     date_of_check = date_of_check + datetime.timedelta(7)