#Q16-  Write a program to check if a set is a superset of another set.


# Check if Set A is a superset of Set B using the >= operator

set_A = {10, 20, 30, 40, 50} # Potential Superset
set_B = {20, 50}             # Potential Subset

# The shortest way to check: >= returns True if the left set is a superset of the right set.
is_superset = set_A >= set_B

print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"Is A a superset of B? (A >= B) -> {is_superset}")

# Example 2 (Not a superset)
set_C = {10, 60}
is_superset_2 = set_A >= set_C

print(f"\nSet C: {set_C}")
print(f"Is A a superset of C? (A >= C) -> {is_superset_2}")