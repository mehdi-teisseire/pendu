from inputs import  get_input, render_text
import pygame

from inputs import get_input

# Menu Errors
def player_name_issue(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Oupps il y a un problème"
    fifth = " "
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def invalid_player_name(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth ="Le nom que vous avez entré est invalide."
    fifth = "Assurez-vous qu'il contient au moins 4 lettres"
    sixth = "et uniquement des lettres."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def player_word_issue(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third ="Le mot que vous avez fourni est invalide."
    fourth ="Vérifiez qu'il contient le bon nombre de caractères,"
    fifth = "uniquement des lettres, sans espaces,"
    sixth = "'-' est autorisé pour les mots composés."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def name_already_registered(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Ce nom est déjà enregistré."
    fifth = "Veuillez en choisir un autre."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def invalid_level_choice_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Choix de niveau invalide."
    sixth = " "
    seventh = "Veuillez entrer un nombre entre 1 et 4."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def invalid_choice_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Erreur."
    sixth = " "
    seventh = "Veuillez entrer 1 ou 2. "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)


def error_happen_adding_word(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Une erreur est survenue lors de l'ajout du mot."
    sixth = "Veuillez réessayer."
    seventh = "Appuyez \"Entrée\" pour continuer. "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def invalid_word_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Ce mot n'est pas valide."
    sixth = "Veuillez réessayer."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def invalid_choice_mess_3(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Choix invalide."
    sixth = " "
    seventh = "Veuillez entrer 1, 2 ou 3."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def invalid_choice_mess_1(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Choix invalide."
    sixth = " "
    seventh = "Veuillez entrer 1."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)


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
def invalid_level_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur : un niveau non valide à été entré."
    fifth = "Veuillez réessayer."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def lenght_error_mess(screen, criteria):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = "Erreur."
    fourth = f"le mot doit comporter entre {criteria['min_length']}"
    fifth = f"et {criteria['max_length']} lettres,"
    sixth = "incluant les traits d'union."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def no_space_error_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur."
    fifth = "le mot ne doit pas contenir d'espaces."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def word_already_in_collection_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur."
    fifth = "Le mot est déjà présent dans la collection."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def no_space_word_error_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Erreur."
    fifth = "Le mot ne doit contenir que des lettres,"
    sixth = "ou des traits d'union, sans espaces."
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def not_in_french_dictionnary_error_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = "Erreur."
    fourth = "Ce mot n'a pas été trouvé"
    fifth = "dans le dictionnaire français."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

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
def empty_input_error(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "L'entrée ne peut pas être vide."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def space_input_error(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "L'entrée ne peut pas être un espace."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

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

def enter_name_to_register(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = "D'accord !"
    fifth = "Veuillez entrer votre nom pour vous enregistrer."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def you_chose_level(screen, chosen_level):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = f"Vous avez choisi le niveau : {chosen_level}."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def return_menu_mess(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "Retour au menu ..."
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def word_added_succesfully(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "Votre mot a été ajouté à la collection !"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def return_first_menu(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third = " "
    fourth = " "
    fifth = "Retour au menu principal"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Scores
def score_tab_display(screen, sorted_scores):
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Tableau des Scores") 
    #render_text(screen, "=== Tableau des Scores ===", (50, 50))
    first = "=== Tableau des Scores ==="
    second = "Nom du Joueur    Score"
    third = for_each_player_name_score(sorted_scores)

    get_input(screen, first, second, third[0] if third else " ", " " if len(third) < 2 else third[1], " " if len(third) < 3 else third[2], " " if len(third) < 4 else third[3], " " if len(third) < 5 else third[4], " " if len(third) < 6 else third[5], " " if len(third) < 7 else third[6], " " if len(third) < 8 else third[7], " " if len(third) < 9 else third[8], " " if len(third) < 10 else third[9])

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

# Graphical representation of errors
def errors_remaining0_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" ==========Y= "
    fourteenth =" ||/       |  "
    fifteenth =" ||        0  "
    sixteenth =" ||       /|\ "
    seventeenth =" ||       /|  "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()
    

def errors_remaining1_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" ||/       |  "
    fifteenth =" ||        0  "
    sixteenth =" ||       /|\ "
    seventeenth =" ||       /|  "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining2_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" ||        0  "
    sixteenth =" ||       /|\ "
    seventeenth =" ||       /|  "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining3_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" ||       /|\ "
    seventeenth =" ||       /|  "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining4_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth ="  "
    sixteenth =" "
    seventeenth =" ||       /|  "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining5_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" "
    seventeenth =" "
    eighteenth ="=============="
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining6_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" "
    seventeenth =" "
    eighteenth = " "
    nineteenth ="||  ||  ||  ||"
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining7_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" "
    seventeenth =" "
    eighteenth =" "
    nineteenth =" "
    twentieth = "=============="
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining8_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" "
    seventeenth =" "
    eighteenth =" "
    nineteenth =" "
    twentieth = " "
    twentieth_one ="||  ||  ||  ||"
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining9_graph(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" "
    seventeenth =" "
    eighteenth =" "
    nineteenth =" "
    twentieth = " "
    twentieth_one = " "
    twentieth_two ="=============="
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()

def errors_remaining10_graph(screen,display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Raté, essayez encore !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    thirteenth =" "
    fourteenth =" "
    fifteenth =" "
    sixteenth =" "
    seventeenth =" "
    eighteenth =" "
    nineteenth =" "
    twentieth = " "
    twentieth_one =" "
    twentieth_two =" "
    twentieth_tree = "||  ||  ||  ||"
    input_letter =  get_input(screen,first, second, third , fourth, fifth, sixth, 
                              seventh, eighth, ninth, tenth, eleventh , twelfth , 
                              thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, 
                              eighteenth , nineteenth, twentieth, twentieth_one, twentieth_two,
                                twentieth_tree)
    return input_letter[0:1].lower()


def won_mess(screen, solution):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth =f"Vous avez gagné ! Le mot était : {solution}"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

def lose_mess(screen, solution):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =  f"Vous avez perdu ! : Le mot était : {solution}."
    fifth ="Ne vous découragez pas et essayez encore !"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer."
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Scores
def score_tab_display(screen, sorted_scores):
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Tableau des Scores") 
    #render_text(screen, "=== Tableau des Scores ===", (50, 50))
    first = "=== Tableau des Scores ==="
    second = "Nom du Joueur              Score"
    third = for_each_player_name_score(sorted_scores)

    get_input(screen, first, second, third[0] if third else " ", " " if len(third) < 2 else third[1], " " if len(third) < 3 else third[2], " " if len(third) < 4 else third[3], " " if len(third) < 5 else third[4], " " if len(third) < 6 else third[5], " " if len(third) < 7 else third[6], " " if len(third) < 8 else third[7], " " if len(third) < 9 else third[8], " " if len(third) < 10 else third[9])

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
"""
# Scores
def score_tab_title(screen):
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Tableau des Scores") 
    first_message = "=== Tableau des Scores ==="
    return get_input(screen, first_message, "", "", "")

def player_score(screen):
    first_message = "Nom du Joueur    Score"
    return get_input(screen, first_message, "", "", "")

def for_each_player_name_score(screen, players):    
    y_position = 90   
    for name, score in players:        
        first_message = f"{name}    {score}"
        render_text(screen, first_message, (50, y_position))        
        y_position += 25

# Menu Errors
def player_name_issue(screen):
    render_text(screen, "Oupps il y a un problème", (50, 50))

def invalid_player_name(screen):
    render_text(screen, "Le nom que vous avez entré est invalide. Assurez-vous ", (50, 100))
    render_text(screen, "qu'il contient au moins 4 lettres et uniquement des lettres.", (50, 100))

def player_word_issue(screen):
    render_text(screen, "Le mot que vous avez fourni est invalide.", (50, 150))
    render_text(screen, "Vérifiez qu'il contient le bon nombre de caractères,", (50, 150))
    render_text(screen, "uniquement des lettres, sans espaces,", (50, 150))
    render_text(screen, "'-' est autorisé pour les mots composés.", (50, 150))


def name_already_registered(screen):
    render_text(screen, "Ce nom est déjà enregistré. Veuillez en choisir un autre.", (50, 200))

def invalid_level_choice_mess(screen):
    render_text(screen, "Choix de niveau invalide.", (50, 250))
    render_text(screen, "Veuillez entrer un nombre entre 1 et 4.", (50, 250))

def invalid_choice_mess(screen):
    render_text(screen, "Erreur : Veuillez entrer 1 ou 2.", (50, 300))

def error_happen_adding_word(screen):
    render_text(screen, "Une erreur est survenue lors de l'ajout du mot.", (50, 350))
    render_text(screen, "Veuillez réessayer.", (50, 350))

def invalid_word_mess(screen):
    render_text(screen, "Ce mot n'est pas valide. Veuillez essayer à nouveau.", (50, 400))

def invalid_choice_mess_3(screen):
    render_text(screen, "Choix invalide. Veuillez entrer 1, 2 ou 3.", (50, 450))

def invalid_choice_mess_1(screen):
    render_text(screen, "Choix invalide. Veuillez entrer 1.", (50, 500))

def invalid_choice_try_again(screen):
    render_text(screen, "Choix invalide. Veuillez essayez encore une fois.", (50, 550))

# Menu messages
def play_as_guest(screen):
    render_text(screen, "Bienvenue, vous jouez en tant qu'invité !", (50, 600))

def welcome_player(screen, player_name):
    render_text(screen, f"Bienvenue de nouveau, {player_name}!", (50, 650))
    render_text(screen, f"Vos nouveaux exploits s'ajouteront aux précédents !", (50, 650))

def enter_name_to_register(screen):
    render_text(screen, "D'accord, veuillez entrer votre nom pour vous enregistrer.", (50, 700))

def saved_your_name(screen):
    render_text(screen, "Votre nom a été sauvegardé avec succès. Bienvenue dans le jeu !", (50, 750))

def you_chose_level(screen, chosen_level):
    render_text(screen, f"Vous avez choisi le niveau : {chosen_level}.", (50, 800))

def return_menu_mess(screen):
    render_text(screen, "Retour au menu ...", (50, 850))

def word_added_succesfully(screen):
    render_text(screen, "Votre mot a été ajouté à la collection avec succès !", (50, 900))

def return_first_menu(screen):
    render_text(screen, "Retour au menu principal", (50, 950))

#def tanks_for_playing(screen):
    #render_text(screen, "Merci d'avoir joué ! À bientôt.", (50, 1000))

# Menus
def select_difficulty_menu(screen):
    render_text(screen, "=== Choisissez Votre Destin ===", (50, 50))
    render_text(screen, "(+) Facile      (++++) Très Dur", (50, 70))
    render_text(screen, "1. La Faucheuse (++++)", (50, 90))
    render_text(screen, "2. Le Dernier Souffle (+++)", (50, 110))
    render_text(screen, "3. La Corde au Cou (++)", (50, 130))
    render_text(screen, "4. Le Dernier Repas (+)", (50, 150))

def first_menu(screen):
    render_text(screen, "=== AU MENU DU PENDU ===", (50, 50))
    render_text(screen, "1. Jouer en Invité", (50, 70))
    render_text(screen, "   Créer un Compte", (50, 90))
    render_text(screen, "   Se Connecter", (50, 110))
    render_text(screen, "2. Lancer une Partie ", (50, 130))
    render_text(screen, "3. Meilleurs Scores ", (50, 150))
    #render_text(screen, "4. Quitter le Jeu", (50, 170))

def sub_menu_player_choice(screen):
    render_text(screen, "===== Que voulez-vous faire ? =====", (50, 50))
    render_text(screen, "1. Jouer avec un Mot Aléatoire", (50, 70))
    render_text(screen, "2. Ajouter un Mot à la Collection", (50, 90))
    render_text(screen, "3. Revenir au Menu Principal", (50, 110))
    

# Rules errors
def invalid_level_mess(screen):
    render_text(screen, "Erreur : un niveau non valide à été entré. Veuillez réessayer.", (50, 1800))

def lenght_error_mess(screen, criteria):
    render_text(screen, f"Erreur: le mot doit comporter entre {criteria['min_length']}", (50, 1850))
    render_text(screen, f"et {criteria['max_length']} lettres, incluant les traits d'union.", (50, 1850))

def no_space_error_mess(screen):
    render_text(screen, "Erreur: le mot ne doit pas contenir d'espaces.", (50, 1900))

def word_already_in_collection_mess(screen):
    render_text(screen, "Erreur: Le mot est déja présent dans la collection.", (50, 1950))

def no_space_word_error_mess(screen):
    render_text(screen, "Erreur: le mot ne doit contenir que des lettres", (50, 2000))
    render_text(screen, "ou des traits d'union, sans espaces.", (50, 2000))

def not_in_french_dictionnary_error_mess(screen):
    render_text(screen, "Erreur: ce mot n'a pas été trouvé dans le dictionnaire français.", (50, 2050))

def file_do_not_exist_error(screen, filename):
    render_text(screen, f"Erreur: Le fichier {filename} n'existe pas.", (50, 2100))

# Play errors
def empty_input_error(screen):
    render_text(screen, "L'entrée ne peut pas être vide.", (50, 2150))

def space_input_error(screen):
    render_text(screen, "L'entrée ne peut pas être un espace.", (50, 2200))

def invalid_character_errors(screen):
    render_text(screen, "Caractère invalide. Veuillez entrer une lettre.", (50, 2250))

# Rules menu 
def hangman_title(screen):
    render_text(screen, "=== LE JEU DU PENDU ===", (50, 50))

def word_to_guess(screen, display_word):
    render_text(screen, "Le mot à deviner : ", (220, 90))
    render_text(screen, display_word, (50, 130))

def number_errors(screen, errors_remaining):
    render_text(screen, f"Vous avez encore {errors_remaining} erreurs restantes.", (50, 2450))

def letters_used(screen, letters_tried):
    render_text(screen, "Les lettres déja utilisées :", (50, 2500))
    render_text(screen, str(letters_tried), (50, 2500))

def already_used_letter(screen):
    render_text(screen, "Cette lettre a déjà été utilisée.", (50, 2550))
    render_text(screen, "Veuillez en proposer une nouvelle.", (50, 2550)) 

def well_done(screen):
    render_text(screen, "Bien joué!", (50, 2600))

def not_this_time(screen):
    render_text(screen, "Pas cette fois, essayez encore !", (50, 2650))

# Graphical representation of errors

def errors_remaining0_graph(screen):
    render_text(screen, " ==========Y= ", (50, 90)) 

def errors_remaining1_graph(screen):
    render_text(screen, " ||/       |  ", (50, 110))

def errors_remaining2_graph(screen):
    render_text(screen, " ||        0  ", (50, 130))

def errors_remaining3_graph(screen):
    render_text(screen, r" ||       /|\ ", (50, 150))

def errors_remaining4_graph(screen):
    render_text(screen, " ||       /|  ", (50, 170))

def errors_remaining5_graph(screen):
    render_text(screen, "==============", (50, 190))

def errors_remaining6_graph(screen):
    render_text(screen, "||  ||  ||  ||", (50, 210))

def errors_remaining7_graph(screen):
    render_text(screen, "==============", (50, 230))

def errors_remaining8_graph(screen):
    render_text(screen, "||  ||  ||  ||", (50, 250))

def errors_remaining9_graph(screen):
    render_text(screen, "==============", (50, 270))

def errors_remaining10_graph(screen):
    render_text(screen, "||  ||  ||  ||", (50, 290)) 

def won_mess(screen, solution):
    render_text(screen, f"Vous avez gagné ! Le mot était : {solution}", (50, 520))

def lose_mess(screen, solution):
    render_text(screen, f"Vous avez perdu ! : Le mot était : {solution}.", (50, 540))
    render_text(screen,"Ne vous découragez pas et essayez encore !", (50, 560))

# Scores
def score_tab_title(screen):
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Tableau des Scores") 
    render_text(screen, "=== Tableau des Scores ===", (50, 50))

def player_score(screen):
    render_text(screen, "Nom du Joueur    Score", (50, 70))

def for_each_player_name_score(screen, players):    
    y_position = 90   
    for name, score in players:        
        render_text(screen, f"{name}    {score}", (50, y_position))        
        y_position += 25  
"""