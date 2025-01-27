
import pygame

# pygame render text
def render_text(screen, text, position, font_size=16, color=(255, 255, 255)):
    font = pygame.font.Font("meiryo.ttc", font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)


# Register to score or play as a guest
def input_register_or_guest(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Souhaitez-vous vous enregistrer "
    sixth = "et participer au classement (1)"
    seventh = "ou jouer en tant qu'invité (2) ? : "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Check if player is coming back or if he is knew
def input_registered_before(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = " "
    sixth = "Vous êtes-vous déjà "
    seventh = "enregistré auparavant ? (oui-non)"
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Enter your name to log or create account
def input_enter_name(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = " "
    sixth = " "
    seventh = "Entrez votre nom : "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Register again or new account
def input_try_register_again_or_no(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth ="Nom non trouvé. "
    fifth = "Voulez-vous essayer à nouveau (1) "
    sixth = "ou vous enregistrer "
    seventh = "avec un nouveau nom (2) ? :"
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Select difficulty menu
def input_enter_choice1_4(screen):
    first = "=== Choisissez Votre Destin ==="
    second = " "
    third = "(+) Facile            (++++) Très Dur"
    fourth = " "
    fifth = "1. La Faucheuse (++++)"
    sixth = "2. Le Dernier Souffle (+++)"
    seventh = "3. La Corde au Cou (++)"
    eighth = "4. Le Dernier Repas (+)"
    ninth = " "
    tenth = "Entrez votre choix (1-2-3-4) : "
    return get_input(screen,first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth )

# Play again
def input_play_again_or_menu(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Voulez-vous refaire une partie ?"
    sixth = " 1 pour oui"
    seventh = "2 pour retourner au menu :"
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Add a word to collection
def input_player_word_rules(screen, validation_criteria, chosen_level):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Veuillez entrer votre mot" 
    fifth = f"(entre {validation_criteria[chosen_level]['min_length']} et {validation_criteria[chosen_level]['max_length']} lettres)."
    sixth = "Pour les mots composés,"
    seventh = "utilisez le format XXX-XXXX : ".lower()
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# The big hangman menu
def input_choice1_3(screen):
    first ="====== AU MENU DU PENDU ======"
    second = " "
    third ="              1. Jouer en Invité"
    fourth ="                  Créer un Compte"
    fifth = "                  Se Connecter"
    sixth ="              2. Lancer une Partie "
    seventh ="              3. Meilleurs Scores "
    eighth = " "
    ninth = "Entrez votre choix (1-2-3) : "
    return get_input(screen,first,second,third,fourth,fifth,sixth,seventh,eighth,ninth )

# Sub menu choose random word or add to collection
def input_enter_choice1_3(screen):
    first =  "===== Que voulez-vous faire ? ====="
    second =" "
    third = "1. Jouer avec un Mot Aléatoire"
    fourth = "2. Ajouter un Mot à la Collection"
    fifth = "3. Revenir au Menu Principal"
    sixth = " "
    seventh = "Veuillez entrer votre choix (1-2-3) :"
    return get_input(screen,first,second,third,fourth,fifth,sixth,seventh)

# Return to menu
def input_return_menu(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = " "
    sixth = " "
    seventh = "Pour retourner au menu, entrez (1) : "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Enter your letter to play
def input_enter_your_letter(screen, display_word, errors_remaining, letters_tried):
    first="======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eight = str(letters_tried)
    ninth = " "
    tenth = "Proposez une lettre : "
    input_letter = get_input(screen, first, second,third,fourth,fifth,sixth,
                             seventh,eight,ninth,tenth)
    return input_letter[0:1].lower()

# Already used letter
def input_already_used_letter(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Lettre déjà utilisée."
    eleventh = "Appuyez \"Entrée\" pour continuer. "
    twelfth = " "
    input_letter = get_input(screen,first, second, third , fourth, fifth, 
                             sixth, seventh, eighth, ninth, tenth, eleventh , twelfth)
    return input_letter[0:1].lower()

# Well done player you guess the right letter
def input_well_done(screen, display_word, errors_remaining, letters_tried):
    first= "======= LE JEU DU PENDU ======="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Il reste {errors_remaining} erreurs."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Bien joué !"
    eleventh = "Appuyez \"Entrée\" pour continuer."
    twelfth = " "
    input_letter = get_input(screen,first, second, third , fourth, fifth, 
                             sixth, seventh, eighth, ninth, tenth, eleventh , twelfth )
    return input_letter[0:1].lower()

# Not the good letter
def input_not_this_time(screen, display_word, errors_remaining, letters_tried):
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
    input_letter = get_input(screen,first, second, third , fourth, fifth, 
                             sixth, seventh, eighth, ninth, tenth, eleventh , twelfth )
    return input_letter[0:1].lower()

# Welcome new player
def input_welcome_new_player(screen, player_name):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth = "Votre nom à été sauvegardé."
    fifth = f"Bienvenue dans le jeu, {player_name} ! "
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer. "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)

# Welcome back player
def input_welcome_player(screen, player_name):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =f"Bienvenue de nouveau, {player_name}!"
    fourth = "Vos nouveaux exploits "
    fifth = "s'ajouteront aux précédents !"
    sixth = " "
    seventh = "Appuyez \"Entrée\" pour continuer. "
    return get_input(screen,player_name, first, second,third,fourth,fifth,sixth,seventh)

# Play as a guest
def input_play_as_guest(screen):
    first ="======= LE JEU DU PENDU ======="
    second = " "
    third =" "
    fourth =" "
    fifth = "Bienvenue ! "
    sixth = "Vous jouez en tant qu'invité."
    seventh = "Appuyez \"Entrée\" pour continuer. "
    return get_input(screen, first, second,third,fourth,fifth,sixth,seventh)


# To handle player interactions
def get_input(screen, first= '', second= '', third = '', fourth = '', fifth = '', sixth = '', seventh = '',
               eighth= '', ninth = '', tenth = '', eleventh = '', twelfth = '', thirteenth = '', fourteenth = '', 
               fifteenth = '', sixteenth = '', seventeenth= '', eighteenth = '', nineteenth= '', twentieth = '',
               twentieth_one ='', twentieth_two = '', twentieth_tree = ''):
    input_box_width = 300
    input_box_height = 25
    input_box_x = (900 - input_box_width) // 2
    input_box_y = 600 - input_box_height - 50

    input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)
    color_active = pygame.Color('white')
    color = color_active 
    text = ''
    font = pygame.font.Font(None, 25)

    error_lines = [first, second, third , fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh , twelfth 
                   , thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth , nineteenth, twentieth,
                     twentieth_one, twentieth_two, twentieth_tree]
    error_lines = [line for line in error_lines if line] 

    while True:
        screen.fill((0, 0, 0))

        for i, line in enumerate(error_lines):
            render_text(screen, line, (input_box_x, input_box_y - 500 + i * 20)) 

        txt_surface = font.render(text, True, color)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text  
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]  
                else:
                    text += event.unicode  

        pygame.display.flip()
