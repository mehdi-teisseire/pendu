import os

# To clear the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# To validate player name
def name_is_valid(player_name):
    return len(player_name) >= 4 and player_name.isalpha()