import random

COLORS = ['R', 'G', 'B', 'Y', 'O', 'W']
TOTAL_GUESSES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))

    return code

def enter_code():
    while True:
        guess = list(input('Enter your guess: ').replace(' ', '').upper())

        if len(guess) != CODE_LENGTH:
            print(f'You must enter {CODE_LENGTH} colors.')
            continue

        for guessed_color in guess:
            if guessed_color not in COLORS:
                print(f'You can only choose these colors: {', '.join(COLORS)}.')
                break
        else:
            return guess

def check_code(code, guess):
    correct_color = 0
    correct_position = 0

    for index, guessed_color in enumerate(guess):
        if guessed_color == code[index]:
            correct_position += 1
            code[index] = None

    for guessed_color in guess:
        if guessed_color in code:
            correct_color += 1
            code[code.index(guessed_color)] = None
    
    return {'correct_position': correct_position, 'correct_color': correct_color}

def print_guesses(guesses):
    for round, guess in enumerate(guesses):
        print(f'Round {round + 1}:   | {' '.join(guess[0])} |   Correct position: {guess[1]['correct_position']}, Correct color: {guess[1]['correct_color']}')
        
def game():
    round = 0
    guesses = []
    code = generate_code()

    print('Enter your guess like: R G G B or rggb.')
    print(f'Possible colors are: {', '.join(COLORS)}.')

    while (round < TOTAL_GUESSES):
        guess = enter_code()
        check_guess = check_code(code.copy(), guess)
        guesses.append([guess, check_guess])
        print_guesses(guesses)
        if (check_guess['correct_position'] == 4):
            break
        round += 1
    else:
        print(f'You lost. Code was {', '.join(code)}')
        return
    print('You won!')

# Restart game
def game_loop():
    while True:
        game()
        if input('Play again? (y/n) ').strip().lower() not in ['y', 'yes']:
            break

game_loop()