x = 5
if (type(x) is int):
    print('True')
else:
    print('false')

x = 5.5

if (type(x) is not float):
    print('true')
else:
    print('false')

x = 20

y = 20

if (x is y):
    print('x & y same identity')

y = 30

if (x is not y):
    print('x & y have different identity')



a = 10

b = -10

print('a >> 1 =', a >> 1)

print('b >> 1 =', b >> 1)

a = 5

b = -10

print('a << 1 =', a << 1)

print('b << 1 =', b << 1)

#Activity 3

print('Enter Marks Obtained in 5 subjects:')

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1 + mark2 + mark3 + mark4 + mark5
avg = int(tot / 5)

validrange = range(0, 101)

if avg not in validrange:
    print('invalid input!')
elif avg in range(91, 101):
    print('Your grade is A1')
elif avg in range(81, 91):
    print('Your grade is A2')
elif avg in range(71, 81):
    print('Your grade is B1')
elif avg in range(61, 71):
    print('Your grade is B2')
