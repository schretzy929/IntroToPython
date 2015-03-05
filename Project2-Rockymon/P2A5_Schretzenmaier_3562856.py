'''
Project 2: Rockymon
Author: Scott Schretzenmaier
Date Created: 2/25/15
Date Edited: 3/4/15

Program Description:
1. Ask the user for a name
2. Greets the user by given name
3. Displays a message introducing the user to the program creator and a description of game instructions
4. Allows the user to choose to play the game or have the game automated
5. On enter the user rolls the dice
6. Program determines if the user has rolled winning or losing conditions
7. If neither the user rolls until they roll their match number or a 5
8. Allows user to play again or quit
'''
import random
import sys
#Function for dice roll, gameType: automatic/manual
def rollDice(gameType):
    if gameType == 1:
        rollDiceManual()
    else:
        rollDiceAutomatic()

#function for manual dice roll
def rollDiceManual():
    input("Hit enter to roll the dice.")
    roll = random.randint(1,12)
    print("You've rolled: " + str(roll))
    return roll

#function for automatic dice roll
def rollDiceAutomatic():
    print("Rolling dice automatically...")
    roll = random.randint(1,12)
    print("You've rolled: " + str(roll))
    return roll

def Rockymon(gameType):
        #promt the user to roll
        print("\nNew Game!")
        #big start roll
        roll = rollDice(gameType)

        #determin if user has won off of big start roll
        if(roll == 5 or roll == 10):
            print("You win!")
        elif(roll == 2 or roll == 4 or roll == 11):
            print("You lose!")
        else:
            print(str(roll) + " is now your match number in order to win you need to roll this match number again before you roll a 5")

            #store match number
            matchNumber = roll

            #Promt user to roll again
            roll = rollDice(gameType)

            #Reroll until a 5 or the match number is rolled
            while (roll != matchNumber and roll != 5):
                roll = rollDice(gameType)

            #determine if the user has won or lost
            if(roll == 5 ):
                print("You lose!")
            else:
                print("You win!")



#Prompt user for their name
username = input ("Welcome to Rockymon, Please input your name.")

#introduction
print("Hello " + username + " my name is Scott Schretzenmaier and and you are about to play Rockymon. This is a dice \n"
                                "game in which you will roll two virtual dice. On the initial roll if you a 5 or 10 you win! \n"
                                "However if you roll a 2, 4 or 11 you lose. If you roll none of these than the number you have rolled\n"
                                "becomes the match number. You will then continue to roll the two dice until you either roll the match\n"
                                "number and win or roll a 5 and lose. Good luck.")

#Promt the user to see if they want to play the game or automate the game
automate = (input("Enter 1 to play the game or 2 to automate the game."))
while(automate != 1 and automate != 2 and automate != "1" and automate != "2"):
    automate = input("Please enter a 1 or a 2")
automate = int(automate)

if(automate == 1):
    #variable that allows user to replay
    playAgain = 'y'
    while (playAgain == 'y'):
        Rockymon(automate)
        #Prompt the user to play again
        playAgain = input("Enter 'y' in order to play again or any other key to quit")
else:
    numberOfGamePlays = int(input("How many times would you like the game to automate?"))
    for count in range(numberOfGamePlays):
        Rockymon(automate)


sys.exit()