from datetime import (date, datetime, timedelta, time, tzinfo, timezone)

print("\n|###### _time.py ######|\n")

x = time(hour=2, minute=0, second=0, microsecond=0)
print("time:", x)

"""
    time.min
    time.max
    time.resolution
    
    ----
    time.hour
    time.minute
    time.second
    time.microsecond
    
    -----
    
    time.fromisoformat('04:23:01')
    
        -> datetime.time(4, 23, 1)
    
    time.replace(
        hour=self.hour, 
        minute=self.minute, 
        second=self.second, 
        microsecond=self.microsecond
    )


"""


print("\nCOMPARAÇÔES")

print("time(22,0) == time(23,0) =>", time(22,0) == time(23,0))
print("time(22,0) != time(23,0) =>", time(22,0) != time(23,0))
print("time(22,0) <= time(23,0) =>", time(22,0) <= time(23,0))
print("time(22,0) > time(23,0) =>", time(22,0) > time(23,0))
print("time(22,0) >= time(23,0) =>", time(22,0) >= time(23,0))
print("time(22,0) < time(23,0) =>", time(22,0) < time(23,0))


str_hours = '22:00:10'
print("str date p/ type date:", time.fromisoformat(str_hours))

time_typeTime = time(23,55)
print('type date p/ str date:', time.isoformat(time_typeTime))


t = time(22,22,22,22)

print("isoformat()",t.isoformat())
print("isoformat(timespec='auto')",t.isoformat(timespec='auto'))
print("isoformat(timespec='minutes')",t.isoformat(timespec='minutes'))
print("isoformat(timespec='seconds')",t.isoformat(timespec='seconds'))