



a = input('Gebe eine Zahl ein ')
b =input('Gebe die zweite zahl ein ')

a_float = float(a)
b_float = float(b)

if a_float > b_float:
    print('a ist Größer als b')
elif a_float == b_float:
    print('Ist gleich groß ')
else:
    print('a ist kleiner als b')



year_input = input('Gib dein Geburtsjahr ein, ')
year = int(year_input)

if year >= 2006 and year <= 2024:
    print('Du bist nicht Alt genug')
elif year >= 1914 and year <= 2006:
    print('....')
 
else:
    print('hat geklappt')
