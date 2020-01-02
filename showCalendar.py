import calendar
import datetime

def main():
    now = datetime.datetime.today()
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.formatmonth(now.year,now.month))


if __name__ == "__main__":
    main()
