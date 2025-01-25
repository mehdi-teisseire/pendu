import os
import random
import enchant
from inputs import *
import display

# Validation criteria for different difficulty levels
validation_criteria = {
    'très dur': {'min_length': 10, 'max_length': 25, 'file': 'word1.txt'},
    'dur': {'min_length': 8, 'max_length': 9, 'file': 'word2.txt'},
    'normal': {'min_length': 6, 'max_length': 7, 'file': 'word3.txt'},
    'facile': {'min_length': 4, 'max_length': 5, 'file': 'word4.txt'}
}

# To clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# To validate player name
def name_is_valid(player_name):
    return len(player_name) >= 3 and player_name.isalpha()

# To check if a word is already in the specified file
def word_is_in_file(word, filename):
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            words = file.read().splitlines()
            return word in words
    except FileNotFoundError:
        display.file_do_not_exist_error()
        return False

# To validate the player's word
def word_is_valid(player_word, chosen_level):
    criteria = validation_criteria.get(chosen_level)
    
    if not criteria:
        display.invalid_level_mess()
        return False

    word_length = len(player_word)
    
    if word_length < criteria['min_length'] or word_length > criteria['max_length']:
        display.lenght_error_mess(criteria)                
        return False
    
    if " " in player_word or player_word.strip() == "":
        display.no_space_error_mess()
        return False

    if word_is_in_file(player_word, criteria['file']):
        display.word_already_in_collection_mess()
        return False

    if not all(character.isalpha() or character == "-" for character in player_word):
        display.no_space_word_error_mess()
        return False

    french_dict = enchant.Dict("fr_FR")
    if not french_dict.check(player_word):
        display.not_in_french_dictionnary_error_mess()
        return False

    return True

# To validate the guess letter
def validate_guess(guess):

    if not guess:
        display.empty_input_error()
        return False
    
    if guess == " ":
        display.space_input_error()
        return False
    
    if not guess.isalpha():
        display.invalid_character_errors() 
        return False
    
    return True

# the game function 
def play_game(level):

    filename_mapping = {
        "1": ("word1.txt", 5),
        "2": ("word2.txt", 6),
        "3": ("word3.txt", 8),
        "4": ("word4.txt", 10)
    }
    
    filename, errors_remaining = filename_mapping[level]
        
    with open(filename, "r", encoding = "utf-8") as word_file:
        words = [line.strip() for line in word_file.readlines()]
    
    solution = random.choice(words)
    letters_found = ""
    display_word = "_ " * len(solution)
    letters_tried = []
    display.hangman_title()

    while errors_remaining > 0:
        display.word_to_guess(display_word)
        display.number_errors(errors_remaining)
        display.letters_used(letters_tried)
       
        guess = input_enter_your_letter()
        if not validate_guess(guess):
            continue 
        
        while guess in letters_tried or guess in letters_found:
            display.already_used_letter() 
            guess = input_enter_your_letter() 
            if not validate_guess(guess):
                continue 
        
        letters_tried.append(guess)   
        letters_tried = list(set(letters_found) | set(letters_tried))

        if guess in solution:
            letters_found += guess
            display.well_done()
        else:
            errors_remaining -= 1
            display.not_this_time()
            if errors_remaining == 0:
                display.errors_remaining0_graph()
            if errors_remaining <= 1:
                display.errors_remaining1_graph()
            if errors_remaining <= 2:
                display.errors_remaining2_graph()
            if errors_remaining <= 3:
                display.errors_remaining3_graph()
            if errors_remaining <= 4:
                display.errors_remaining4_graph()
            if errors_remaining <= 5:
                display.errors_remaining5_graph()                    
            if errors_remaining <= 6:
                display.errors_remaining6_graph()
            if errors_remaining <= 7:
                display.errors_remaining7_graph()
            if errors_remaining <= 8:
                display.errors_remaining8_graph()
            if errors_remaining <= 9:
                display.errors_remaining9_graph()
            if errors_remaining <= 10:
                display.errors_remaining10_graph()           

        display_word = ""
        for current_character in solution:
            if current_character in letters_found:
                display_word += current_character + " "
            elif current_character == "-":
                display_word += "- "
            else:
                display_word += "_ "

        if "_" not in display_word:
            display.won_mess(solution)
            return True
    
    if errors_remaining == 0:
        display.lose_mess(solution)
        return False