# ================================
# PERSONAL GOALS DISPLAY
# ================================

# ---------- PART 1: import the keyword module ----------
import keyword
# ---------- PART 2: ask the three questions ----------
person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month = input("Enter the month you want to reach it by: ")
# ---------- PART 3: store the practice time ----------
daily_minutes = 30
# ---------- PART 4: the heading ----------
print("\nMY PERSONAL GOAL PLAN\n")
# Print MY PERSONAL GOAL PLAN with one blank line above it and one below.
# Do it in a single print() using \n at the start and the end.


# ---------- PART 5: the four plan lines ----------
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")
# ---------- PART 6: two lines that join up ----------
print("Status: ", end=" ")
print("Not started")
print("Reminder:-", end=" ")
print("Practise every day!")
# ---------- PART 7: the sentence and the keywords ----------
print("\nIn one sentence:", person_name, "wants to get better at", goal_name, "by", target_month, "by practising for", daily_minutes, "minutes a day.")