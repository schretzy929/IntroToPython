'''
Project 2: Rockymon
Author: Scott Schretzenmaier
Date Created: 2/25/15
Date Edited: 3/4/15

Program Description:
1. Ask the user for a name
2. Greets the user by given name
3. Displays a message introducing the user to the program creator and a description of game instructions
4. On enter the user rolls the dice
5. Program determines if the user has rolled winning or losing conditions
6. If neither the user rolls until they roll their match number or a 5
7. Allows user to play again or quit
'''
import random
import sys

username = input ("Welcome to Rockymon, Please input your name.")

#introduction
print("Hello " + username + " my name is Scott Schretzenmaier and and you are about to play Rockymon. This is a dice \n"
                                "game in which you will roll two virtual dice. On the initial roll if you a 5 or 10 you win! \n"
                                "However if you roll a 2, 4 or 11 you lose. If you roll none of these than the number you have rolled\n"
                                "becomes the match number. You will then continue to roll the two dice until you either roll the match\n"
                                "number and win or roll a 5 and lose. Good luck.")

playAgain = 'y'

while (playAgain == 'y'):
    #stores game player name
    #promt the user to roll
    input("New Game: Hit enter to roll the dice.")
    #big start roll
    roll = random.randint(0, 12)

    #display big start roll
    print("Your opening roll is the " + str(roll))

    #determin if user has won off of big start roll
    if(roll == 5 or roll == 10):
        print("You win!")
    elif(roll == 2 or roll == 4 or roll == 11):
        print("You lose!")
    else:
        print("Your big start roll is " + str(roll) + " in order to win you need to roll this match number again before you roll a 5")

        #store match number
        matchNumber = roll
        #Promt user to roll again
        input("Hit enter to roll again.")
        roll = random.randint(0,12)

        #Reroll until a 5 or the match number is rolled
        while (roll != matchNumber and roll != 5):
            input("You rolled a " + str(roll) + " please hit enter to roll again.")
            roll = random.randint(0,12)

        #determine if the user has won or lost
        if(roll == 5 ):
            print("You rolled a 5 you lose!")
        else:
            print("You rolled your match number " + str(matchNumber) + " you win!")

    #Prompt the user to play again
    playAgain = input("Enter 'y' in order to play again or any other key to quit")