# Menu Errors
def player_name_issue():
    print("Oupps il y a un problème")

def invalid_player_name():
     print("Le nom est invalide: Assurez vous qu'il contient\nau moins 4 lettres et seulement des lettres.")

def player_word_issue():
    print("Le mot est invalide : Assurez vous de rentrer le bon nombre de carractères,\nseulement des lettres, sans espaces vides, '-' est autorisé pour les mots composés,\net verifiez que votre mot est bien dans le dictionnaire.")

def name_already_registered():
    print("Ce nom est déjà enregistré. Veuillez en choisir un autre.")

def invalid_level_choice_mess():
    print("Choix de niveau invalide.\nVeuillez entrer un nombre entre 1 et 4.")
    print(" ")

def invalid_choice_mess():
    print("Choix invalide. Veuillez entrer 1 ou 2.")

def error_happen_adding_word():
    print("Une erreur est survenue lors de l'ajout du mot. Veuillez réessayer.")

def invalid_word_mess():
    print("Ce mot n'est pas valide. Veuillez essayer encore.")

def invalid_choice_mess_3():
    print ("Choix invalide. Veuillez entrer 1, 2 ou 3.")

def invalid_choice_mess_1():
    print ("Choix invalide. Veuillez entrer 1.")

def invalid_choice_try_again():
    print("Choix invalide, essayez encore.")

# Menu messages
def welcome_player(player_name):
    print(f"Bienvenue de nouveau, {player_name}!") 

def enter_name_to_register():
     print("D'accord, veuillez entrer votre nom pour vous enregistrer.")  

def saved_your_name():
    print("Votre nom a été sauvegardé.")

def you_chose_level(chosen_level):
    print(f"Vous avez choisi : {chosen_level}.")

def return_menu_mess():
    print("Retour au menu ...")

def word_added_succesfully():
    print("Votre mot a été ajouté à la collection avec succès !")

def return_first_menu():
    print("Retour au menu principal")

def tanks_for_playing():
    print("Merci d'avoir joué ! À bientôt.")
    print(" ")

# Menus
def select_difficulty_menu():
    print("\n=== Choisissez un niveau de difficulté ===")
    print(" ")
    print("1. Plus dur que dur")
    print("2. Dur")
    print("3. Normal")
    print("4. Facile")
    print(" ")

def first_menu():
    print("\n=== MENU DU PENDU ===")
    print(" ")
    print("1. S'enregistrer")
    print("2. JOUER ")
    print("3. Le tableau des scores ")
    print("4. Quitter")  

def sub_menu_player_choice():
    print("\n=== Que voulez-vous faire ? ===")
    print(" ")
    print("1. Jouer avec un mot au hasard")    
    print("2. Ajouter votre mot à notre collection")
    print("3. Retour au menu principal")

#rules errors
def invalid_level_mess():
    print("Erreur : un niveau non valide à été entré.")

def lenght_error_mess(criteria):
    print(f"Erreur: le mot doit faire entre {criteria['min_length']} \net {criteria['max_length']} lettres, incluant les trait d'unions.") 

def no_space_error_mess():
    print("Erreur: le mot ne doit pas contenir d'espaces.")

def word_already_in_collection_mess():
    print("Erreur: Le mot est déja dans la collection.")

def no_space_word_error_mess():
    print("Erreur: le mot ne doit contenir que des lettres ou des traits d'union.")

def not_in_french_dictionnary_error_mess():
    print("Erreur: ce mot n'a pas été trouvé dans le dictionnaire français.")

def file_do_not_exist_error(filename):
    print(f"Erreur: Le fichier {filename} n'existe pas.")

# rules menu 

def hangman_title():
    print("\n")
    print("*** LE JEU DU PENDU ***")

def word_to_guess(display_word):
    print("\nLe mot à deviner : ", display_word)

def number_errors(errors_remaining):
    print(f"Nombre d'erreurs restant : {errors_remaining}")

def letters_used(letters_tried):
    print("Les lettres déja utilisées :\n" + str(letters_tried))

def already_used_letter():
    print("Cette lettre a déjà été utilisée. Veuillez en proposer une autre.") 

def well_done():
    print("Bien joué!")

def not_this_time():
    print("Pas cette fois, essaie encore !\n")

def errors_remaining0_graph():
    print(" ==========Y= ")

def errors_remaining1_graph():
    print(" ||/       |  ")

def errors_remaining2_graph():
    print(" ||        0  ")

def errors_remaining3_graph():
    print(r" ||       /|\ ")

def errors_remaining4_graph():
    print(" ||       /|  ")

def errors_remaining5_graph():
    print("==============")

def errors_remaining6_graph():
    print("||  ||  ||  ||")

def errors_remaining7_graph():
    print("==============")

def errors_remaining8_graph():
    print("||  ||  ||  ||")

def errors_remaining9_graph():
    print("==============")

def errors_remaining10_graph():
    print("||  ||  ||  ||")

def won_mess(solution):
    print(f"\n *** Vous avez gagné ! Le mot était : {solution} *** ")

def lose_mess(solution):
    print(f"\nVous avez perdu ! : Le mot était : {solution}")

# scores

def score_tab_title():
    print("\n=== Tableau des Scores ===")

def player_score():
    print("Nom du Joueur\tScore")

def for_each_player_name_score(name, score):
    print(f"{name}\t\t{score}")