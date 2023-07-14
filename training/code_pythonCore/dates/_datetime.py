from datetime import (date, datetime, timedelta, time, tzinfo, timezone)

print("\n|###### _datetime.py ######|\n")

my_datetime = datetime(
    year=10,
    month=2,
    day=3,
    hour=0,
    minute=0,
    second=0,
    microsecond=0
)

print("today:", datetime.today())
print("now:", datetime.now(tz=None))
stringDate_to_typeDate = datetime.fromisoformat('2011-11-04 00:05:23.283')

print("converção data str p/ tipo date:", stringDate_to_typeDate)

""" ----------
    _datetime.py.year
    _datetime.py.month
    _datetime.py.day
    _datetime.py.hour
    _datetime.py.minute
    _datetime.py.second
    _datetime.py.microsecond
---------- """

"""---------
    _datetime.py.date()
    _datetime.py._time.py()
    _datetime.py.replace()
    _datetime.py.timetuple()
----------"""

today = datetime.today()
yesterday = today - timedelta(days=1)

print("Calculo de data:", yesterday)


now = datetime.now()

now_str = now.strftime("%d/%m/%Y %H:%M:%S")
print("converte data para strring:", now_str)

now_str_to_datetime = datetime.strptime(now_str, "%d/%m/%Y %H:%M:%S")
print("converte data strrinng para data datetime:", now_str_to_datetime)