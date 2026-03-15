# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple Hangman game in Python using strings, loops, conditionals, and user input. In this assignment, you will practice managing game state and guiding a player through repeated turns.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Use the starter code to choose a secret word and initialize the variables needed to run the game.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Create variables to track guessed letters, incorrect guesses, and the maximum number of incorrect attempts.
- Prepare the game so it can display the hidden word as letters and underscores.


### 🛠️	Build the Main Game Loop

#### Description
Write the main gameplay loop so the player can guess letters until they either reveal the full word or run out of attempts.

#### Requirements
Completed program should:

- Prompt the player to enter one letter at a time.
- Show the current progress of the secret word using underscores for letters that have not been guessed yet.
- Update the game state after each guess and reduce the remaining attempts for incorrect guesses.
- End the game with a clear win message if the word is guessed.
- End the game with a clear lose message if the player uses all allowed incorrect guesses.
