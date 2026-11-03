number = int(input('Enter a random number'))
if number % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

print('Enter three different numbers')
number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 >= number2 and number1 >= number3:
    print(number1, ' is the largest')
elif number2 >= number1 and number2 >= number3:
    print(number2, ' is the largest')
elif number3 >= number1 and number3 >= number2:
    print(number3, ' is the largest')
else:
    print('Invalid input')