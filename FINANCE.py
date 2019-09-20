while True:
    try:
        INCOME = int(input("Please enter your Monthly Income to the nearest whole number "))
    except ValueError and NameError:
        print ("I'm Sorry, please input a whole number")
        continue
    else:
        # Successful Input
        break
        # Now for cost of living

while True:
    try:
        RENT = int(input("Please input your Rent / House payment amount per month "))
        CELL = int(input("Please input your monthly cell phone bill amount "))
        FOOD = int(input("Please input your monthly food costs "))
        UTILITIES = int(input("Please input your monthly Utility bill amount "))
        CAR = int(input("Please input your monthly Car payment amount (This includes a car payment and insurance but "
                        "not gas, repairs, etc "))
        GAS = int(input("Please enter the amount you pay per month for Gasoline "))
        OTHER = int(input("Please enter the TOTAL amount of any other bills we may have missed "))
    except ValueError and NameError:
        print ("I'm sorry, please enter a valid amount")
        continue
    else:
        # Successful Inputs
        break

TOTAL_COST = RENT + CELL + FOOD + UTILITIES + CAR + GAS + OTHER
DIFFERENCE = INCOME - TOTAL_COST
print "Your total cost is about " + str(TOTAL_COST)
print "And your Monthly income is about " + str(INCOME)
print "So your left over amount to work with is about " + str(DIFFERENCE)

# Now For Savings goals

while True:
    try:
        SAVINGS = int(input("Please input your TOTAL amount currently in your savings "))
        # GOAL = int(input("Please enter your GOAL savings amount to the nearest whole number"))
        INTEREST = int(input("Please enter your bank's interest amount on your savings (if you don't know, enter "
                             "0 and we'll use the national average APY for savings accounts) "))
        TIME = int(input("How long in months do you want to save for? "))
        PERCENT = int(input("About what percentage of your left over income would you like to put away? (Many people"
                            "recommend about 20% "))
    except ValueError and NameError:
        print ("I'm sorry, please enter a valid number")
        continue
    else:
        # SUCCESS
        break

        # noinspection PyUnreachableCode
        if INTEREST == 0:
            INTEREST = 2
        else:
            INTEREST = INTEREST
            break
        if PERCENT == 0:
            PERCENT = 20
        else:
            PERCENT = PERCENT
            break

DIFFERENCE = DIFFERENCE + SAVINGS

PERCENT = (DIFFERENCE * PERCENT) / 100.0

# Now we want to calculate the user's goal and how long it will take to get there
# Ending formula:
# (Initial amount (already in savings) + (Percentage of leftover income * Goal time)) * Interest

FINAL = (SAVINGS + (PERCENT * TIME)) * INTEREST
print FINAL