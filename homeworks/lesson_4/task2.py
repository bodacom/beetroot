# The valid phone number program.

# Make a program that checks if a string is in the right format for a phone number. 
# The program should check that the string contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

phone_number = '3806823545'

if len(phone_number) == 10 and phone_number.isdigit():
    print('You have a valid phone number. Do you want to dial the number?')

else:
    print('Sorry, you have an unvalid phone number')
    