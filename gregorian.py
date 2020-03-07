import calendar
from datetime import date

# Create a plain text calendar
c = calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(2020, 1, 0, 0)
print(str)

for month in range(1, 13):
    # It retrieves a list of weeks that represent the month
    mycal = calendar.monthcalendar(date.today().year, date.today().month)
    # The first MONDAY has to be within the first two weeks
    week1 = mycal[0]
    week2 = mycal[1]
    if week1[calendar.MONDAY] != 0:
        auditday = week1[calendar.MONDAY]
    else:
    # if the first MONDAY isn't in the first week, it must be in the second week
        auditday = week2[calendar.MONDAY]
        print("%10s %2d" % (calendar.month_name[month], auditday))