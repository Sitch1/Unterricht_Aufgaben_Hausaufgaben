



# eat_list = []

# for _ in range(3):
#     user_input = input ("Dein Lieblingsessen: ")
#     eat_list.append(user_input)
#     print(f"Lieblings Essen: {user_input}")

# for gerricht in eat_list:
#     print(f"Dein Essen: {eat_list}")

essen = []


while True:
    user = input("Gebe bitte dein lieblings Essen an unf für beenden tippe 'fertig'! ")
    essen.append(user)

   
    continue_input = input("Möchtest du vortfahren ? JA/NEIN ").strip().lower
    if continue_input != "JA":
        print("Dus hast das Programm beendet!")
    break
print(f"Dein Essen ist: {essen}")
        
    
