# ================================
# SCHOOL CLUB MEMBER BADGE
# ================================

# ---------- PART 1: member details ----------
import keyword
member_name = input("Enter your name: ")
club_name = input("Enter the club name: ")
# ---------- PART 2: data types ----------
member_number = 8
points = 9.5
is_active = True
print("Member number:", member_number, "Data type:", type(member_number))
print("Points:", points, "Data type:", type(points))
print("Is active:", is_active, "Data type:", type(is_active))

# ---------- PART 3: badge code ----------
badge_code = member_name[:3] + club_name[-1] + str(member_number)
print("Badge code:", badge_code)

# ---------- PART 4: final badge ----------
print("===== CLUB BADGE =====")
print("Member:", member_name)
print("Club:", club_name)
print("Code:", badge_code)
print("Points:", points)
print("Active:", is_active)