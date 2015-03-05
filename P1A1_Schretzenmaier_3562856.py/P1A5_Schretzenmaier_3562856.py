'''
Author: Scott Schretzenmaier
Date Created: 1/20/15
Date Last Edit: 2/4/15
Python ssVersion: 2.7
Project 1: Budget Calculator
Assignment 5: Prompt the user for their name, insert it into the welcome message. Then collect budget info from
the user and use it to calculate the users budget / net income

'''

import sys

#msg: Input prompt message
#varName: The current variables name
#Prints: Variable name, Variable value, Variable Type
#return: input as float rounded to second decimal
def getBudgetInput(msg, varName):
    budget = round(float(raw_input(msg)), 2)
    print 'Variable Name: ' + varName + ', Variable Value: ' + str(budget) + ', Variable Type: ', type(budget), '\n'
    return budget

#msg: Input prompt message
#varName: The current variables name
#Prints: Variable name, Variable value, Variable Type
#return: input as float rounded to second decimal
def getBudgetPercentInput(msg, totalPay, varName):
    percentBudget = float(raw_input(msg)) / 100
    budget = round( (totalPay * percentBudget), 2)

    print 'Variable Name: ' + varName + ', Variable Value: ' + str(budget) + ', Variable Type: ', type(budget), '\n'
    return budget


#Prompt user for their name, store it in variable
userName = raw_input('Please enter your name: ')

#Welcome Message
print 'Welcome ' + userName + '! My name is Scott Schretzenmaier and this is the budget calculator ' + \
      ' and it will be used to calculate your budget given your input.\n'

#Person's hourly rate
hourlyRate = getBudgetInput('What is your hourly rate?: ', 'hourlyRate')

#Overtiem rate
overtimeRate = getBudgetInput('What is your overtime rate?: ', 'overtimeRate')

#regular hours worked
hoursWorked = getBudgetInput('How many hours have you worked?: ', 'hoursWorked')

#overtime hours worked
overtimeWorked = getBudgetInput('How many overtime hours have you worked?: ', 'overtimeWorked')

#calculate gross pay
grossPay = (hoursWorked * hourlyRate) + (overtimeWorked * overtimeRate)

#rent
rent = getBudgetInput('How much is your rent payment?: ', 'rent')

# %  pay toward electric bill
electric = getBudgetPercentInput('What percent of your paycheck goes to your electric bill?: ', grossPay, 'electric')

# % pay toward sewer bll
sewer = getBudgetPercentInput('What percent of your paycheck goes to your sewer bill?: ', grossPay, 'sewer')

# % pay toward gas bill
gas = getBudgetPercentInput('What percent of your paycheck goes to your gas bill?: ', grossPay, 'gas')

# food budget
foodBudget = getBudgetInput('What is your food budget?: ', 'foodBudget')

# entertainment budget
entertainmentBudget = getBudgetInput('What is your entertainment budget?: ', 'entertainmentBudget')

#budget for a car expenses for the month
carExpense = getBudgetInput('What is your car expense per month?: ', 'carExpense')

#person's monthly expenses - list each one (electric, water, sewer, gas, food, entertainment, and car expenses)
print userName + ' your monthly expenses are: ' \
    '\nElectric = $' + format(electric, '.2f') + \
    '\nWater = $' + format(sewer, '.2f') + \
    '\nGas = $' + format(gas, '.2f') + \
    '\nFood = $' + format(foodBudget, '.2f') + \
    '\nEntertainment = $' + format(entertainmentBudget, '.2f') + \
    '\nMonthly Car Expense = $' + format(carExpense, '.2f')

#sum all monthly expenses together (called "deductions")
deductions = electric + sewer + gas + foodBudget + entertainmentBudget + carExpense
print 'Your total deductions are $' + format(deductions, '.2f')

#gross pay
print 'Your gross pay is $' + format(grossPay, '.2f')

#net pay (subtract deductions from the gross pay)
netPay = grossPay - deductions
print 'Your net pay is $' + format(netPay, '.2f')


sys.exit()