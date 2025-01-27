
import display
from rules import  name_is_valid, word_is_valid, validation_criteria, play_game
from score import update_score, display_score_table
from inputs import *

# To check if the player name is in the score file
def name_exists(player_name):
    try:
        with open('score.txt', 'r', encoding="utf-8") as score_file:
            registered_names = [line.split(",")[0].strip() for line in score_file.readlines()]
            return player_name in registered_names
    except FileNotFoundError:
        return False
    
# To register login or play as guest
def register_player(screen):
    while True: 
        play_guest = input_register_or_guest(screen) 
        
        if play_guest == '2':
            input_play_as_guest(screen) 
            return
        
        if play_guest == '1':
            while True:
                has_account = input_registered_before(screen)
                if has_account.lower() in ['oui', 'non']: 
                    break
                else:
                    display.invalid_choice_mess(screen) 
            
            player_name = input_enter_name(screen)
            
            if has_account == 'oui':
                if name_exists(player_name):
                    input_welcome_player(screen, player_name)
                    return player_name
                else:
                    try_again = input_try_register_again_or_no(screen)
                    if try_again == '1':
                        continue
                    elif try_again == '2':
                        display.enter_name_to_register(screen)
                        break 
                    
            elif has_account == 'non':
                if name_is_valid(player_name) and not name_exists(player_name):
                    try: 
                        with open('score.txt', 'a', encoding="utf-8") as score: 
                            score.write("\n" + player_name + ",0")
                            input_welcome_new_player(screen, player_name)
                            return player_name
                    except Exception as e: 
                        display.player_name_issue(screen)
                else:
                    if not name_is_valid(player_name):
                        display.invalid_player_name(screen)
                    else:
                        display.name_already_registered(screen)

        display.invalid_choice_mess(screen)

# To select the game level
def select_difficulty(screen):
     #input_enter_choice1_4(screen)

    while True: 
        level_choice = input_enter_choice1_4(screen)
        level_mapping = {
            "1": "très dur",
            "2": "dur",
            "3": "normal",
            "4": "facile"
        }
        chosen_level = level_mapping.get(level_choice)
        
        if chosen_level:
            return level_choice, chosen_level
        else:
            display.invalid_level_choice_mess(screen)

# Loop for playing multiple games and register scores
def play_game_option(screen, player_name, level_choice):

    while True:

        won = play_game(screen, level_choice) 
        update_score(player_name, level_choice, won)
        
        play_again = input_play_again_or_menu(screen)
        if play_again == "1":
            level_choice , chosen_level = select_difficulty(screen)
            display.you_chose_level(screen, chosen_level)
        elif play_again == "2":
            display.return_menu_mess(screen)

            return
        else:
            display.invalid_choice_mess(screen)

# To add a word to a collection
def add_word_option(screen, chosen_level):
    while True: 
        player_word = input_player_word_rules(screen, validation_criteria, chosen_level)
        
        if word_is_valid(screen, player_word, chosen_level):
            try:
                filename_mapping = {
                    'très dur': 'word1.txt',
                    'dur': 'word2.txt',
                    'normal': 'word3.txt',
                    'facile': 'word4.txt'
                }
                with open(filename_mapping[chosen_level], "a", encoding= "utf-8") as word_file:
                    word_file.write("\n" + player_word)
                display.word_added_succesfully(screen)
                return
            except Exception :
                display.error_happen_adding_word(screen)
        else:
            display.invalid_word_mess(screen)

# To organize all the navigation The big menu
def menu(screen):
    player_name = ""

    while True:
        #input_choice1_3(screen)
        
        choice = input_choice1_3(screen)

        if choice == '1':
            player_name = register_player(screen)

        elif choice == "2":
            level_choice,chosen_level = select_difficulty(screen)

            while True:
                #display.sub_menu_player_choice(screen)

                word_choice = input_enter_choice1_3(screen)

                if word_choice == "1":
                    play_game_option(screen, player_name, level_choice)

                elif word_choice == "2":
                    add_word_option(screen, chosen_level)
                elif word_choice == "3":
                    display.return_first_menu(screen)
                    break
                else: 
                    display.invalid_choice_mess_3(screen)

        elif choice == "3":          
            display_score_table(screen)
            while True:
                return_to_menu = input_return_menu(screen)
                if return_to_menu == "1":
                    break
                else:
                    display.invalid_choice_mess_1(screen)
            
        else:
            display.invalid_choice_try_again(screen)            

