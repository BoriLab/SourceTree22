from random import randint
play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0,2)]

player = "Paper"

if(computer == player):
    print("무승부")