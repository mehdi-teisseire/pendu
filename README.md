# HANGMAN GAME

Hangman is a classic word-guessing game that can be played by one or more players. The objective is to guess the hidden word before your attempts run out. Here’s a quick guide on how to play:

## Game Setup

Enter the player name : which will be used in the game score tab accessible in the menu
Choose a level difficulty (Harder than hard, Hard, Normal, Easy)
    Harder than harder: 10 to 25  or more characters and 5 errors 
    Hard: 8 to 9 letters and 6 errors 
    Normal: 6 to 7 letters and 8 errors 
    Easy: 4 to 5 letters and  10 errors 

    Choose a Word to add to prelist words : the player write a word that is then added to the level list he already choose.
         (we accept only words with conditions: numbers of letters depends on the level - the word exist in the french dictionnary - also if it is a composed word write it: XXX-XXXX, and the word can't already be in the list)
Acces to the score tab
    Essential Elements:
        Player Name: Display the player's name.
        Current Score: Show the player's current score based on their performance.
        Scores = xxx
            HARDER: level 1 won = +5 level 1 lost = -1
            HARD: level 2 won = +4 level 2 lost = -1
            NORMAL: level 3 won = +3 level 3 lost = -1
            EASY: level 4 won = +2 level 4 lost = -1

And start the game.

## How to Play:

At the beginning it is shown the underscore line one underscore for one letter.
For example, if the word is "apple," it would look like this: _ _ _ _ _.
Guess a Letter: The player take turns guessing one letter at a time.
Add a count down for the number of errors left

Check the Guess:
If the guessed letter is in the word, the programm fills in the dashes with that letter in the correct positions. 
For example, if they guess "p," it updates to _ p p _ _.
If the letter is not in the word, the program adds a part to the hangman figure (head, body, arms, legs).
Continue Guessing: The player continue to guess letters until they either:
Reveal the entire word (win).
Use up all their allowed incorrect guesses/errors (lose).

## Winning the Game

The game is won if the players guess the word before the hangman is fully drawn.
The game is lost if the hangman is completed before the word is guessed.

## Tips

Think of common letters and letter combinations.
Consider the length of the word and any revealed letters to make educated guesses.

Enjoy playing Hangman!

