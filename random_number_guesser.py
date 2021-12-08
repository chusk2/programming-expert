import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
while True:
    
    try:
        start = int(input('Enter the start of the range: '))
        break
    except ValueError:
        print('Please enter a valid number.')
    
while True:

    try:
        end = int(input('Enter the end of the range: '))
        if end >= start:
            break
    except ValueError:
        print('Please enter a valid number.')
        continue
    # the number was integer but was lower than start
    print('Please enter a valid number.')

#number_to_guess = random.randint(start,end)
number_to_guess = 0
#print(number_to_guess)
attempts = 0

# start guessing
while True:

    try:
        attempts += 1
        guess = int(input('Guess a number: '))

    except ValueError:
        print('Please enter a valid number.')
        continue
    
    if guess == number_to_guess:
        print(f'You guessed the number in {attempts} ', end='')
        if attempts == 1:
            print('attempt')
        else:
            print('attempts')
        break

    #### Do not count the last attempt if it was a guess
    