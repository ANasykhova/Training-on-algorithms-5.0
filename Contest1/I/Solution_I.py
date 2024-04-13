def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


count = int(input())
year = int(input())

months = {'January': 0, 'February': 31, 'March': 59, 'April': 90, 'May': 120, 'June': 151, 'July': 181, 'August': 212,
          'September': 243, 'October': 273, 'November': 304, 'December': 334}
if is_leap(year):
    months = {'January': 0, 'February': 31, 'March': 60, 'April': 91, 'May': 121, 'June': 152, 'July': 182,
              'August': 213, 'September': 244, 'October': 274, 'November': 305, 'December': 335}

holidays = []
for i in range(count):
    day, month = input().split()
    day = int(day)
    month = months[month]
    holidays.append(day + month)

days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
day_of_week = days[input().split()[0]]

days_in_year = [52] * 7

holidays_in_year = [0] * 7

if is_leap(year):
    days_in_year[day_of_week % 7] += 1
    days_in_year[(day_of_week + 1) % 7] += 1
else:
    days_in_year[day_of_week % 7] += 1

for i in holidays:
    data = (i + day_of_week - 1) % 7
    days_in_year[data] -= 1

worst_day_value = min(range(len(days_in_year)), key=lambda x: days_in_year[x])
best_day_value = max(range(len(days_in_year)), key=lambda x: days_in_year[x])

from_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
worst_day = from_days[worst_day_value]
best_day = from_days[best_day_value]

print(best_day, worst_day)
