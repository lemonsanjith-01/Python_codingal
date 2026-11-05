#test_value = 0

#while test_value <= 0:
    #print('hi')
    #test_value += 1
    #if test_value == 3:
     #   break


total_chores = 4
original_count = total_chores
print(f'you have {original_count} chores to finish today.')

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: 
        next_chore = 'Make your bed'
    elif chore_num == 2:
        next_chore = 'Feed the pet'
    elif chore_num == 3:
        next_chore = 'Take out the trash'
    else:
        next_chore = 'Wash the dishes'

    answer = input(f'Have you finished: {next_chore}? (yes/no): ')

    if answer == 'yes':
        completed_count += 1
        chore_num += 1
        print('Great job! Chore completed!')
    else:
        print('Okay, finish it and check again')

    print('Chores remaing:', total_chores - completed_count)
    print()


print('===== ALL CHORES COMPLETE! =====')
print('Great work finish ing your entire checklist today :)!\n')


print("Now let's safely peek at an infinite loop...")
test_value=0
safety_counter = 0
while test_value <= 0:
    print('Oh no! This will go on forever!')
    safety_counter += 1
    if safety_counter == 3:
        print('Haha i am joking we will stop here on purpose. However real infinite loops will go on and on forever.')
        break

print('\n===== CHORE CHECKLIST SUMMARY =====')
print('Chores assigned today:', original_count)
print('Chores completed:', completed_count)
print('Chores remaining:', total_chores - completed_count)
print('======================================')