import display
from rules import clear_screen, name_is_valid, word_is_valid, validation_criteria, play_game
import time
from score import update_score, display_score_table

# To check if the player name is in the score file
def name_exists(player_name):
    try:
        with open('score.txt', 'r', encoding="utf-8") as score_file:
            registered_names = [line.split(",")[0].strip() for line in score_file.readlines()]
            return player_name in registered_names
    except FileNotFoundError:
        return False

# To verify if player already have an account
def register_player():
    while True:
        has_account = input("Vous êtes vous déja enrregistré auparavant ? (oui/non) : ").strip().lower()
        
        if has_account == 'oui':
            player_name = input("Entrez votre nom : ")
            if name_exists(player_name):
                print(f"Bienvenue de nouveau, {player_name}!")
                return player_name
            else:
                try_again = input("Nom non trouvé.\nVoulez-vous essayer à nouveau (1)\nou vous enregistrer avec un nouveau nom (2) ? : ").strip()
                if try_again == '1':
                    continue
                elif try_again == '2':
                    print("D'accord, veuillez entrer votre nom pour vous enregistrer.")
        
        player_name = input("Entrez votre nom : ")
        if name_is_valid(player_name) and not name_exists(player_name):
            try: 
                with open('score.txt', 'a', encoding="utf-8") as score: 
                    score.write("\n" + player_name + ",0")
                    print("Votre nom a été sauvegardé.")
                    return player_name
            except Exception as e: 
                display.player_name_issue(e)
        else:
            if not name_is_valid(player_name):
                display.invalid_player_name()
            else:
                print("Ce nom est déjà enregistré. Veuillez en choisir un autre.")

        time.sleep(2)
        clear_screen()
    
# A menu to select the game level
def select_difficulty():
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
            "1": "très dur",
            "2": "dur",
            "3": "normal",
            "4": "facile"
        }
        chosen_level = level_mapping.get(level_choice)
        
        if chosen_level:
            print(f"Vous avez choisi : {chosen_level}.")
            #return chosen_level
            return level_choice, chosen_level
        else:
            print("Choix de niveau invalide.\nVeuillez entrer un nombre entre 1 et 4.")
            print(" ")

 # Loop for playing multiple games and register scores
def play_game_option(player_name, level_choice):

    while True:
        time.sleep(2)
        clear_screen()
        won = play_game(level_choice) 
        update_score(player_name, level_choice, won)
        
        play_again = input("Voulez-vous refaire une partie ?\n (1 pour oui, 2 pour retourner au menu) : ")
        if play_again == "1":
            level_choice = select_difficulty()
        elif play_again == "2":
            print("Retour au menu ...")
            time.sleep(2)
            clear_screen()
            return
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

# To add a word to a collection
def add_word_option(chosen_level):
    while True: 
        player_word = input(f"\nVeuillez entrer votre mot (entre {validation_criteria[chosen_level]['min_length']} et {validation_criteria[chosen_level]['max_length']} lettres).\nPour les mots composés, utilisez le format : XXX-XXXX\nVotre mot : ").lower()
        
        if word_is_valid(player_word, chosen_level):
            try:
                filename_mapping = {
                    'très dur': 'word1.txt',
                    'dur': 'word2.txt',
                    'normal': 'word3.txt',
                    'facile': 'word4.txt'
                }
                with open(filename_mapping[chosen_level], "a", encoding= "utf-8") as word_file:
                    word_file.write("\n" + player_word)
                print("Votre mot a été ajouté à la collection avec succès !")
                return
            except Exception :
                print("Une erreur est survenue lors de l'ajout du mot. Veuillez réessayer.")
        else:
            print("Ce mot n'est pas valide. Veuillez essayer encore.")

# To organize all the navigation The big menu
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

        if choice == '1':
            player_name = register_player()
            time.sleep(2)
            clear_screen()

        elif choice == "2":
            time.sleep(2)
            clear_screen()
            level_choice,chosen_level = select_difficulty()

            while True:
                time.sleep(2)
                clear_screen()
                print("\n=== Que voulez-vous faire ? ===")
                print(" ")
                print("1. Jouer avec un mot au hasard")    
                print("2. Ajouter votre mot à notre collection")
                print("3. Retour au menu principal")

                word_choice = input("\nVeuillez entrer votre choix (1-3) : ")

                if word_choice == "1":
                    play_game_option(player_name, level_choice)

                elif word_choice == "2":
                    add_word_option(chosen_level)
                elif word_choice == "3":
                    print("Retour au menu principal")
                    time.sleep(2)
                    clear_screen()
                    break
                else: 
                    print ("Choix invalide. Veuillez entrer 1, 2 ou 3.")

        elif choice == "3":
            time.sleep(2)            
            clear_screen()            
            display_score_table()
            while True:
                return_to_menu = input("\nPour retourner au menu (1) : ")
                if return_to_menu == "1":
                    time.sleep(2)
                    clear_screen()
                    break
                else:
                    print ("Choix invalide. Veuillez entrer 1.")
            
        elif choice == "4":  
            print("Merci d'avoir joué ! À bientôt.")
            print(" ")
            break
            
        else:            
            print("Choix invalide, essayez encore.")

menu()