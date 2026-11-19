secret_number = 21
print('Guess a number between 1 to 50! You will have 5 lives. I will give a hint everytime you lose. Good luck :)!')
lives = 5
guess = 9
while lives > 0 and guess != secret_number:
    guess = int(input('Guess my number!: '))
    if guess >= 18 and guess <= 20:
        print('HOT!!!')
    elif guess <= 18 and guess >= 10:
        print('Warm!')
    elif guess <= 10:
        print('Cold :(')
    elif guess >= 22 and guess <= 30:
        print('warm')
    elif guess >= 30 and guess <= 40:
        print('Cold!')
    elif guess >= 40 and guess <= 50:
        print('Ice cold :(')
    elif guess <= 0:
        print('Invalid.')
    elif guess == secret_number:
        print('You won!')
        lives = 0
    else:
        print('Invalid please enter a number between 1 - 50')
    lives -= 1