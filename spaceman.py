import random

def load_word():
    # Load a random word from a file for the game. 
    with open('words.txt', 'r') as f:
        words_list = f.readlines()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


'''Pseudo Code:
Use secret word and loop through it so we can check each letter of the word
Return the value of True if the letter the user picks is inside the secret word'''

def is_word_guessed(secret_word, letters_guessed):
    # Check if all letters in the secret word have been guessed. 
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

'''Pseudo Code:
This will display the currently hidden word with underscores or the letter that has been guessed correctly
If the user input's letter is within the hidden word we will display that letter, otherwise we display an underscore'''

def get_guessed_word(secret_word, letters_guessed):
    # Return the current guessed word with underscores for unguessed letters. 
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word

'''Pseudo Code:
Checks to see if the user guessed letter is within the secret word
Returns true if it is, otherwise false'''

def is_guess_in_word(guess, secret_word):
    # Check if the player's guessed letter is in the secret word. 
    return guess in secret_word  # True or False if the guess is in the word


'''Pseudo Code:
Runs the program
Initializes global variables for the game and calls our functions
A list should be used to contain our guessed letters
Error checks so our inputs are only letters
Displays text if our input is valid or invalid
If no more chances are left, the game will end and display the secret word
Or if we guess the word a win message will be displayed'''
def spaceman(secret_word):
    # Main game loop for the Spaceman guessing game. 
    letters_guessed = []
    attempts_left = 7

    # Introduction to the game
    print('Welcome to Spaceman! You need to guess the secret word one letter at a time, similar to how Hangman is played!')
    print('When you guess a letter, the letter will appear on screen. If you guess wrong, you lose an attempt. You have 7 attempts, good luck!')
    print(f'The secret word has {"_ " * len(secret_word)} letters.')

    while attempts_left > 0:


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
