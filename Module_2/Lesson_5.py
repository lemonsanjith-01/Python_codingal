# a pattern needs two things:

# 1) how many rows
#rows = int(input('How many rows do you want?'))
# 2) how many characters per row

#for i in range(rows):
 #   print(i)
  #  for j in range(i + 1):
     #   print(j,)
   #     print("*", end="")
    #print()
#Right angle triangle activity:
print('Half Pyramid pattern of stars (*):')
n = int(input('Enter the amount of rows: '))
for i in range(n):
    for j in range(i+1):
        print('* ', end='')
    print()

#Floyd's triangle
rows = int(input('please Enter the total number of rows: '))
number = 1

print("Floyd's triangle")
for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(number, end='  ')
        number = number + 1
    print()

#diamond shape
rowSize = int(input('enter number of the rows:'))
if rowSize%2==0:
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow - 1
for i in range(1, halfDiamRow+1):
    for j in range(1, space+1):
        print(end=' ')
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(end=str(num))
        num = num + 1
    print()