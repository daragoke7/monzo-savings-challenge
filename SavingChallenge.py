# Program to calculate how much will be taken out each month on Monzo savings challenge
import datetime
import calendar

# today = datetime.date.today()
# start_of_year = datetime.date(2026, 1, 1)
#
# no_of_days = abs(today - start_of_year).days


# now = datetime.datetime.now()

# current_month = now.month
# day = int(input("What day for? (Only insert integers here): "))
month = int(input("What month for? (Only insert integers here): "))
# first_day = calendar.monthrange(now.year, month-1)
last_day_call = calendar.monthrange(2026, month)
day = last_day_call[1]
# day_of_year = datetime.date(2026, current_month, last_day).timetuple().tm_yday
# selected_month = ""




user_date = datetime.date(2026, month, day)
day_of_year = user_date.timetuple().tm_yday

back_date = datetime.date(2026, month, 1)
back_date_of_year = back_date.timetuple().tm_yday

a = back_date_of_year
b = day_of_year

# calc = back_date_of_year - day_of_year

total_amt = ((b*(b+1))/2) - ((a*(a-1))/2)
month_name = user_date.strftime("%B")



# how much each month
print(f"Total for {month_name} will be: £{total_amt/100}.")