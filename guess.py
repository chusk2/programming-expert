import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
while True:
    start = input('Enter the start of the range: ')
    try:
        start = int(start)
        break
    except ValueError:
        print('Please enter a valid number.')
        continue
    
while True:
    try:
        end = int(input('Enter the end of the range: '))
    except ValueError:
        print('Please enter a valid number.')
        continue
    if end >= start:
        break
    print('Please enter a valid number.')

number_to_guess = random.randint(start,end+1)
attemps = 0
while True:
    
    guess = int(input('Guess a number: '))
    if guess == number_to_guess:
        print(f'You guessed the number in {attemps}')
        break
    attemps += 1