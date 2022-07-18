# a program that calculates the minimum number of coins required to give a user change.
# Working with US currency, so Quarters = 25c, Dimes = 10c, Nickles = 5c, and Pennies = 1c

# Prompt the user to input the amount of change owed, which must be greater than zero
# If the user keys in an input that is <= 0, then the user will be re-prompted until a vild input is received
# Then the system will calculate the number of quarters, dimes, nickles and pennies that makes up the change owed

from cs50 import get_float

while True:
    # Use "get_float" because its likely that the user will input an amount with decimals
    cents = get_float("Change: ")
    if cents > 0:
        break

# Workings:
# if cents = 1.89
# then cents = round(1.89 * 100) = 189
cents = round(cents * 100)

count = 0

# Number of Quarters calculation:
while cents >= 25:
    cents = cents - 25
    count += 1

# Number of Dimes calculation:
while cents >= 10:
    cents = cents - 10
    count += 1

# Number of Nickels calculation:
while cents >= 5:
    cents = cents - 5
    count += 1

# Number of Pennies calculation:
while cents >= 1:
    cents = cents - 1
    count += 1

print("Total coins: ", count)