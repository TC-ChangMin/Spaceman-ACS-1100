import random
import os

def load_word():
    # Load a random word from a file for the game. 
    with open('words.txt', 'r') as f:
        words_list = f.readlines()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

# def clear_terminal():
#     # Clear the terminal screen for a fresh game state display. 
#     if os.name == 'nt':  # For Windows
#         os.system('cls')
#     else:  # For Linux and MacOS
#         os.system('clear')

def is_word_guessed(secret_word, letters_guessed):
    # Check if all letters in the secret word have been guessed. 
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    # Return the current guessed word with underscores for unguessed letters. 
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word

def is_guess_in_word(guess, secret_word):
    # Check if the player's guessed letter is in the secret word. 
    return guess in secret_word  # True or False if the guess is in the word

def spaceman(secret_word):
    # Main game loop for the Spaceman guessing game. 
    letters_guessed = []
    attempts_left = 7
    # first_iteration = True  # Flag for the first game iteration

    # Introduction to the game
    print('Welcome to Spaceman! You need to guess the secret word one letter at a time, similar to how Hangman is played!')
    print('When you guess a letter, the letter will appear on screen. If you guess wrong, you lose an attempt. You have 7 attempts, good luck!')
    print(f'The secret word has {"_ " * len(secret_word)} letters.')

    while attempts_left > 0:
        # if not first_iteration:
        #     clear_terminal()  # Clear the terminal after the first guess

        # Display current game status
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        print(f"Word so far: {guessed_word}")
        print(f"Letters guessed so far: {', '.join(letters_guessed)}")
        print(f"Attempts left: {attempts_left}\n")

        # Get a valid guess from the player
        guess = input("Please guess a single letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        if guess in letters_guessed:
            print("You've already guessed that letter. Try again.")
            continue

        # Process the guess and update game state
        letters_guessed.append(guess)
        if is_guess_in_word(guess, secret_word):
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Wrong guess. You have {attempts_left} attempts left.")

        # Check if the player has guessed the word
        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        # Set flag to False after the first iteration
        first_iteration = False
    else:
        print(f"Game over! The secret word was: {secret_word}")

# These function calls will start the game
secret_word = load_word()
spaceman(secret_word)
