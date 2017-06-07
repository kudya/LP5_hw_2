from datetime import datetime, timedelta, date, time
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
date_now = datetime.now()
today = datetime.strftime(date_now, '%A, %d of %B, %Y')
delta_1d = timedelta(days=1)
delta_1m = timedelta(days=30)
yesterday = date_now - delta_1d
yesterday = datetime.strftime(yesterday, '%A, %d of %B, %Y')
month_ago = date_now - delta_1m
month_ago = datetime.strftime(month_ago, '%A, %d of %B, %Y')
print('today: ', today)
print('yesterday: ', yesterday)
print('month_ago: ', month_ago)

# Превратите строку "01/01/17 12:10:03.234567" в объект datetime
string_date = '01/01/17 12:10:03.234567'
datetime_date = datetime.strptime(string_date, '%d/%m/%y %H:%M:%S.%f')
print(datetime_date)