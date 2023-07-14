from datetime import (date, datetime, timedelta, time, tzinfo, timezone)

print("\n|###### timedelta ######|\n")

delta = timedelta(
	days=50,
	seconds=27,
	microseconds=10,
	milliseconds=29000,
	minutes=5,
	hours=8,
	weeks=2
)

print("min:", timedelta.min)
print("max:", timedelta.max)
print("resolution:", timedelta.resolution)

x = timedelta(days=10)
y = timedelta(days=20, minutes=-30)
print("Intervalos de tempo:", y - x)

print("total de segundos em um tempo:", x.total_seconds())
