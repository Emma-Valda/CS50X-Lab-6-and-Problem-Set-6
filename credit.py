from cs50 import get_int


def main():
    # The user is prompted to input their credit card number
    while True:
        credit_card = get_int("Number: ")
        # the program will break out of the while loop if the user enters and valid input
        if credit_card >= 0:
            break

    if check_validity(credit_card):
        print_card_brand(credit_card)
    else:
        print("INVALID")


def check_validity(credit_card_number):
    return checksum(credit_card_number)


def checksum(credit_card_number):
    sum = 0
    # Convert the credit card number into a string
    for i in range(len(str(credit_card_number))):
        if (i % 2 == 0):
            sum += credit_card_number % 10
        else:
            # For example: 2 * 7 = 14
            digit = 2 * (credit_card_number % 10)
            # now the program will take the 14 and break it up into 1 + 4
            sum += digit // 10 + digit % 10

        # the credit_card_number need to be reduced without changing the range(len(str(credit_card_number)))
        credit_card_number //= 10

    return sum % 10 == 0


def print_card_brand(credit_card_number):
    # The credit card number can begin with either 34 or 37
    if (credit_card_number >= 34e13 and credit_card_number < 35e13) or (credit_card_number >= 37e13 and credit_card_number < 38e13):
        print("AMEX")
    # The credit card number can begin with either 51, 52,...,55
    elif (credit_card_number >= 51e14 and credit_card_number < 56e14):
        print("MASTERCARD")
    elif (credit_card_number >= 4e12 and credit_card_number < 5e12) or (credit_card_number >= 4e15 and credit_card_number < 5e15):
        print("VISA")
    else:
        print("INVALID")


# python's way of running the main function
if __name__ == "__main__":
    main()