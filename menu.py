import display
from rules import clear_screen, name_is_valid, word_is_valid, validation_criteria, play_game
import time

# To display the menu
def menu():
    player_name = ""
    
    while True:

        print("\n=== MENU DU PENDU ===")
        print(" ")
        print("1. S'enregistrer")
        print("2. JOUER ")
        print("3. Le tableau des scores ")
        print("4. Quitter")  
        
        choice = input("\nEntrez votre choix (1-4): ")

        # Registration process
        if choice == '1':

            while True:
                player_name = input("Entrez votre nom : ")
                if name_is_valid(player_name):
                    try: 
                        with open('score.txt', 'a', encoding="utf-8") as score: 
                            score.write("\n" + player_name)
                            print("Votre nom a été sauvegardé.")
                            break 
                    except Exception as e: 
                        display.player_name_issue(e)
                else:
                    display.invalid_player_name()
            time.sleep(2)
            clear_screen()

        # Game setup and difficulty selection
        elif choice == "2":

            clear_screen()
            print("\n=== Choisissez un niveau de difficulté ===")
            print(" ")
            print("1. Plus dur que dur")
            print("2. Dur")
            print("3. Normal")
            print("4. Facile")
            print(" ")

            while True: 
                level_choice = input("Entrez votre choix (1-4) : ")
                
                level_mapping = {
                    "1": "Très dur",
                    "2": "Dur",
                    "3": "Normal",
                    "4": "Facile"
                }
                chosen_level = level_mapping.get(level_choice)
                
                if chosen_level:
                    print(f"Vous avez choisi : {chosen_level}.")
                    break 
                else:
                    print("Choix de niveau invalide.\nVeuillez entrer un nombre entre 1 et 4.")
                    print(" ")

            time.sleep(2)
            clear_screen()

            # Player Choice
            print("\n=== Que voulez-vous faire ? ===")
            print(" ")
            print("1. Jouer avec un mot au hasard")    
            print("2. Ajouter votre mot à notre collection")
            while True:    
                word_choice = input("\nVeuillez entrer votre choix (1 ou 2) : ")

                if word_choice == "1":
                    start_return_choice = input("Vous avez choisi de jouer au hasard !\nPrêt à jouer ?\nEntrez 1 pour jouer, 2 pour retourner au menu : ")

                    if start_return_choice == "1":
                        time.sleep(2)
                        clear_screen()
                        play_game(level_choice)
                    elif start_return_choice == "2":
                        print("Retour au menu principal...")
                        time.sleep(2)
                        clear_screen()
                        break
                    else:
                        print("Choix invalide. Veuillez entrer 1 ou 2.")

                # To add a word to the collection
                elif word_choice == "2":

                    while True: 
                        player_word = input(f"\nVeuillez entrer votre mot (entre {validation_criteria[chosen_level]['min_length']} et {validation_criteria[chosen_level]['max_length']} lettres).\n"
                            "Pour les mots composés, utilisez le format : XXX-XXXX\n"
                            "Votre mot : ").lower()
                        
                        if word_is_valid(player_word, chosen_level):
                            try:
                                filename_mapping = {
                                    'très dur': 'word1.txt',
                                    'dur': 'word2.txt',
                                    'normal': 'word3.txt',
                                    'facile': 'word4.txt'
                                }
                                with open(filename_mapping[chosen_level], "a") as word_file:
                                    word_file.write("\n" + player_word)
                                print("Votre mot a été ajouté à la collection avec succès !")
                                break
                            except Exception as e:
                                print("Une erreur est survenue lors de l'ajout du mot. Veuillez réessayer.")
                        else:
                            print("Ce mot n'est pas valide. Veuillez essayer encore.")
                else:
                    print("Choix invalide. Veuillez entrer 1 ou 2.")

        elif choice == "3":            
            clear_screen()            
            print("=== Tableau des scores ===")
            # Logic for accessing the score tab would go here

        # Exit option
        elif choice == "4":  
            print("Merci d'avoir joué ! À bientôt.")
            print(" ")
            break
            
        else:            
            print("Choix invalide, essayez encore.")

menu() 