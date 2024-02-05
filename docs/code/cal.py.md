Print today's date and a calendar for current month.

```python
from calendar import TextCalendar
from datetime import date

t = date.today()
print("Today is", t)
print()  # prints empty line
TextCalendar().prmonth(t.year, t.month)
```

> Run ```lamr code cal.py --all``` to get this code with excercises.

## Excercises

1. Print calendar for the next month.
2. Change the first day the week in calendar to Sunday.
3. Implement `print_month(year: int, month: int)` function to print calendar.
4. Change output format for today's date.
5. Print the date of your birthday.
6. Find out what day of the week your actual birthday was.

## References

1. Documentation for `datetime`. URL: <https://docs.python.org/3/library/datetime.html#available-types>
2. Documentation for `calendar.TextCalendar`. URL: <https://docs.python.org/3/library/calendar.html#calendar.TextCalendar>
