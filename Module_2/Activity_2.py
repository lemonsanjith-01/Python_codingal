n = int(input('Enter the number whose sum you want to find:'))
sum = 0

for num in range(1,n+1):
    sum = sum+num
    print('\nSum =', sum)

#activity 2

string = input('please enter your own String : ')

string2 = (' ')

for i in string:
    string2 = i +string2

print('\nThe Original String = ', string)
print('The Reversed String = ', string2)
