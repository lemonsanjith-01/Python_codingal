v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y
print('value of v+w * x / y is ', z)

name = 'Alex'
age = 0

if (name == 'Alex' or name == 'John') and age >= 2:
    print('Hello! welcome')
else:
    print('Good bye!')

#actvity 2

print('Enter a Number (Numerator):')
numn = int(input())
print('Enter a number (denominator)')
numd = int(input())

if numn%numd==0:
    print('\n' + str(numn)+ ' is divisible by ' +str(numd))
else:
    print('\n' + str(numn)+ ' is divisible by ' + str(numd))

#activity 4

a = int(input('enter a value:'))
b = int(input('enter value 2:'))
c = int(input('enter value 3:'))

avg = (a + b + c) / 3
print('avg =', avg)

if avg> a and avg > b and avg > c:
    print('%d is higher than %d, %d, %d') %(avg, a, b, c)
elif avg> a and avg > b:
    print('%d is higher than %d, %d') %(avg, a, b)
elif avg> a and avg > c:
    print('%d is higher than %d, %d') %(avg, a, c)
elif avg> b and avg > c:
    print('%d is higher than %d, %d') %(avg, b, c)
elif avg > a:
    print('%d is higher than %d, %d') %(avg, a, c)
else:
    print('invalid input')