# Instruction
# -----------
# 1. Finish the list of lists so that it also
#    contains the bedroom and bathroom data.
#    Make sure you enter these in order!
# 2. Print out house; does this way of
#    structuring your data make more sense?
# 3. Print out the type of house. Are you still
#    dealing with a list?



# Solution
# --------

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.58

# house information as list of lists
house = [["hallway", hall], 
         ["kitchen", kit],
         ["living room", liv], 
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
