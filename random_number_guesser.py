import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
while True:
    
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

number_to_guess = random.randint(start,end)
#print(number_to_guess)
attempts = 1

# start guessing
while True:

    guess = input('Guess a number: ')
    
    if guess.isdigit():

        if guess == number_to_guess:
            print(f'You guessed the number in {attempts} ', end='')
        if attempts == 1:
            print('attempt')
        else:
            print('attempts')
        break

    else:
        print('Please enter a valid number.')
    attempts += 1
    