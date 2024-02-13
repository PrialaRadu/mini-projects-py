# A simple Rock Paper Scissors Game where the user plays against the computer


import random


# Retrieves and validates user's input on number of games
def get_user_games():
    user_games = 0
    try:
        user_games = int(input("How many games do you want to play? "))
        if user_games < 1:
            raise ValueError('Type an integer greater than 0! ')
    except ValueError:
        print('Type a valid integer! ')
    return user_games


def rock_paper_scissors(games):
    user_wins = computer_wins = 0
    while games:
        # Retrieves user's choice
        user_choice = input("Enter your choice ('R' for Rock, 'P' for Paper, 'S' for Scissors): ")
        while user_choice not in ['R', 'P', 'S']:
            user_choice = input('Invalid choice, type a valid character (P, R or S): ')

        # Retrieves computer's choice
        computer_choice = random.choice(['R', 'P', 'S'])
        print(f'The computer chose: {computer_choice}')

        # Conditions where the user wins
        if (user_choice, computer_choice) in [('R', 'P'), ('P', 'S'), ('S', 'R')]:
            computer_wins += 1
        # Conditions where the computer wins
        elif (user_choice, computer_choice) in [('P', 'R'), ('S', 'P'), ('R', 'S')]:
            user_wins += 1
        # The rest conditions result in a tie
        else:
            print('Tie!')

        print(f'User score: {user_wins}, Computer score: {computer_wins}\n')
        games -= 1


rock_paper_scissors(get_user_games())
