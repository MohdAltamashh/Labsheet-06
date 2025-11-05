#Q18-  Write a program to remove all elements of one set from another set.


# Program to remove all elements of set B from set A (in-place modification)

set_A = {1, 2, 3, 4, 5}
set_B = {3, 5, 6, 7} # Elements 3 and 5 will be removed from set_A

print(f"Original Set A: {set_A}")
print(f"Set B (Elements to remove): {set_B}")

# Shortest way to perform in-place set difference:
# This removes all elements in set_B from set_A
set_A -= set_B

print(f"\nSet A after removing elements of B: {set_A}")