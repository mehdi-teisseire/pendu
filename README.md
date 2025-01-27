# HANGMAN GAME
Hangman is a classic word-guessing game that can be played by one or more players. The objective is to guess the hidden word before your attempts run out. Here’s a quick guide on how to play:

## Game Setup

Enter the player name : which will be used in the game score tab accessible in the menu
Choose a level difficulty (Harder than hard, Hard, Normal, Easy)
    Harder than harder: 11 or more characters in 15 attemps or/and 5 errors ?
    Hard: 9 letters in 16 attemps or/and 6 errors ?
    Normal: 7 letters in 18 attemps or/and 8 errors ?
    Easy: 5 letters in 20 attemps or/and  10 errors ?

    Choose a Word to add to prelist words : the player write a word that is then added to the level list he already choose.
         (can we accept only words with conditions 5 letters for the easy mode, 7 for the Normal, 9 for the Hard, 11 and more for Harder than harder - also if it is a composed word write it this format: XXX-XXXX)
            check for characters accepted only letters and -
                - is the only symbol accepted ( - will replace _ in the word when shown)
            check if the word is a real word - PyEnchant (come with a fr_FR dictionnary)
            check if the word is already in the list
            error messages : 
                list of all the things that can happen 
                    "this word is already in the list"
                    "this word is not a real word"
                    "this word has non accepted characters"
        loop to ask the player again
    Or he can choose a random word from the list.
Acces to the score tab
    Essential Elements for the Score Tab
        Player Name: Display the player's name.
        Current Score: Show the player's current score based on their performance. (how to calculate it ????)
        Games Played: Track the total number of games played.
        Games Won: Display the number of games won.
        Games Lost: Show the number of games lost.
        Win Rate: Calculate and display the percentage of wins.
Than Button Start the game
And Button to quit ?

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
 
### Coding steps

 #### Word.txt
 #### Word.py
    Opening the file:
        to append a: input user word should be appended at the end of the file
        to read r: to choose and display a random file in the game.

## Winning the Game

The game is won if the players guess the word before the hangman is fully drawn.
The game is lost if the hangman is completed before the word is guessed.

## Tips

Think of common letters and letter combinations.
Consider the length of the word and any revealed letters to make educated guesses.

Enjoy playing Hangman!

