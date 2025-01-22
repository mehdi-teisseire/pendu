import os
import random

# To clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# To validate player name
def name_is_valid(player_name):
    return len(player_name) >= 4 and player_name.isalpha()

# To play the game
def play_game(level):

    filename_mapping = {
        "1": ("word1.txt", 5),
        "2": ("word2.txt", 6),
        "3": ("word3.txt", 8),
        "4": ("word4.txt", 10)
    }
    
    filename, errors_remaining = filename_mapping[level]
        
    with open(filename, "r") as word_file:
        words = [line.strip() for line in word_file.readlines()]
    
    solution = random.choice(words)
    letters_found = ""
    display = "_ " * len(solution)

    print("*** LE JEU DU PENDU ***")
    
    while errors_remaining > 0:
        print("\nLe mot à deviner : ", display)
        print(f"Nombre d'erreurs restant : {errors_remaining}")
        guess = input("Propose une lettre : ")[0:1].lower()

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
                print(" ||       /|\ ")
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