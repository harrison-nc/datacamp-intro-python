# Instruction
# -----------
# 1. Update the area of the bathroom area to be
#    10.50 square meters instead of 9.50.
# 2. Make the areas list more trendy! Change
#    "living room" to "chill zone".

# Solution
# --------

# Create the areas list
areas = ["hallway", 11.25,
         "kitchen", 18.0,
         "living room", 20.0,
         "bedroom", 10.75,
         "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

# Print out areas
print(areas)
