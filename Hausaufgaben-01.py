



is_winter_holiday = '2024.12.23' and '2025.01.01'
is_eastern = '2025.04.07' and '2025.04.19'
is_eastern_01 = '2025.04.30' and '2025.04.30'
is_holiday_01 = '2025.05.02' and '2025.05.02'
is_holiday_02 = '2025.05.30' and '2025.05.30'
is__holiday_03 = '2025.06.10' and '2025.06.10'
is_summerholiday = '2025.07.03' and '2025.08.13'
is_autumnholiday = '2025.10.13' and '2025.10.25'



date = input('Datum eingeben zu sehen ob Arbeit oder Urlaub ist. ')



if is_winter_holiday >= date and date <= is_winter_holiday:
    print ('Winterferien vom 23.12.2024 - 01.01.2025')
elif is_eastern >= date and date <= is_eastern:
    print ('Osterferien vom 07.04.2025 - 19.04.2025')
elif is_eastern_01 >= date and date <= is_eastern_01:
    print('Feirtag')
elif is_holiday_01 >= date and date <= is_holiday_01:
    print('Feiertag 2')
else:
    print('Es ist zeit zu Knüpeln')



date = input('Datum eingeben zu sehen ob Arbeit oder Urlaub ist. Year/month/day: ')

is_winter = date >= '2024.12.23' and date <='2025.01.01'
is_eastern = date >='2025.04.07' and date <='2025.04.19'
in_eastern_01 = date >= '2025.04.30' and date <='2025.04.30'
is_holiday = date >= '2025.05.02' and date <= '2025.05.02'
is_holiday = date >= '2025.05.30' and date <= '2025.05.30'
is__holiday = date >= '2025.06.10' and date <= '2025.06.10'
is_summerholiday = date >= '2025.07.03' and date <= '2025.08.13'
is_autumnholiday = date >= '2025.10.13' and date <= '2025.10.25'



if is_winter:
    print('Winterferien vom 23.12.2024 - 01.01.2025')
elif is_eastern >= date and date <= is_eastern:
    print('Osternferien')

