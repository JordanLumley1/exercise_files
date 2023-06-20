# Simple PIN entry

# setting the value for the correct pin.
correct_pin = str(1234)

# setting the ammount of attempts.
attempts = 3

# welcome message
print('Welcome to JL bank')

# setting a loop that only lets the user continue if the ammount of attempts left is above or equal to 1.
# if pin entered is correct, balance is displayed.
# if incorrect the loop re starts until attempts is 0.
# when attemps reach zero prints a message.

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
