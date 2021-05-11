from random import randint
play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0,2)]

player = "Paper"


print('player {}'.format(player))


if player == computer:
    print("tie")