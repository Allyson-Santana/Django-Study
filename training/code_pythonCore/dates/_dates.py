from datetime import (date, datetime, timedelta, time, tzinfo, timezone)

now = datetime.now()
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
prev_week = today - timedelta(weeks=1)

print(
    "\nnow => ", now,
    "\ntoday => ", today,
    "\nyesterday => ", yesterday,
    "\ntomorrow => ", tomorrow,
    "\nnext_week => ", next_week,
    "\nprev_week => ", prev_week
)

now_str = now.strftime("%d/%m/%Y %H:%M:%S")
print("converte data para string:", now_str)

now_str_to_datetime = datetime.strptime(now_str, "%d/%m/%Y %H:%M:%S")
print("converte data strrinng para data datetime:", now_str_to_datetime)

tz_fnt = timezone(timedelta(hours=-2))
tz_brt = timezone(timedelta(hours=-3))

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