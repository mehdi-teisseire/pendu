
# Menu inputs
def input_register_or_guest():
    return input("Souhaitez-vous vous enregistrer et participer au classement (1)\nou jouer en tant qu'invité (2) ? : ").strip()

def input_registered_before():
    return input("Vous êtes-vous déja enrregistré auparavant ? (oui/non) : ").strip().lower()

def input_enter_name():
    return input("Entrez votre nom : ")

def input_try_register_again_or_no():
    return input("Nom non trouvé.\nVoulez-vous essayer à nouveau (1)\nou vous enregistrer avec un nouveau nom (2) ? : ").strip()

def input_enter_choice1_4():
    return input("Entrez votre choix (1-4) : ")

def input_play_again_or_menu():
    return input("Voulez-vous refaire une partie ?\n (1 pour oui, 2 pour retourner au menu) : ")

def input_player_word_rules(validation_criteria, chosen_level):
    return input(f"\nVeuillez entrer votre mot (entre {validation_criteria[chosen_level]['min_length']} et {validation_criteria[chosen_level]['max_length']} lettres).\nPour les mots composés, utilisez le format : XXX-XXXX\nVotre mot : ").lower()

def input_choice1_4():
    return input("\nEntrez votre choix (1-4): ")

def input_enter_choice1_3():
    return input("\nVeuillez entrer votre choix (1-3) : ")

def input_return_menu():
    return input("\nPour retourner au menu, entrez (1) : ")

# rules inputs

def input_enter_your_letter():
    return input("Proposez une lettre : ")[0:1].lower()


