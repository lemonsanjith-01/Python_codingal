# GROCERY COST COMPARISON TOOL
print("=== GROCERY COST COMPARISON TOOL ===")

# ---------- PART 1: what did this week's shop cost per person? ----------
rice_price = 12            # (given)
milk_price = 4             # (given)
fruit_price = 8            # (given)
number_of_baskets = 2      # (given)
family_members = 4         # (given)

cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_members

# ---------- PART 2: can the items be shared equally? ----------
total_items = int(input("Enter the total number of items: "))
people = int(input("Enter the number of people: "))
if total_items % people == 0:
    print("The items can be shared equally.")
else:
    print("The items cannot be shared equally.")
    print(f"There will be {total_items % people} items left over.")

# ---------- PART 3: compare with three stores ----------
weekly_average = 72.5      # (given) the corrected weekly average
store_a_average = 70       # (given)
store_b_average = 75       # (given)
store_c_average = 80       # (given)

if weekly_average < store_a_average and weekly_average < store_b_average and weekly_average < store_c_average:
    verdict = "cheaper than all three stores"
elif weekly_average > store_a_average and weekly_average > store_b_average and weekly_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"

print("\n=== SUMMARY ===")                                   # (given)
print("Cost per person this week:", cost_per_person)         # (given)
print("Weekly average           :", weekly_average)          # (given)
print("Verdict                  :", verdict)                 # (given)