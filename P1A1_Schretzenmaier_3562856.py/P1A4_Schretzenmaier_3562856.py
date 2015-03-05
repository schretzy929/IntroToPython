'''
 Author: Scott Schretzenmaier
 Project 1: Budget calculator
 Assignment 4: Get the user's input for a bunch of variables that will be used later on
'''
import sys

#Prompt user for their name, store it in variable
userName = raw_input('Please enter your name: ')

#Welcome Message
print 'Welcome ' + userName + '! My name is Scott Schretzenmaier and this is the budget calculator ' + \
      ' and it will be used to calculate your budget given your input.'

#Person's hourly rate
hourlyRate = float(raw_input('What is your hourly rate?: '))
hourlyRate = round(hourlyRate, 2)
print 'hourlyRate', hourlyRate, type(hourlyRate)

#Overtiem rate
overtimeRate = float(raw_input('What is your overtime rate?: '))
overtimeRate = round(overtimeRate, 2)
print 'overtimeRate', overtimeRate, type(overtimeRate)

#regular hours worked
hoursWorked = float(raw_input('How many hours have you worked?: '))
hoursWorked = round(hoursWorked, 2)
print 'hoursWorked', hoursWorked, type(hoursWorked)

#overtime hours worked
overtimeWorked = float(raw_input('How many overtime hours have you worked?: '))
overtimeWorked = round(overtimeWorked, 2)
print 'overtimeWorked', overtimeWorked, type(overtimeWorked)

#rent
rent = float(raw_input('How much is your rent payment?: '))
rent = round(rent, 2)
print 'rent', rent, type(rent)

# %  pay toward electric bill
electric = float(raw_input('What percent of your paycheck goes to your electric bill?: '))
hourlyRate = round(hourlyRate, 2)
print 'electric', electric, type(electric)

# % pay toward sewer bll
sewer = float(raw_input('What percent of your paycheck goes to your sewer bill?: '))
sewer = round(sewer, 2)
print 'sewer', sewer, type(sewer)

# % pay toward gas bill
gas = float(raw_input('What percent of your paycheck goes to your gas bill?: '))
gas = round(gas, 2)
print 'gas', gas, type(gas)

# food budget
foodBudget = float(raw_input('What is your food budget?: '))
foodBudget = round(foodBudget, 2)
print 'foodBudget', foodBudget, type(foodBudget)

# entertainment budget
entertainmentBudget = float(raw_input('What is your entertainment budget?: '))
entertainmentBudget = round(entertainmentBudget, 2)
print 'entertainmentBudget', entertainmentBudget, type(entertainmentBudget)

#budget for a car expenses for the month
carExpense = float(raw_input('What is your car expense per month?: '))
carExpense = round(carExpense, 2)
print 'carExpense', carExpense, type(carExpense)

sys.exit()