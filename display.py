from inputs import  get_input
import pygame

# Menu Errors
# To display general errors
def player_name_issue(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Oupps il y a un problème"
    fifth = " "
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for invalid name
def invalid_player_name(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth ="Le nom que vous avez entré est invalide."
    fifth = "Assurez-vous qu'il contient au moins 3 lettres"
    sixth = "et uniquement des lettres."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for invalid word
def player_word_issue(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third ="Le mot que vous avez fourni est invalide."
    fourth ="Vérifiez qu'il contient le bon nombre de caractères,"
    fifth = "uniquement des lettres, sans espaces,"
    sixth = "'-' est autorisé pour les mots composés."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for already registered player name
def name_already_registered(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Ce nom est déjà enregistré."
    fifth = "Veuillez en choisir un autre."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

#To display error message for invalid level choice
def invalid_level_choice_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Choix de niveau invalide."
    sixth = " "
    seventh = "Veuillez entrer un nombre entre 1 et 4."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for invalid entry one or two
def invalid_choice_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Erreur."
    sixth = " "
    seventh = "Veuillez entrer 1 ou 2. "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for something bad happening when adding a word 
def error_happen_adding_word(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Une erreur est survenue lors de l'ajout du mot."
    sixth = "Veuillez réessayer."
    seventh = "Appuyez \"Entrée\" pour continuer. "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for invalid word when adding to collection
def invalid_word_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Ce mot n'est pas valide."
    sixth = "Veuillez réessayer."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display invalid choice message, enter 1 2 or 3
def invalid_choice_mess_3(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Choix invalide."
    sixth = " "
    seventh = "Veuillez entrer 1, 2 ou 3."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display invalid choice enter 1
def invalid_choice_mess_1(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Choix invalide."
    sixth = " "
    seventh = "Veuillez entrer 1."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# to display invalid choice try again
def invalid_choice_try_again(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Choix invalide."
    fifth = "Veuillez essayez encore une fois."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Rules errors
# To display error message for invalid difficulty level choice
def invalid_level_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur : un niveau non valide à été entré."
    fifth = "Veuillez réessayer."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message and criteria to register a new word to collection
def lenght_error_mess(screen, criteria):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = "Erreur."
    fourth = f"le mot doit comporter entre {criteria['min_length']}"
    fifth = f"et {criteria['max_length']} lettres,"
    sixth = "incluant les traits d'union."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display invalid error for typing space in the word
def no_space_error_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur."
    fifth = "le mot ne doit pas contenir d'espaces."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for a word already in the collection
def word_already_in_collection_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur."
    fifth = "Le mot est déjà présent dans la collection."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for symbols or numbers in the word
def no_space_word_error_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur."
    fifth = "Le mot ne doit contenir que des lettres,"
    sixth = "ou des traits d'union, sans espaces."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message for the word not in dictionnary
def not_in_french_dictionnary_error_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = "Erreur."
    fourth = "Ce mot n'a pas été trouvé"
    fifth = "dans le dictionnaire français."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display error message in case the file text did not exist
def file_do_not_exist_error(screen, filename):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = "Erreur."
    fifth = f"Le fichier {filename} n'existe pas."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Play errors
# To display error message for an empty entry
def empty_input_error(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "L'entrée ne peut pas être vide."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display an error message for a space in the entry
def space_input_error(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "L'entrée ne peut pas être un espace."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display an error message for an invalid entry (not a letter or hyphen)
def invalid_character_errors(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = "Caractère invalide."
    fifth = "Veuillez entrer une lettre."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Menu messages
# To display a message when a player choose to register with another name
def enter_name_to_register(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = "D'accord !"
    fifth = "Veuillez entrer votre nom "
    sixth = "pour vous enregistrer. "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display a level difficulty message information
def you_chose_level(screen, chosen_level):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = f"Vous avez choisi le niveau : {chosen_level}."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display a return to menu message
def return_menu_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "Retour au menu ..."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display an information message for addind a word succesfully
def word_added_succesfully(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "Votre mot a été ajouté à la collection !"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display a message to return to the menu
def return_first_menu(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "Retour au menu principal"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# To display the win message
def won_mess(screen, solution):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth ="Vous avez gagné !"
    sixth = f"Le mot était : {solution}"
    seventh = "Appuyez \"Entrée\" pour continuer."
    eighth = " "
    ninth = " "
    tenth = " "
    eleventh = " GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    twelfth = " GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    thirteenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    fourteenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    fifteenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ  "
    sixteenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ  "
    seventeenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ  "
    eighteenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    nineteenth =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    twentieth = " GAGNÉ GAGNÉ GAGNÉ GAGNÉ "
    twentieth_one =" GAGNÉ GAGNÉ GAGNÉ GAGNÉ "

    return get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one)

# To display the lose  message
def lose_mess(screen, solution):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Vous avez perdu ! : "
    fifth =F" Le mot était : {solution}."
    sixth = " Ne vous découragez pas !"
    seventh = "Essayez encore !"
    eighth = " "
    ninth = "Appuyez \"Entrée\" pour continuer."
    tenth = " "
    eleventh = " "
    twelfth = " "
    thirteenth =" ==========Y= "
    fourteenth =" ||/                      |  "
    fifteenth =" ||                       0  "
    sixteenth =" ||                      /|\uFF3C"
    seventeenth =" ||                      /|  "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||  ||  ||  ||  || "
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||  ||  ||  ||  || "
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||  ||  ||  ||  || "
    return get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)

# Scores
# To display the best 10 first player
def score_tab_display(screen, sorted_scores):
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Tableau des Scores") 
    #render_text(screen, "=== Tableau des Scores ===", (50, 50))
    first = "=== Tableau des Scores ==="
    second = "Nom du Joueur              Score"
    third = for_each_player_name_score(sorted_scores)
    fourth =" "
    fifth  = "Appuyez \"Entrée\" pour continuer."
    get_input(screen, first, second, third[0] if third else " ", " " if len(third) < 2 else third[1],
               " " if len(third) < 3 else third[2], " " if len(third) < 4 else third[3], " " if len(third) < 5 else third[4],
                 " " if len(third) < 6 else third[5], " " if len(third) < 7 else third[6], " " if len(third) < 8 else third[7],
                 " " if len(third) < 9 else third[8], " " if len(third) < 10 else third[9],fourth,fifth)

# To adjust the displaying of the score tab
def for_each_player_name_score(players):    
    temp_list = []
    spaces = "　　　　　　　　　　　　　　　"
    for name, score in players:

        temp_name = ""
        for i in range(len(name)):
            if name[i] in "àäâ":
                temp_name += chr(65344)
            elif name[i] in "éêèë":
                temp_name += chr(65349)
            elif name[i] in "ïî":
                temp_name += chr(65353)
            elif name[i] in "öôò":
                temp_name += chr(65359)
            elif name[i] in "ûüù":
                temp_name += chr(65365)
            else:    
                temp_name += chr(ord(name[i])+65248)
        
        if len(temp_name) > 15:
            temp_name = temp_name[:14]
        else:
            temp_name = temp_name + spaces[:14-len(temp_name)]
        temp_list.append(f"{temp_name}{score}")
    return temp_list
