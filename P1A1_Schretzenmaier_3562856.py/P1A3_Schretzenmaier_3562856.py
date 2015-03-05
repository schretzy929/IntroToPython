'''
 Author: Scott Schretzenmaier
 Project 1: Budget calculator
 Assignment 3: Prompt user for their name, Insert it into the welcome message
'''

__author__ = 'scottschretzenmaier'

#Prompt user for their name, store it in variable
userName = raw_input('Please enter your name: ')

#Welcome Message
print 'Welcome ' + userName + '! My name is Scott Schretzenmaier and this is the budget calculator ' + \
      ' and it will be used to calculate your budget given your input.'

#Person's hourly rate
hourlyRate = 100
print 'hourlyRate', hourlyRate, type(hourlyRate)

#Overtiem rate
overtimeRate = 150
print 'overtimeRate', overtimeRate, type(overtimeRate)

#regular hours worked
hoursWorked = 10
print 'hoursWorked', hoursWorked, type(hoursWorked)

#overtime hours worked
overtimeWorked = 5
print 'overtimeWorked', overtimeWorked, type(overtimeWorked)

#rent
rent = 500
print 'rent', rent, type(rent)

# %  pay toward electric bill
electric = 10
print 'electric', electric, type(electric)

# % pay toward sewer bll
sewer = 5
print 'sewer', sewer, type(sewer)

# % pay toward gas bill
gas = 5
print 'gas', gas, type(gas)

# food budget
foodBudget = 500
print 'foodBudget', foodBudget, type(foodBudget)

# entertainment budget
entertainmentBudget = 500
print 'entertainmentBudget', entertainmentBudget, type(entertainmentBudget)

#budget for a car expenses for the month
carExpense = 100
print 'carExpense', carExpense, type(carExpense)