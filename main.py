import random

difficulties = ['mastermind', 'easy', 'normal', 'hard']

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

    Mastermind: The normal mastermind game (number length = 3, maximum guesses = 20).
    
Non-Mastermind games (you are only prompted if a digit is correct and in the right place).
    Easy: Number length = 2
    Normal: Number length = 3
    Hard: Number length = 3 (guesses are limited to 7!)
    
Type the difficulty you wish to chose below.""")

# Checks if input difficulty is valid.

while not valid_difficulty:
    difficulty = input('\nDifficulty: ').lower()
    if difficulty in difficulties:
        valid_difficulty = True
    else:
        print('Please try again, that is not a valid difficulty.')


# Selects a random number based on the bound parameters given in difficulty selection.

def random_number_selection(lb, ub):
    random_number = random.randint(lb, ub)
    return random_number


# Iterates over the player guess and the correct number, returning the number of matching indexes as the positions
# variable, then formats an output according to its length.

def easy_game():
    def checking_easy_correct_digits():
        correct_digit = 0

        # Works out correct location of digit.

        guess_list = [number1 for number1 in str(easy_game_guess)]
        correct_number_list = [number2 for number2 in str(correct_number)]

        for element in guess_list:
            if element in correct_number_list:
                correct_digit += 1
                correct_number_list.remove(element)
            else:
                continue
        return correct_digit

        # Works out correct digit.

    def checking_easy_correct_location():
        i = 0
        correct_location = 0
        while i < guess_length:
            if str(easy_game_guess)[i] == str(correct_number)[i]:
                correct_location += 1
            i += 1
        return correct_location

    checking_easy_correct_location()
    checking_easy_correct_digits()

    locations_and_digits = checking_easy_correct_location()
    digits = checking_easy_correct_digits() - checking_easy_correct_location()

    if locations_and_digits != guess_length:
        print(f'Correct number, wrong place: {digits} \nCorrect number, right place: {locations_and_digits}')
    else:
        return True


# Checks if guess is valid (i.e. suits the guess length and contains no other characters).

def check_guess():
    while True:
        guess = input('Guess: ')
        if len(guess) == guess_length:
            return guess
        print('That is not a valid guess, please try again...')


# Checks the difficulty chosen and sets the parameters for game functions.

if difficulty == 'mastermind':
    correct_number = random_number_selection(99, 1000)
    maximum_guesses = 20
    guess_length = 3
if difficulty == 'easy':
    correct_number = random_number_selection(9, 100)
    maximum_guesses = 999
    guess_length = 2
if difficulty == 'normal':
    correct_number = random_number_selection(99, 1000)
    maximum_guesses = 999
    guess_length = 3
if difficulty == 'hard':
    correct_number = random_number_selection(99, 1000)
    maximum_guesses = 7
    guess_length = 3

#print(correct_number)


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


# Visual output for the player telling them how many guesses they took and what the correct number was.

def winning_the_game():
    print(f"""
    Well Done! You guessed the number in {guess_number} guesses.
    The correct number was {correct_number}.""")


def losing_the_game():
    print(f"""
    Stop right there! You have exceeded the maximum guess count. The correct number was {correct_number}.""")


# Checks whether maximum guesses has been exceeded. If not, the common digit variable is printed however if it is,
# either the winning game or losing game function is called.

while guess_number <= maximum_guesses:
    guess_number += 1
    if difficulty == 'mastermind':
        easy_game_guess = check_guess()

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

# Appends both name and score to Leaderboard and prints its contents.

if difficulty == 'mastermind':

    name = input("\n\nWhat is your name (else, type 'no')? ")
    if name == 'no':
        print('I see you value your privacy.')
        name = 'unknown'

    with open('Leaderboard.txt', 'a+') as f_append:
        f_append.write(f'\n  {name}      {guess_number}')
    with open('Leaderboard.txt', 'r') as f_read:
        print(f_read.read())
