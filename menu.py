import display
from rules import clear_screen, name_is_valid, word_is_valid, validation_criteria, play_game
import time
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

# To verify if player already have an account
def register_player():
    while True:
        has_account = input_registered_before()
        
        if has_account == 'oui':
            player_name = input_enter_name()
            if name_exists(player_name):
                display.welcome_player(player_name)
                return player_name
            else:
                try_again = input_try_register_again_or_no()
                if try_again == '1':
                    continue
                elif try_again == '2':
                    display.enter_name_to_register()
        
        player_name = input_enter_name()
        if name_is_valid(player_name) and not name_exists(player_name):
            try: 
                with open('score.txt', 'a', encoding="utf-8") as score: 
                    score.write("\n" + player_name + ",0")
                    display.saved_your_name()
                    return player_name
            except Exception as e: 
                display.player_name_issue(e)
        else:
            if not name_is_valid(player_name):
                display.invalid_player_name()
            else:
                display.name_already_registered()

        time.sleep(2)
        clear_screen()
    
# A menu to select the game level
def select_difficulty():
    display.select_difficulty_menu()

    while True: 
        level_choice = input_enter_choice1_4()
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
            display.invalid_level_choice_mess()

 # Loop for playing multiple games and register scores
def play_game_option(player_name, level_choice):

    while True:
        time.sleep(2)
        clear_screen()
        won = play_game(level_choice) 
        update_score(player_name, level_choice, won)
        
        play_again = input_play_again_or_menu()
        if play_again == "1":
            level_choice , chosen_level = select_difficulty()
            display.you_chose_level(chosen_level)
        elif play_again == "2":
            display.return_menu_mess()
            time.sleep(2)
            clear_screen()
            return
        else:
            display.invalid_choice_mess()

# To add a word to a collection
def add_word_option(chosen_level):
    while True: 
        player_word = input_player_word_rules(validation_criteria, chosen_level)
        
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
                display.word_added_succesfully()
                return
            except Exception :
                display.error_happen_adding_word()
        else:
            display.invalid_word_mess()

# To organize all the navigation The big menu
def menu():
    player_name = ""

    while True:
        display.first_menu()
        
        choice = input_choice1_4()

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
                display.sub_menu_player_choice()

                word_choice = input_enter_choice1_3()

                if word_choice == "1":
                    play_game_option(player_name, level_choice)

                elif word_choice == "2":
                    add_word_option(chosen_level)
                elif word_choice == "3":
                    display.return_first_menu()
                    time.sleep(2)
                    clear_screen()
                    break
                else: 
                    display.invalid_choice_mess_3()

        elif choice == "3":
            time.sleep(2)            
            clear_screen()            
            display_score_table()
            while True:
                return_to_menu = input_return_menu()
                if return_to_menu == "1":
                    time.sleep(2)
                    clear_screen()
                    break
                else:
                    display.invalid_choice_mess_1()
            
        elif choice == "4":
            display.tanks_for_playing()  
            break
            
        else:
            display.invalid_choice_try_again()            

menu()