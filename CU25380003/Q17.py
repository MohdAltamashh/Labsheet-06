#Q17-  Write a program to check if two sets are disjoint.


# Check if two sets are disjoint using the isdisjoint() method

set_X = {10, 20, 30}
set_Y = {40, 50, 60} # Disjoint (no common elements)
set_Z = {30, 70, 80} # Not disjoint (element 30 is common)

# Example 1: Disjoint sets (Expected: True)
is_disjoint_1 = set_X.isdisjoint(set_Y)

print(f"Set X: {set_X}")
print(f"Set Y: {set_Y}")
print(f"Are X and Y disjoint? -> {is_disjoint_1}")

# Example 2: Non-disjoint sets (Expected: False)
is_disjoint_2 = set_X.isdisjoint(set_Z)

print(f"\nSet X: {set_X}")
print(f"Set Z: {set_Z}")
print(f"Are X and Z disjoint? -> {is_disjoint_2}")