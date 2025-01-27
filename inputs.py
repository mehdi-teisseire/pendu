
import pygame

def render_text(screen, text, position, font_size=25, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

"""
def get_input(screen, first= '', second= '', third = '', fourth = '', fifth = '', sixth = '', seventh = '', eighth= '', ninth = '', tenth = '', eleventh = '', twelfth = '', thirteenth = '', fourteenth = '', fifteenth = '', sixteenth = '', seventeenth= '', eighteenth = '', nineteenth= '', twentieth = ''):
    input_box_width = 140
    input_box_height = 25
    input_box_x = (900 - input_box_width) // 2
    input_box_y = 600 - input_box_height - 50

    input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)
    color_inactive = pygame.Color('magenta')
    color_active = pygame.Color('white')
    color = color_inactive
    text = ''
    active = False
    font = pygame.font.Font(None, 25)

    # Collect error messages into a list
    error_lines = [first, second, third , fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh , twelfth , thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth , nineteenth, twentieth]
    error_lines = [line for line in error_lines if line]  # Filter out empty lines

    while True:
        screen.fill((0, 0, 0))

        # Render the first part of the prompt
        #render_text(screen, first, (input_box_x, input_box_y - 200))

        # Render the second part of the prompt
        #render_text(screen, second, (input_box_x, input_box_y - 180))

        # Render the error messages below the input box
        for i, line in enumerate(error_lines):
            render_text(screen, line, (input_box_x, input_box_y - 200 + i * 20))  # Adjust position based on index

        # Render the text input
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text  
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]  
                    else:
                        text += event.unicode  

        pygame.display.flip()
"""
# Menu inputs

def input_register_or_guest(screen):
    first = "Souhaitez-vous vous enregistrer et participer"
    second = "au classement (1) ou jouer en tant qu'invité (2) ? : "
    return get_input(screen, first, second)

def input_registered_before(screen):
    first ="Vous êtes-vous déjà enregistré auparavant ?"
    second = "(oui-non) : "
    return get_input(screen, first, second)

def input_enter_name(screen):
    first = ""
    second = "Entrez votre nom : "
    return get_input(screen, first, second)

def input_try_register_again_or_no(screen):
    first = "Nom non trouvé.Voulez-vous essayer à nouveau (1)"
    second = "ou vous enregistrer avec un nouveau nom (2) ? : "
    return get_input(screen, first, second)

def input_enter_choice1_4(screen):
    first = "=== Choisissez Votre Destin ==="
    second = "(+) Facile      (++++) Très Dur"
    third = "1. La Faucheuse (++++)"
    fourth = "2. Le Dernier Souffle (+++)"
    fifth = "3. La Corde au Cou (++)"
    sixth = "4. Le Dernier Repas (+)"
    seventh = " "
    eighth = "Entrez votre choix (1-2-3-4) : "
    return get_input(screen,first,second,third,fourth,fifth,sixth,seventh,eighth )

def input_play_again_or_menu(screen):
    first = "Voulez-vous refaire une partie ?"
    second = "1 pour oui, 2 pour retourner au menu : "
    return get_input(screen, first, second)

def input_player_word_rules(screen, validation_criteria, chosen_level):
    first = f"Veuillez entrer votre mot (entre {validation_criteria[chosen_level]['min_length']} et {validation_criteria[chosen_level]['max_length']} lettres)." 
    second = "Pour les mots composés, utilisez le format XXX-XXXX : ".lower()
    return get_input(screen, first, second)

def input_choice1_3(screen):
    first = "=== AU MENU DU PENDU ==="
    second = "1. Jouer en Invité"
    third = "   Créer un Compte"
    fourth =  "   Se Connecter"
    fifth = "2. Lancer une Partie "
    sixth = "3. Meilleurs Scores "
    seventh = " "
    eighth = "Entrez votre choix (1-2-3) : "
    return get_input(screen,first,second,third,fourth,fifth,sixth,seventh,eighth )


def input_enter_choice1_3(screen):
    first =  "===== Que voulez-vous faire ? ====="
    second =" "
    third = "1. Jouer avec un Mot Aléatoire"
    fourth = "2. Ajouter un Mot à la Collection"
    fifth = "3. Revenir au Menu Principal"
    sixth = " "
    seventh = "Veuillez entrer votre choix (1-2-3) :"
    return get_input(screen,first,second,third,fourth,fifth,sixth,seventh)

def input_return_menu(screen):
    first = "Pour retourner au menu, entrez (1) : "
    return get_input(screen, first)

# Rules inputs
def input_enter_your_letter(screen, display_word, errors_remaining, letters_tried):
    first= "=== LE JEU DU PENDU ==="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Vous avez encore {errors_remaining} erreurs restantes."
    seventh = "Les lettres déjà utilisées :"
    eight = str(letters_tried)
    ninth = " "
    tenth = "Proposez une lettre : "
    input_letter = get_input(screen, first, second,third,fourth,fifth,sixth,seventh,eight,ninth,tenth)
    return input_letter[0:1].lower()

def input_already_used_letter(screen, display_word, errors_remaining, letters_tried):
    first= "=== LE JEU DU PENDU ==="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Vous avez encore {errors_remaining} erreurs restantes."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Cette lettre a déjà été utilisée."
    eleventh = " "
    twelfth = "Proposez une lettre : "
    input_letter = get_input(screen,first, second, third , fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh , twelfth)
    return input_letter[0:1].lower()

def input_well_done(screen, display_word, errors_remaining, letters_tried):
    first= "=== LE JEU DU PENDU ==="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Vous avez encore {errors_remaining} erreurs restantes."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = " Bien joué !"
    eleventh = " "
    twelfth = "Proposez une lettre : "
    input_letter = get_input(screen,first, second, third , fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh , twelfth )
    return input_letter[0:1].lower()


def input_not_this_time(screen, display_word, errors_remaining, letters_tried):
    first= "=== LE JEU DU PENDU ==="
    second =" "
    third =  "Le mot à deviner : "
    fourth = display_word
    fifth = " "
    sixth = f"Vous avez encore {errors_remaining} erreurs restantes."
    seventh = "Les lettres déjà utilisées :"
    eighth = str(letters_tried)
    ninth = " "
    tenth = "Pas cette fois, essayez encore !"
    eleventh = " "
    twelfth = "Proposez une lettre : "
    input_letter = get_input(screen,first, second, third , fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh , twelfth )
    return input_letter[0:1].lower()

# welcome player

def input_welcome_new_player(screen, player_name):
    first = "Votre nom à été sauvegardé avec succès."
    second = f"Bienvenue dans le jeu, {player_name} ! "
    third ="Pour retourner au menu, entrez (1) : "
    return get_input(screen, first, second, third)

def input_welcome_player(screen, player_name):
    first = f"Bienvenue de nouveau, {player_name}!"
    second = "Vos nouveaux exploits s'ajouteront aux précédents !"
    third ="Pour retourner au menu, entrez (1) : "
    return get_input(screen, first, second, third)

def input_play_as_guest(screen):
    first= "Bienvenue, vous jouez en tant qu'invité !"
    second ="Pour retourner au menu, entrez (1) :"
    return get_input(screen, first, second)


# if i want to input stay active
def get_input(screen, first= '', second= '', third = '', fourth = '', fifth = '', sixth = '', seventh = '', eighth= '', ninth = '', tenth = '', eleventh = '', twelfth = '', thirteenth = '', fourteenth = '', fifteenth = '', sixteenth = '', seventeenth= '', eighteenth = '', nineteenth= '', twentieth = ''):
    input_box_width = 140
    input_box_height = 25
    input_box_x = (900 - input_box_width) // 2
    input_box_y = 600 - input_box_height - 50

    input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)
    color_inactive = pygame.Color('green')
    color_active = pygame.Color('white')
    color = color_active  # Set color to active since we want it always active
    text = ''
    font = pygame.font.Font(None, 25)

    # Collect error messages into a list
    error_lines = [first, second, third , fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh , twelfth , thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth , nineteenth, twentieth]
    error_lines = [line for line in error_lines if line]  # Filter out empty lines

    while True:
        screen.fill((0, 0, 0))

        # Render the error messages below the input box
        for i, line in enumerate(error_lines):
            render_text(screen, line, (input_box_x, input_box_y - 200 + i * 20))  # Adjust position based on index

        # Render the text input
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            # Always consider the input box active
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return text  
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]  
                else:
                    text += event.unicode  

        pygame.display.flip()
