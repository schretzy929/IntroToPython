'''
Project 2: Rockymon
Author: Scott Schretzenmaier
Date Created: 2/25/15
Date Edited: 2/26/15

Program Description:
1. Ask the user for a name
2. Greets the user by given name
3. Displays a message introducing the user to the program creator and a description of game instructions
4. On enter the user rolls the dice
5. Program determines if the user has rolled winning or losing conditions
'''
import random
import sys

#stores game player name
username = input ("Welcome to Rockymon, Please input your name.")

#introduction
print("Hello " + username + " my name is Scott Schretzenmaier and and you are about to play Rockymon. This is a dice \n"
                            "game in which you will roll two virtual dice. On the initial roll if you a 5 or 10 you win! \n"
                            "However if you roll a 2, 4 or 11 you lose. If you roll none of these than the number you have rolled\n"
                            "becomes the match number. You will then continue to roll the two dice until you either roll the match\n"
                            "number and win or roll a 5 and lose. Good luck.")

#big start roll
roll = random.randint(0, 12)

#display big start roll
print("Your opening roll is the " + str(roll))

#determin if user has won off of big start roll
if(roll == 5 or roll == 10):
    print("You win!")
    sys.exit()
elif(roll == 2 or roll == 4 or roll == 11):
    print("You lose!")
    sys.exit()
else:
    print("Your big start roll is " + str(roll) + " in order to win you need to roll this match number again before you roll a 5")



