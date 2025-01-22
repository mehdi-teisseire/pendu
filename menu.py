import display
from rules import clear_screen, name_is_valid, word_is_valid, validation_criteria, play_game

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
                        with open('score.txt', 'a', encoding = "utf-8") as score: 
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
            print("Choisissez un niveau de difficulté :\nPlus dur que dur: 1\n Dur: 2\nNormal: 3\nFacile: 4 ")
            level_choice = input("Entrez votre choix (1-4): ")
            
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
            word_choice = input("Voulez vous :\n1. Jouer avec un mot au hasard\n2.Ajouter votre mot à notre collection\n\nVeuillez entrer votre choix (1 ou 2) : ")
            if word_choice == "1":
                start_return_choice = input("Vous avez choisi au hasard ! Prêt à jouer ? (1 pour jouer, 2 pour le menu): ")
                if start_return_choice == "1":
                    play_game(level_choice)
            elif word_choice == "2":
                player_word = input(f"Entez votre mot (minimum {validation_criteria[chosen_level]['min_length']} et maximum {validation_criteria[chosen_level]['max_length']} lettres, pour les mots composés : XXX-XXXX): ").lower()
                            
                if word_is_valid(player_word, chosen_level):
                    try:
                        filename_mapping = {
                            'très dur': 'word1.txt',
                            'dur': 'word2.txt',
                            'normal': 'word3.txt',
                            'facile': 'word4.txt'
                        }
                        with open(filename_mapping[chosen_level], "a") as word_file:
                            word_file.write("\n" + player_word )
                        print("Votre mot à été ajouté à la collection !")
                    except Exception as e:
                        display.player_word_issue()
                else:
                    print("Ce mot n'est pas valide . Essayez encore.")
            else:
                print("Choix invalide, essayez encore.")
        elif choice == "3":            
                    clear_screen()            
                    # Logic for accessing the score tab would go here        
        else:            
            print("Choix invalide, essayez encore.")

menu()                    