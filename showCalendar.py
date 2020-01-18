import calendar
import datetime
import argparse

def _showmonth(year, month):
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.formatmonth(year,month))

def _showyear(year):
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.formatyear(year))


def main():
    """
        Calendar for cmd

        cal  produces calender for current month
        cal year produces the calendar for the entire year
        cal year month produces the calendar for year month

    """
    parser = argparse.ArgumentParser(description="Calendar for cmd")
    parser.add_argument("-m","--month" , type=int, help="month", default=-1)
    parser.add_argument("-y","--year" , type=int, help="year", default=-1)

    args = parser.parse_args()
    now = datetime.datetime.today()
    if args.month != -1 and args.year != -1:
        _showmonth(args.year, args.month) 
    elif args.year != -1:
        _showyear(args.year)
    elif args.month != -1:
        _showmonth(now.year, args.month) 
    else:
        _showmonth(now.year, now.month) 

    now = datetime.datetime.today()
    c = calendar.TextCalendar(calendar.SUNDAY)
    


if __name__ == "__main__":
    main()
