#main.py

import datetime as dt
from view import BirthdayView

today = dt.datetime.today()
month_today = today.month
day_today = today.day

if __name__ == "__main__":
    view = BirthdayView()
    view.display_birthday(month_today, day_today)
    view.send_birthday_emails(month_today, day_today)