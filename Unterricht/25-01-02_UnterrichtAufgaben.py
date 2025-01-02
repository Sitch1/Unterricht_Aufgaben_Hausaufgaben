# 1. Die Summer aller Zahlen berechnet.
# 2. Nur die ungeraden Zahlen ausgibt.
# 3. Die größte Zahl in der Liste finden.



# 'list_nr = [2, 4, 5]
# result = sum(list_nr) #!!! ´´´sum(list_nr)´´´ !!! ´´´sum´´´ ist ein befehl für multiplikation, alles was in der liste ist wird zusammen gerechnet.!!!
# print(result)



list_Nr1 = list(range(11))
summe = 0

def result():
    global summe
    for i in list_Nr1:
        summe += i
    return summe

ergebnis = result()
print(f' Das ergebniss aus den Zahlen: {list_Nr1} ist das ergebniss {ergebnis}')


def ungerade():
    gerade = []
    ungerade = []

    for i in list_Nr1:
        if i % 2 == 0:
            gerade.append(i)
        else:
            ungerade.append(i)
    print(f'{gerade}')
    print(f'{ungerade}')


ungerade()