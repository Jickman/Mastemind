import random

difficulties = ['easy', 'normal', 'hard']

difficulty = ''
correct_number = ''
guess_number = 0

print("""
Welcome to the Mastermind Game!!
Your task is to try and guess the correct number. You are told on guessing how many of your digits are the same
but not the positions they are in.
Difficulties:
    Easy: Number length = 2
    Normal: Number length = 3
    Hard: Number length = 3 (guesses are limited to 7!)""")

while not valid_difficulty:
    valid_difficulty = False
    
    difficulty = input('Difficulty: ')
    if difficulty in difficulties:
        valid_difficulty = True
    else:
        print('Please try again, that is not a valid difficulty')


def random_number_selection(upper_bound):
    random_number = random.randint(1, upper_bound)
    return random_number


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


def check_guess():
    correct_guess = False

    while not correct_guess:
        guess = input('Guess: ')
        if len(guess) == guess_length:
            correct_guess = True
        else:
            print('That is not a valid guess, please try again...')
    return guess


def winning_the_game():
    print("""
    Well Done! You guessed the number in {} guesses.
    The correct number was {}.""".format(guess_number, correct_number))


def losing_the_game():
    print("""
    Stop right there! You have exceeded the maximum guess count. The correct number was {}.""".format(correct_number))


def checking_correct_digits():
    i = 0
    result = 0
    guess = check_guess()
    while i <= guess_length - 1:
        value2 = str(guess)[i]
        value1 = str(correct_number)[i]
        i += 1
        if value1 == value2:
            result += 1
    return result


while guess_number <= maximum_guesses:
    guess_number += 1
    correct_digits = checking_correct_digits()
    if correct_digits == guess_length:
        winning_the_game()
        break
    elif guess_number > maximum_guesses:
        losing_the_game()
        break
    else:
        print("Common digits: {}.".format(correct_digits))
        continue
