#Q15-  Write a program to check if a set is a subset of another set.


# Check if Set A is a subset of Set B using the <= operator

set_A = {1, 2, 3}
set_B = {1, 2, 3, 4, 5}

# The shortest way to check: <= returns True if the left set is a subset of the right set.
is_subset = set_A <= set_B

print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"Is A a subset of B? {is_subset}")

# Example 2 (Not a subset)
set_C = {3, 6}
is_subset_2 = set_C <= set_B

print(f"\nSet C: {set_C}")
print(f"Is C a subset of B? {is_subset_2}")