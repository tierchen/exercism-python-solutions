from datetime import date
import calendar


_teenth = list(range(13, 20))
_days = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'


def meetup_day(year, month, day_of_the_week, which):
    dw = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th':4, 'last': -1,}
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    days_dates = {d: dates for d, dates in zip(_days, zip(*month_days))}
    days_dates = {wd: [d for d in days_dates[wd] if d != 0] for wd in days_dates}
    if which == 'teenth':
        day = set(_teenth).intersection(set(days_dates[day_of_the_week])).pop()
    else:
        day = days_dates[day_of_the_week][dw[which]]
    return date(year, month, day)