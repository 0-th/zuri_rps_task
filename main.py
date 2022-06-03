from random import choice

options = {"R": "Rock", "P": "Paper", "S": "Scissors"}

print("------Welcome to Rock, Paper, Scissors game------")

while True:
    print("\n'R' for Rock\n'P' for Paper\n'S' for Scissors")

    user_input = input("Input: ").upper()
   
    if user_input not in options:
        print(f"{user_input} is not a valid input")
        continue

    user_choice = options[user_input]

    cpu_choice = options[choice(list(options.keys()))]

    player_choices = {'CPU': cpu_choice, 'Player': user_choice}

    print(f'Player ({player_choices["Player"]}) : CPU ({player_choices["CPU"]})')

    
    def winner_message(winner):
        print(f'{player_choices[winner]} wins!')

    # check user's choice against CPU's
    if player_choices['CPU'] == player_choices['Player']:
        print("Ended in a draw!")
        print(player_choices)
        continue
    elif 'Rock' and 'Paper' in list(player_choices.values()):
        print('Paper folds Rock')
        if player_choices['CPU'] == 'P':
            winner_message('CPU')
            break
        else:
            winner_message('Player')
            break
    elif 'Rock' and 'Scissors' in list(player_choices.values()):
        print('Rock beats Scissors')
        if player_choices['CPU'] == 'R':
            winner_message('CPU')
            break
        else:
            winner_message('Player')
            break
    elif 'Paper' and 'Scissors' in list(player_choices.values()):
        print('Scissors cuts Paper.')
        if player_choices['CPU'] == 'P':
            winner_message('CPU')
            break
        else:
            winner_message('Player')
            break
