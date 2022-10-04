from datetime import date

def day_of_week(day):
    print(f'{day}. The menu today is: ')

import calendar
curr_date = date.today()
day_of_week(calendar.day_name[curr_date.weekday()])

if calendar.day_name[curr_date.weekday()] == "Monday":
    print(f"Soy Shepherd's Pie kinda day")

elif calendar.day_name[curr_date.weekday()] == 'Tuesday':
    print(f'Rice and broccoli, white beans, '
          f'salad and soy beef.')

elif calendar.day_name[curr_date.weekday()] == 'Wednesday':
    print(f'Brazilian vegan feijoada, with rice, black'
          f'beans, braised cabbage, fried banana and orange.')

elif calendar.day_name[curr_date.weekday()] == 'Thursday':
    print(f'Eggplant Parmigiana.')

elif calendar.day_name[curr_date.weekday()] == 'Friday':
    print(f'Vegan stew.')

elif calendar.day_name[curr_date.weekday()] == 'Saturday':
    print(f'Vegan pizzas.')

elif calendar.day_name[curr_date.weekday()] == 'Sunday':
    print(f'Today we are closed! Please come back tomorrow.')

else:
    print(f"Seems like there's an error.")
