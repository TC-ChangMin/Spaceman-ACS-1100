import random

def instructions():
    print('Welcome to Spaceman! This is a hangman-like game where a user can guess one letter at a time to try and figure out the secret word.')
    print('You have 7 attempts to guess. Good Luck!')

def load_word():
    with open('test.txt', 'r') as f:
        words_list = f.readlines()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def find_matched_letters(secret, guess):
    matched_letters = []
    for letter in guess:
        if letter in secret:
            matched_letters.append(letter)
    return matched_letters

def update_matching_letters(secret, guess, previous_matching_letters):
    matching_letters = list(previous_matching_letters)
    for i in range(len(secret)):
        if secret[i] == guess:
            matching_letters[i] = guess
    return ''.join(matching_letters)

def spaceman():
    secret = load_word()
    matching_letters = ['_'] * len(secret)
    attempts = 7
    word_length = "_" * len(secret)

    instructions()
    print(f"Your current word is {word_length}")
    while attempts > 0:
        guess = input("Guess a single letter: ").lower()

        # Check if the input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print(f"Please enter a single letter.")
            continue

        if guess in matching_letters or guess in find_matched_letters(secret, matching_letters):
            print("You've already guessed that letter. Try again.")
            continue

        if guess in secret:
            matching_letters = update_matching_letters(secret, guess, matching_letters)
            print(f"Good guess! Current progress: {matching_letters}")
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.\n Remember your current guess is {matching_letters}")

        if '_' not in matching_letters:
            print(f"Congratulations! You guessed the secret word: {secret}")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The secret word was: {secret}")

if __name__ == "__main__":
    spaceman()
