#Problem 1

header1 = """"Welcome to number Deffinition. I am Sebastian Sloan and you \nare 
going to be delighted when my program can tell you if the \nnumber you entered 
is positive, negative or zero!! \nlets get started."""

print(header1)
print("")
warning = """WARNING: An invalid number will cause the program to crash, please \n
      only enter valid numbers"""

print(warning)
print("")
print("")

userNumber = float(input("Please input your number here: "))

print("")
print("")

if(userNumber < 0):
    print("Your number is Negative!!")
elif(userNumber == 0):
    print("Your number is Zero")
else:
    print("Your number is Possitive!")
    
print("")
print("")
print("")
print("")


# Problem 2

header2 = """Welcome to Colorado National Bank. Please enter in a customer total \n
below and we would be happy to help you give back the correct change!!"""

print(header2)

print("")
print("")
print("")
warning = """WARNING: An invalid number will cause the program to crash, please \n
       only enter valid numbers"""
print(warning)
print("")
print("")

customerTotal = round(float(input("Please input the customers total: ")),2)
    
if(customerTotal >= 10000):
    print(""""The drawer does not have sufficient funds to make change, \n
          Transaction has been declined.""")
    
else:
    
    print("Thank you for your input! Here is how you will give back the change:")
    print("")
    print("")
    
    twenties = customerTotal//20
    print(f"{int(twenties)} Twenty-dollar Bills")
    tens = (customerTotal - (twenties * 20))//10
    print(f"{int(tens)} Ten-dollar Bills")
    fives = (customerTotal - (twenties * 20) - (tens * 10))//5
    print(f"{int(fives)} Five-dollar Bills")
    ones = (customerTotal - (twenties * 20) - (tens * 10) - (fives * 5))//1
    print(f"{int(ones)} One-dollar Bills")
    quarters = (customerTotal - (twenties * 20) - (tens * 10) - (fives * 5) - (ones * 1))//.25
    print(f"{int(quarters)} Quarters")
    dimes = (customerTotal - (twenties * 20) - (tens * 10) - (fives * 5) - (ones * 1) - (quarters * .25))//.10
    print(f"{int(dimes)} Dimes")
    nickles = (customerTotal - (twenties * 20) - (tens * 10) - (fives * 5) - (ones * 1) - (quarters * .25) - (dimes * .10))//.05
    print(f"{int(nickles)} Nickles")
    pennies = (customerTotal - (twenties * 20) - (tens * 10) - (fives * 5) - (ones * 1) - (quarters * .25) - (dimes * .10) - (nickles * .05))//.01
    print(f"{int(pennies)} Pennies")

print("")
print("")
print("")
print("")

# Problem 3

#=============================================================================
header3 = """Welcome to the Sentence analaizer! Please type in a sentance \n
Then find out what the sentance contains!"""

print(header3)

print("")
print("")
print("")

userSentance = input("Please type your desired sentance here: \n")

print("")
print("")

import re

if(userSentance.isalpha()):
    print("Contains only letters")
    print("")
elif(userSentance.isupper()):
    print("contains only Upper Case Letters")
    print("")
elif(userSentance.islower()):
    print("Contains only lower case letters")
    print("")
elif(userSentance.isdigit()):
    print("Contains only numbers")
    print("")
elif(userSentance.isalnum()):
    print("Contains only words and numbers")
    print("")
elif(re.search("^[A-Z]", userSentance)):
    print("Starts with an uppercase letter")
    print("")
elif(userSentance.endswith('.')):
    print("Ends With a period")
    print("")
else:
    print("Your sentance is irregular, please re imput sentance.")
    
print("")
print("")
print("")
print("")
#=============================================================================
    
# Problem 4

header4 = """Welcome to Sebastians Tax Calculations!! Here will will take your \n
income and calculate what taxes you owe! Please only put in real numbers. All other \n
inputs will cause a system crash. Thank you."""

print(header4)
print("")
print("")
print("")

customerIncome = round(float(input("Please enter your total income for the year: $")),2)

if(customerIncome <= 50000):
    fiftyOrLess = round(customerIncome * 0.01,2)
    print("")
    print("")
    print(f"The amount of income tax you owe is: ${fiftyOrLess}")
elif(customerIncome <= 75000):
    firstFifty = round(50000 * 0.01,2)
    nextTwentyFive = round((customerIncome - 50000) * .02,2)
    print("")
    print("")
    print(f"The amount of income that you owe is: ${firstFifty + nextTwentyFive}")
elif(customerIncome <= 100000):
    firstFifty = round(50000 * 0.01,2)
    nextTwentyFive = round(25000 * .02,2)
    followingTwentyFive = round((customerIncome - 75000) * .03,2)
    print("")
    print("")
    print(f"The amount of income that you owe is: ${firstFifty + nextTwentyFive + followingTwentyFive}")
elif(customerIncome <= 250000):
    firstFifty = round(50000 * 0.01,2)
    nextTwentyFive = round(25000 * .02,2)
    followingTwentyFive = round(25000 * .03,2)
    nextOneHundredAndFifty = round((customerIncome - 100000) * .04,2)
    print("")
    print("")
    print(f"The amount of income that you owe is: ${firstFifty + nextTwentyFive + followingTwentyFive + nextOneHundredAndFifty}")
elif(customerIncome <= 500000):
    firstFifty = round(50000 * 0.01,2)
    nextTwentyFive = round(25000 * .02,2)
    followingTwentyFive = round(25000 * .03,2)
    nextOneHundredAndFifty = round(150000 * .04,2)
    doubleTrouble = round((customerIncome - 250000) * .05,2)
    print("")
    print("")
    print(f"The amount of income that you owe is: ${firstFifty + nextTwentyFive + followingTwentyFive + nextOneHundredAndFifty + doubleTrouble}")
elif(customerIncome > 500000):
    firstFifty = round(50000 * 0.01,2)
    nextTwentyFive = round(25000 * .02,2)
    followingTwentyFive = round(25000 * .03,2)
    nextOneHundredAndFifty = round(150000 * .04,2)
    doubleTrouble = round(250000 * .05,2)
    iWish = round((customerIncome - 500000) * .06,2)
    print("")
    print("")
    print(f"The amount of income that you owe is: ${firstFifty + nextTwentyFive + followingTwentyFive + nextOneHundredAndFifty + doubleTrouble + iWish}")



    
 