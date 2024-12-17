import random


def spiel_starten():
    print('Spiele Schere, Stein, Papier mit mir!')

while True:
    print('\nBitte wähle: Schere, Stein, Papier')

    eingabe = input ('\nWähle weise: ')
    spielzuege = ['Schere', 'Stein', 'Papier']
    
    if eingabe in spielzuege:
            random.shuffle(spielzuege)
            computer =spielzuege[0]


            if computer == eingabe:
                print('Unendschieden')
            if computer == 'Schere' and eingabe == 'Papier':
                print('Du hast verloren')
            if computer == 'Schere' and eingabe == 'Stein':
                print('Du hast Gewonnen')
            if computer == 'Stein' and eingabe == 'Schere':
                print('Du hast verloren')
            if computer == 'Stein' and eingabe == 'Papier':
                print('Du hast gewonnen')
            if computer == 'Papier' and eingabe == 'Stein':
                print('Du hast verloren')
            if computer == 'Papier'and eingabe == 'Schere':
                print('Du hast gewonnen')
    else:
            print('Falsche Eingabe')

    weitermachen = input('\nMöchtest du noch eine runde spielen? (Ja/Nein): ')
    if weitermachen != 'Ja':
        print('\nDanke fürs Spielen! Bis zum nächsten mal.')
        break
    
            
         
         
    spiel_starten()
        
