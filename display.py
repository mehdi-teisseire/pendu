# Menu Errors
def player_name_issue():
    print("Oupps il y a un problème")

def invalid_player_name():
     print("Le nom que vous avez entré est invalide.\nAssurez-vous qu'il contient\nau moins 4 lettres et uniquement des lettres.")

def player_word_issue():
    print("Le mot que vous avez fourni est invalide.\nVérifiez qu'il contient le bon nombre de carractères,\nuniquement des lettres, sans espaces, '-' est autorisé pour les mots composés.\nAssurez-vous également qu'il figure dans le dictionnaire.")

def name_already_registered():
    print("Ce nom est déjà enregistré. Veuillez en choisir un autre.")

def invalid_level_choice_mess():
    print("Choix de niveau invalide.\nVeuillez entrer un nombre entre 1 et 4.")
    print(" ")

def invalid_choice_mess():
    print("Erreur : Veuillez entrer 1 ou 2.")

def error_happen_adding_word():
    print("Une erreur est survenue lors de l'ajout du mot. Veuillez réessayer.")

def invalid_word_mess():
    print("Ce mot n'est pas valide. Veuillez essayer à nouveau.")

def invalid_choice_mess_3():
    print ("Choix invalide. Veuillez entrer 1, 2 ou 3.")

def invalid_choice_mess_1():
    print ("Choix invalide. Veuillez entrer 1.")

def invalid_choice_try_again():
    print("Choix invalide, veuillez essayez encore une fois.")

# Menu messages
def play_as_guest():
    print("Bienvenue, vous jouez en tant qu'invité !")

def welcome_player(player_name):
    print(f"Bienvenue de nouveau, {player_name}!\nVos nouveaux exploits s'ajouteront aux précedents !") 

def enter_name_to_register():
     print("D'accord, veuillez entrer votre nom pour vous enregistrer.")  

def saved_your_name():
    print("Votre nom a été sauvegardé avec succès. Bienvenue dans le jeu !")

def you_chose_level(chosen_level):
    print(f"Vous avez choisi le niveau : {chosen_level}.")

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
    print("\n=== Choisissez Votre Destin ===")
    print("(+) Facile\t(++++) Très Dur")
    print(" ")
    print("1. La Faucheuse (++++)")
    print("2. Le Dernier Souffle (+++)")
    print("3. La Corde au Cou (++)")
    print("4. Le Dernier Repas (+)")
    print(" ")

def first_menu():
    print("\n=== AU MENU DU PENDU ===")
    print(" ")
    print("1. Jouer en Invité\n\033[3CCréer un Compte\n\033[3CSe Connecter")
    print("2. Lancer une Partie ")
    print("3. Meilleurs Scores ")
    print("4. Quitter le Jeu")  

def sub_menu_player_choice():
    print("\n=== Que voulez-vous faire ? ===")
    print(" ")
    print("1. Jouer avec un Mot Aléatoire")    
    print("2. Ajouter un Mot à la Collection")
    print("3. Revenir au Menu Principal")

#rules errors
def invalid_level_mess():
    print("Erreur : un niveau non valide à été entré. Veuillez réessayer.")

def lenght_error_mess(criteria):
    print(f"Erreur: le mot doit comporter entre {criteria['min_length']} \net {criteria['max_length']} lettres, incluant les traits d'union.") 

def no_space_error_mess():
    print("Erreur: le mot ne doit pas contenir d'espaces.")

def word_already_in_collection_mess():
    print("Erreur: Le mot est déja présent dans la collection.")

def no_space_word_error_mess():
    print("Erreur: le mot ne doit contenir que des lettres ou des traits d'union, sans espaces.")

def not_in_french_dictionnary_error_mess():
    print("Erreur: ce mot n'a pas été trouvé dans le dictionnaire français.")

def file_do_not_exist_error(filename):
    print(f"Erreur: Le fichier {filename} n'existe pas.")

# rules menu 

def hangman_title():
    print("\n")
    print("=== LE JEU DU PENDU ===")

def word_to_guess(display_word):
    print("\nLe mot à deviner : ", display_word)

def number_errors(errors_remaining):
    print(f"Vous avez encore {errors_remaining} erreurs restantes.")

def letters_used(letters_tried):
    print("Les lettres déja utilisées :\n" + str(letters_tried))

def already_used_letter():
    print("Cette lettre a déjà été utilisée. Veuillez en proposer une nouvelle.") 

def well_done():
    print("Bien joué!")

def not_this_time():
    print("Pas cette fois, essayez encore !\n")

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
    print(f"\nVous avez perdu ! : Le mot était : {solution}. Ne vous découragez pas et essayez encore !")

# scores

def score_tab_title():
    print("\n=== Tableau des Scores ===")

def player_score():
    print("Nom du Joueur\tScore")

def for_each_player_name_score(name, score):
    print(f"{name}\t\t{score}")