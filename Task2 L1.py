import re

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)

    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))

    return checksum % 10 

def validate_credit_card(card_number):
    # Remove all non-digit characters from the card number
    card_number = re.sub(r'\D', '', card_number)

    # Check if the card number is valid (must be 13-16 digits)
    if not re.match(r'^\d{13,16}$', card_number):
        return False

    # Check the Luhn algorithm
    if luhn_checksum(card_number) != 0:
        return False

    return True

# Test the function
card_number = input("Enter your credit card number: ")
if validate_credit_card(card_number):
    print( "True")
else:
    print( "False")
