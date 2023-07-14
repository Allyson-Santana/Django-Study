from datetime import (date, datetime, timedelta, time, tzinfo, timezone)

print("\n|###### _timezone.py ######|\n")

tz_fnt = timezone(timedelta(hours=-2))
tz_brt = timezone(timedelta(hours=-3))

print("tz_fnt:", datetime.now(tz=tz_fnt))
print("tz_brt:", datetime.now(tz=tz_brt))

print("format:", datetime.now(tz=tz_brt).strftime('%d/%m/%Y %H:%M:%S %p %z | %Z'))

now = datetime.now()

now_str = now.strftime("%d/%m/%Y %H:%M:%S")
print("converte data para strring:", now_str)

now_str_to_datetime = datetime.strptime(now_str, "%d/%m/%Y %H:%M:%S")
print("converte data strrinng para data datetime:", now_str_to_datetime)

now_tz_utc = datetime.now()
now_tz_fnt = datetime.now(tz=tz_fnt)
now_tz_brt = now_tz_fnt.astimezone(tz_brt)
convert_to_utc_with_type_datetime = now_tz_brt.astimezone(timezone.utc)

# String de exemplo
data_str = '2023-04-16 20:53:14.933400-03:00'
# Converter a string para datetime
convert_to_utc = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S.%f%z').astimezone(timezone.utc)

print(
    "\nnow_tz_utc: ", now_tz_utc,
    "\nnow_tz_fnt: ", now_tz_fnt,
    "\nnow_tz_brt: ", now_tz_brt,
    "\nconvert_to_utc:", convert_to_utc,
    "\nconvert_to_utc_with_type_datetime:", convert_to_utc_with_type_datetime,
)
