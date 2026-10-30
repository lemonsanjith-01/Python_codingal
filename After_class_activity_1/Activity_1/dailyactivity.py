# ---------- PART 1: homework time ----------
homeworktime = int(input())
# ---------- PART 2: choose a plan ----------
if homeworktime >= 60:
    plan = 'start homework now'
    print('That is a long homework session')
else:
    plan = 'finish homework quickly'
    print('That is a short homework session')
# ---------- PART 3: free time ----------
awnser = input('is there free time after homework (yes/no)')
if awnser == 'yes':
    print('reminder to pick a hobby')
else:
print
print(homeworktime, plan, awnser)
