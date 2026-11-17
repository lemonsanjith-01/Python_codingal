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