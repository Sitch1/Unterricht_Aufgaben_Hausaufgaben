from datetime import datetime

date = datetime.now()

print(date)

#date = datetime(input('Datum eingeben zu sehen ob Arbeit oder Urlaub ist (yyyy.mm.dd): '))

is_winter = date >= datetime(2024, 12, 24) and date <= datetime(2025, 1, 2)
is_eastern = date >= datetime(2025, 4, 7) and date <= datetime(2025, 4, 19)
is_eastern_01 = date >= datetime(2025, 4, 30) and date <= datetime(2025, 4, 30)
is_holiday = date >= datetime(2025, 5, 2) and date <= datetime(2025, 5, 2)
is__holiday = date >= datetime(2025, 6, 10) and date <= datetime(2025, 6, 10)
is_summerholiday = date >= datetime(2025, 7, 3) and date <= datetime(2025, 8, 13)
is_autumnholiday = date >= datetime(2025, 10, 13) and date <= datetime(2025, 10, 25)
# ''Wenn'' #
if is_winter:
        print('Winterferien')
    #'' ansonsten wenn'' #
elif is_eastern:
        print('Osternferien')
    # '' Ansonsten'' #
elif is_eastern_01:
        print('Feiertag')
else:
        print('Es ist zeit zu knüppeln')