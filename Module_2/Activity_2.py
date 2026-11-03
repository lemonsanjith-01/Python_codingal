n = int(input('Enter the number whose sum you want to find:'))
sum = 0

for num in range(1,n+1):
    sum = sum+num
    print('\nSum =', sum)