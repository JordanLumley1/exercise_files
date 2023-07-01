# PIN protect on PIN entry

# imports the use of function getpass which hides the value of user input.
import getpass

# setting the variable for the PIN code and change to a string so it can relate to the user input.
correct_pin = str(1234)

# setting the value for the ammount of attempts.
attempts = 5

# welcome message
print('Welcome to JL bank')

# variable for user input of Y or N for pin protection.
pin_protection = input('Would you like to shield your PIN? Y/N : ')

if pin_protection == 'Y':
    while attempts >= 1:
        user_input = getpass.getpass('Please enter PIN: ')
        if user_input == correct_pin:
            print('Correct pin. Your balance is £1000.00')
            break
        else:
            attempts -= 1
            print('Pin incorrect. You have', attempts, 'attempts remaining.')
    else:
        print('Card retained. Please contact bank.')
else:
    while attempts >= 1:
        user_input = input('Please enter PIN: ')
        if user_input == correct_pin:
            print('Correct pin. Your balance is £1000.00')
            break
        else:
            attempts -= 1
            print('Pin incorrect. You have', attempts, 'attempts remaining.')
    else:
        print('Card retained. Please contact bank.')
