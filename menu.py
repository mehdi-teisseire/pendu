import display
from rules import clear_screen, name_is_valid

# To display the menu
def menu():
    player_name = ""
    while True:
        print("\n*** MENU DU PENDU ***")
        print("1. S'enregistrer")
        print("2. JOUER ")
        print("3. Le tableau des scores ")
        
        choice = input("\nEntrez votre choix (1-3): ")

        if choice == '1':
            while True:
                player_name = input("Entrez votre nom : ")
                if name_is_valid(player_name):
                    try: 
                        with open('score.txt', 'a') as score: 
                            score.write("\n" + player_name)
                            print("Votre nom à été sauvegardé !")
                            clear_screen()
                            break 
                    except Exception as e: 
                        display.player_name_issue(e)
                else:
                        display.invalid_player_name()
