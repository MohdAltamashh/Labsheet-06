#Q12.  Write a program to find the intersection of two sets.


# 1. Create two initial sets
set_a = {"apple", "banana", "cherry", "date"}
set_b = {"cherry", "date", "elderberry", "fig"}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 2. Find the intersection using the '&' operator (Operator Method)
# Only elements found in BOTH sets ('cherry', 'date') are included.
intersection_set_operator = set_a & set_b
print(f"\nIntersection using '&' operator: {intersection_set_operator}")

# 3. Find the intersection using the .intersection() method (Method Method)
intersection_set_method = set_a.intersection(set_b)
print(f"Intersection using .intersection() method: {intersection_set_method}")

# Verify that both methods produce the same result
print(f"Are the results identical? {intersection_set_operator == intersection_set_method}")