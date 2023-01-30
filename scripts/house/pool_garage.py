# Instruction
# -----------
# 1. Use the + operator to paste the list
#    ["pool_house", 24.5] to the end of the
#    areas list. Store the resulting list as
#    areas_1.
# 2. Further extend areas_1 by adding data on
#    your garage. Add the string "garage" and
#    float 15.45. Name the resulting list areas_2

# Solution
# --------
areas = ["hallway", 11.25,
         "kitchen", 18.0,
         "living room", 20.0,
         "bedroom", 10.75,
         "bathroom", 9.50]

# Add pool_house data to areas, new list is
# areas_1
areas_1 = areas + ["pool_house", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

# Print areas, areas_1, areas_2
print(areas)
print(areas_1)
print(areas_2)
