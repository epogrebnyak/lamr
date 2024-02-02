"""Print today's date and calendar for current month."""

from calendar import TextCalendar
from datetime import date

t = date.today()
print("Today is", t)
print()  # prints empty line
TextCalendar().prmonth(t.year, t.month)

# Excercises:
# 1. change output for today's date
# 2. print calendar for the next month as well
# 3. change the first day the week in calendar
# 4. print your birthday
# 5. find out what day of the week your actual birthday was
# 6. implement print_month(year, month) function

# References:
# - https://docs.python.org/3/library/datetime.html#available-types
# - https://docs.python.org/3/library/calendar.html#calendar.TextCalendar
