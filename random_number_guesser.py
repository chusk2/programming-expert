import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
while True:
    ### Possible bug: negative numbers are also integers
    ### but return False when 'negative number'.isidigit()
    start = input('Enter the start of the range: ')
    if start.isdigit():
        start = int(start)
        break
    else:
        print('Please enter a valid number.')
    
while True:

    end = input('Enter the end of the range: ')
    if end.isdigit():
        if int(end) >= start:
            end = int(end)
            break
        else:
            print('Please enter a valid number.')
    
    else:
        print('Please enter a valid number.')

number_to_guess = random.randint(start,end)
attempts = 0

# start guessing
while True:

    guess = input('Guess a number: ')
    if guess.isdigit():
        attempts += 1
        guess = int(guess)
        if guess == number_to_guess:
            if attempts == 1:
                suffix = ''
            elif attempts > 1:
                suffix = 's'
            print(f'You guessed the number in {attempts} attempt{suffix}')              
            break

    else:
        print('Please enter a valid number.')
    