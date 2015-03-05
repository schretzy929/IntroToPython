'''
Project 2: Rockymon
Author: Scott Schretzenmaier
Date Created: 2/25/15
Date Edited: 2/25/15

Program Description:
1. Ask the user for a name
2. Greets the user by given name
3. Displays a message introducing the user to the program creator and a description of game instructions
'''

#stores game player name
username = input ("Welcome to Rockymon, Please input your name.")

#introduction
print("Hello " + username + " my name is Scott Schretzenmaier and and you are about to play Rockymon. This is a dice "
                            "game in which you will roll two virtual dice. On the initial roll if you a 5 or 10 you win!"
                            "However if you roll a 2, 4 or 11 you lose. If you roll none of these than the number you have rolled"
                            "becomes the match number. You will then continue to roll the two dice until you either roll the match"
                            "number and win or roll a 5 and lose. Good luck.")

