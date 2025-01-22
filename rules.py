import os
import random
import enchant

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
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            return word in words
    except FileNotFoundError:
        print(f"Erreur: Le fichier {filename} n'existe pas.")
        return False

# To validate the player's word
def word_is_valid(player_word, level):
    criteria = validation_criteria.get(level)
    
    if not criteria:
        print("Erreur : un niveau non valide à été entré.")
        return False

    word_length = len(player_word)
    
    if word_length < criteria['min_length'] or word_length > criteria['max_length']:        
        print(f"Erreur: le mot doit faire entre {criteria['min_length']} \net {criteria['max_length']} lettres, incluant les trait d'unions.")        
        return False
    
    if " " in player_word or player_word.strip() == "":
        print("Erreur: le mot ne doit pas contenir d'espaces ni être vide.")
        return False

    if word_is_in_file(player_word, criteria['file']):
        print("Erreur: Le mot est déja dans la collection.")
        return False

    if not all(character.isalpha() or character == "-" for character in player_word):
        print("Erreur: le mot ne doit contenir que des lettres ou des traits d'union.")
        return False

    french_dict = enchant.Dict("fr_FR")
    if not french_dict.check(player_word):
        print("Erreur: ce mot n'a pas été trouvé dans le dictionnaire français.")
        return False

    return True

# To play the game
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
    display = "_ " * len(solution)
    letters_tried = []
    print("*** LE JEU DU PENDU ***")
    
    while errors_remaining > 0:
        print("\nLe mot à deviner : ", display)
        print(f"Nombre d'erreurs restant : {errors_remaining}")
        print("Les lettres déja utilisées :\n" + str(letters_tried))
        guess = input("Propose une lettre : ")[0:1].lower()
        while guess in letters_tried or guess in letters_found:
            print("Cette lettre a déjà été utilisée. Veuillez en proposer une autre.") 
            guess = input("Propose une lettre : ")[0:1].lower()       
        letters_tried.append(guess)   
        letters_tried = list(set(letters_found) | set(letters_tried))

        if guess in solution:
            letters_found += guess
            print("Bien joué!")
        else:
            errors_remaining -= 1
            print("Pas cette fois, essaie encore !\n")
            if errors_remaining == 0:
                print(" ==========Y= ")
            if errors_remaining <= 1:
                print(" ||/       |  ")
            if errors_remaining <= 2:
                print(" ||        0  ")
            if errors_remaining <= 3:
                print(r" ||       /|\ ")
            if errors_remaining <= 4:
                print(" ||       /|  ")
            if errors_remaining <= 5:                    
                print("==============")
            if errors_remaining <= 6:
                print("||  ||  ||  ||")
            if errors_remaining <= 7:
                print("==============")
            if errors_remaining <= 8:
                print("||  ||  ||  ||")
            if errors_remaining <= 9:
                print("==============")
            if errors_remaining <= 10:
                print("||  ||  ||  ||")            

        display = ""
        for current_character in solution:
            if current_character in letters_found:
                display += current_character + " "
            else:
                display += "_ "

        if "_" not in display:
            print(f"\n *** Vous avez gagné ! Le mot était : {solution} *** ")
            break
    
    if errors_remaining == 0:
        print(f"\nVous avez perdu ! : Le mot était : {solution}")