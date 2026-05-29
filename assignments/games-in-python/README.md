
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman-style word guessing game with Python. Practice string handling, loops, conditionals, and user input while giving players a fun interactive experience.

## 📝 Tasks

### 🛠️ Game Setup

#### Description
Create a word list with at least 5 different words and choose one word randomly at the start of each game.

#### Requirements
Completed program should:

- Define a list of words to choose from.
- Select one word randomly using `random.choice()`.
- Keep the chosen word hidden from the player.

### 🛠️ Guessing Loop

#### Description
Implement the main game loop that asks the player for letter guesses, updates the displayed progress, and tracks incorrect guesses.

#### Requirements
Completed program should:

- Prompt the player to guess a single letter.
- Reveal correctly guessed letters in the word display (e.g. `h _ n g m a n`).
- Track and display the letters that have already been guessed.
- Deduct an attempt for each wrong guess.
- Prevent repeated guesses from counting as extra attempts.

### 🛠️ Win/Lose Conditions

#### Description
Finish the game with clear success and failure messages once the word is guessed or attempts run out.

#### Requirements
Completed program should:

- End when the player guesses all letters correctly.
- End when the player uses all allowed incorrect guesses.
- Display a win message with the full word if the player succeeds.
- Display a lose message and reveal the correct word if the player fails.
