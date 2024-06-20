import random
import numpy as np

#q learning for rock paper scissors

playerMoves = ['rock', 'paper', 'scissors']
aiMoves = ['rock', 'paper', 'scissors']

q_table = {}

for pmove in playerMoves:
    for amove in aiMoves:
        q_table[(pmove, amove)] = 0

def get_reward(player, ai):
    if player == ai:
        return 0
    if player == 'rock':
        if ai == 'scissors':
            return 1
        return -1
    if player == 'paper':
        if ai == 'rock':
            return 1
        return -1
    if player == 'scissors':
        if ai == 'paper':
            return 1
        return -1
    
move = random.choice(aiMoves)
player = random.choice(playerMoves)

for i in range(1000):
    reward = get_reward(player, move)
    newPmove = random.choice(playerMoves) 
    q_table[(move, player)] = q_table[(move, player)] + 0.5 * (reward + 0.9 * np.max(q_table[(player, newPmove)]) - q_table[(move, player)])

    move = player
    player = newPmove

print(q_table)

#play using best move reward based

while True:
    player = input('Enter your move: ')
    #select the best move based on the reward

    options = []

    for i in q_table:
        print(i)
        if i[0] == player:
            options.append((i[1], q_table[i]))

    move = max(options, key=lambda x: x[1])[0] #select the move with the highest reward

    print('AI move: ', move)

