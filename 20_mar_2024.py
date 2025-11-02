import datetime, time

future = datetime.datetime(2026, 7, 11)
print(f"my birthday {future}")
now = datetime.datetime.now()
print(f"time now {now}")
#time to that date
print(f"{(future - now).days} days until my birthday")