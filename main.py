import random

difficulties = ['very easy', 'easy', 'normal', 'hard']

valid_difficulty = False

difficulty = ''
correct_number = ''
guess_number = 0
maximum_guesses = ''
guess_length = ''

print("""
Welcome to the Mastermind Game!!
Your task is to try and guess the correct number. You are told on guessing how many of your digits are the same
but not the positions they are in.
Difficulties:
    Very Easy: Number length = 3 (you are told where the correct digits are)
    Easy: Number length = 2
    Normal: Number length = 3
    Hard: Number length = 3 (guesses are limited to 7!)""")

# Checks if input difficulty is valid.

while not valid_difficulty:
    difficulty = input('\nDifficulty: ').lower()
    if difficulty in difficulties:
        valid_difficulty = True
    else:
        print('Please try again, that is not a valid difficulty')


# Selects a random number based on the parameters given in difficulty selection.

def random_number_selection(upper_bound):
    random_number = random.randint(1, upper_bound)
    return random_number


# Iterates over the player guess and the correct number, returning the number of matching indexes as the positions
# variable, then formats an output according to its length.

def easy_game():
    def check_easy_guess():
        i = 0
        positions = ''
        while i < guess_length:
            if str(easy_game_guess)[i] == str(correct_number)[i]:
                positions += str(i + 1)
            i += 1
        return positions

    check_easy_guess()
    correct_digit_positions = check_easy_guess()

    length = len(correct_digit_positions)

    if length == 0:
        print('There are not correct digits.')
    elif length == 1:
        print(f'Correct digit location: {correct_digit_positions}')
    elif length == 2:
        print(f'Correct digit location: {correct_digit_positions[0]} and {correct_digit_positions[1]}')
    else:
        return True


# Visual output for the player telling them how many guesses they took and what the correct number was.

def winning_the_game():
    print(f"""
    Well Done! You guessed the number in {guess_number} guesses.
    The correct number was {correct_number}.""")


def losing_the_game():
    print(f"""
    Stop right there! You have exceeded the maximum guess count. The correct number was {correct_number}.""")


# Checks if guess is valid (i.e. suits the guess length and contains no other characters).

def check_guess():
    while True:
        guess = input('Guess: ')
        if len(guess) == guess_length:
            return guess
        print('That is not a valid guess, please try again...')


# Checks the difficulty chosen and sets the parameters for game functions.

if difficulty == 'very easy':
    correct_number = random_number_selection(1000)
    maximum_guesses = 999
    guess_length = 3
if difficulty == 'easy':
    correct_number = random_number_selection(100)
    maximum_guesses = 999
    guess_length = 2
if difficulty == 'normal':
    correct_number = random_number_selection(1000)
    maximum_guesses = 999
    guess_length = 3
if difficulty == 'hard':
    correct_number = random_number_selection(1000)
    maximum_guesses = 7
    guess_length = 3

print(correct_number)


# Sets a result variable to 0 and iterates over both the player's guess and the correct number, returning the
# number of common digits.

def checking_correct_digits():
    i = 0
    result = 0
    normal_mode_guess = check_guess()
    while i <= guess_length - 1:
        value2 = str(normal_mode_guess)[i]
        value1 = str(correct_number)[i]
        i += 1
        if value1 == value2:
            result += 1
    return result


# Checks whether maximum guesses has been exceeded. If not, the common digit variable is printed however if it is,
# either the winning game or losing game function is called.

while guess_number <= maximum_guesses:
    guess_number += 1
    if difficulty == 'very easy':
        easy_game_guess = check_guess()
        easy_game()
        if easy_game():
            winning_the_game()
            break
    else:
        common_digits = checking_correct_digits()
        if common_digits == guess_length:
            winning_the_game()
            break
        elif guess_number > maximum_guesses:
            losing_the_game()
            break
        else:
            print(f"Common digits: {common_digits}.")
            continue
