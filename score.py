import os
import display
from inputs import *

# Score rules based on levels
score_rules = {
    "1": {"gagné": 5, "perdu": -1},
    "2": {"gagné": 4, "perdu": -1},
    "3": {"gagné": 3, "perdu": -1},
    "4": {"gagné": 2, "perdu": -1}
}
# To update the score when player already have an account
def update_score(player_name, level, won):
    scores = read_scores()
    if player_name not in scores:
        return  
    if won:
        scores[player_name] += score_rules[level]["gagné"]
    else:
        scores[player_name] += score_rules[level]["perdu"]

    write_scores(scores)

# To read scores from the score file
def read_scores():
    scores = {}
    if os.path.exists('score.txt'):
        with open('score.txt', 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line: 
                    parts = line.split(',')
                    if len(parts) == 2: 
                        name, score = parts
                        scores[name] = int(score)
    return scores

# To write scores back to the score file
def write_scores(scores):
    with open('score.txt', 'w', encoding="utf-8") as file:
        for name, score in scores.items():
            file.write(f"{name},{score}\n")


# To display the score table
def display_score_table():
    scores = read_scores()
    sorted_scores = sorted(scores.items(), key = lambda x: x[1], reverse = True)

    display.score_tab_title()
    display.player_score()
    for name, score in sorted_scores:
        display.for_each_player_name_score(name, score)