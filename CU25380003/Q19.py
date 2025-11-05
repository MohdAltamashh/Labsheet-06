#Q19. Write a program to create the power set of a given set.


import itertools

# Define the input set
input_set = {1, 'b', 'c'}

# The power set logic starts here
# ------------------------------

# 1. Convert the set to a list. This is necessary because itertools.combinations 
#    needs an ordered iterable for consistent indexing.
s = list(input_set)

# 2. Use a list comprehension to generate the power set.
#    We iterate through all possible subset lengths (r), from 0 (empty set) 
#    up to the total length of the set (len(s)).
power_set = [
    set(subset) 
    for r in range(len(s) + 1) 
    for subset in itertools.combinations(s, r)
]

# ------------------------------
# Output the result

print(f"Original Set: {input_set}")
print(f"The Power Set P(S) contains {len(power_set)} subsets:")
print(f"{power_set}")