from datetime import (date, datetime, timedelta, time, tzinfo, timezone)

print("\n|###### date ######|\n")

date_typeDate = date(2023, 10, 29)
print("date (tipo data):", date_typeDate)
date_typeString = date.fromisoformat('2023-10-29')
print("converte data string para tipo date):", date_typeString)

print("today:", date_typeDate.today())
print("weekday:", date_typeDate.weekday())
print(
    "year:",date_typeString.year, "|",
    "month:", date_typeString.month, "|",
    "day:", date_typeString.day
)

new_date_replace = date_typeDate.replace(year=2024, day=8)
print("replace date:",new_date_replace)

print("strftime:", new_date_replace.strftime("%d:%m:%Y"))


print("")