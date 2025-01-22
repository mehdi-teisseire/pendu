import display
from rules import clear_screen, name_is_valid, play_game

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

        elif choice == "2":
            clear_screen()
            print("Choisissez un niveau de difficulté (Plus dur que dur: 1, Dur: 2, Normal: 3, Facile: 4 )")
            level_choice = input("Entez votre choix (1-4): ")
            
            level_mapping = {
                "1": "Très dur",
                "2": "dur",
                "3": "normal",
                "4": "facile"
            }
            chosen_level = level_mapping.get(level_choice)
            if not chosen_level:
                print("Choix de niveau invalide, essayez encore.")
                continue
            
            print(f"Bien joué ! Vous avez choisi : {chosen_level.capitalize()}.")
            word_choice = input("Vous voulez jouer avec un mot au hasard ? (1)\nou ajouter votre mot à notre collection (2) ? (1-2): ")
            if word_choice == "1":
                start_return_choice = input("Vous avez choisi au hasard ! Prêt à jouer ? (1 pour jouer, 2 pour le menu): ")
                if start_return_choice == "1":
                    play_game(level_choice)