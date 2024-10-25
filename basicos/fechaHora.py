from datetime import date, datetime

print(f"La fecha de hoy es: {date.today()}")
print(f"La hora es: {datetime.now().time().strftime('%H:%M:%S')}")
