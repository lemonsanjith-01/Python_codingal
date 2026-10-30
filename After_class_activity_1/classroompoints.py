team1 = 125
team2 = 100
team3 = 120
team4 = 111
team5 = 85

total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("Total points       :", total)
print("Average per team   :", average)

stars_per_point = 2
reward_stars = total * stars_per_point
print("Total reward stars :", reward_stars)

boxes = reward_stars // 25
leftover = reward_stars % 25
 
print("Full boxes packed  :", boxes)
print("Leftover stars     :", leftover) 

last_week = 600
 
print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)

total += 30
print("After bonus points :", total)
 
total -= 15
print("After missed tasks :", total)

reward_stars = total * stars_per_point
boxes = reward_stars // 25
 
print("Final boxes packed :", boxes)
