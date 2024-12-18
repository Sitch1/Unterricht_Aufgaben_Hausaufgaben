



import datetime
def Tag_bis_ende_des_jahres():
    aktuelles_datum = datetime.date.today()
    Jahresende = datetime.date(2024, 12, 31)
    differenz = aktuelles_datum - (Jahresende)
    print(differenz)

Tag_bis_ende_des_jahres()




def tag_bis_jahresende():
    
    tag_bis_jahresende = input('Gebe bitte ein Datum ein: ')