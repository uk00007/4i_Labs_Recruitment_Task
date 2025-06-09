import numpy as np

results_log = []


def game_time():
    moves = ['Rock', 'Paper', 'Scissor']
    index = np.random.randint(3)
    move_by_computer = moves[index]
    move_by_user = input('What\'s your move ?? ')
    results_log.append(f'What\'s your move ?? : {move_by_user.title()}')

    while move_by_user.title() not in moves:
        move_by_user = input(
            'Invalid move !!!\nTry again\nWhat\'s your move ?? ')
        results_log.append(
            f'Invalid move !!!\nTry again\nWhat\'s your move ?? {move_by_user.title()}')

    user_index = moves.index(move_by_user.title())

    results = ['You won !!', 'Better Luck Next Time !', 'It\'s a tie !!']

    print(f'Move by computer : {move_by_computer}')
    results_log.append(f'Move by computer : {move_by_computer}')

    if index == (user_index+1) % 3:
        print(results[1], "\n")
        results_log.append(f'{results[1]}\n')
        return 0
    elif index == user_index:
        print(results[2], "\n")
        results_log.append(f'{results[2]}\n')
        return 1
    else:
        print(results[0], "\n")
        results_log.append(f'{results[0]}\n')
        return 2


rules = """
RULES:
You get 2 points each time you win,
1 point each time it's a tie &
0 if you lose.
"""
print(rules)
results_log.append(rules)

no_of_games = int(input('How many games do you want to play : '))
results_log.append(f'How many games do you want to play : {no_of_games}')
score = 0
while no_of_games > 0:
    score += game_time()
    no_of_games = no_of_games-1

print(f'Your score is : {score}')
results_log.append(f'Your score is : {score}')

with open("4i Labs/game_results.txt", "w") as f:
    for line in results_log:
        f.write(line + "\n")


print("Results saved to game-results.txt")
