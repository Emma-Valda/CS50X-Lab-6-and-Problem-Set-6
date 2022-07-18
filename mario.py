# The user will be prompted to key in a positive integer between 1 and 8 inclusive, which will be the height of the pyramid
# If the user inputs an incorrect input, they will be reprompted to input another integer until a valid integer is received
# Then the pyramid will the printed

from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

# The shape of the pyramid will be printed out using hashes
# "end=""" specifies that nothing should be printed at the end of the string
for i in range(n):
    print(" " * (n - 1 - i), end="")
    print("#" * (i + 1), end="")
    print(" " * 2, end="")
    print("#" * (i + 1))
