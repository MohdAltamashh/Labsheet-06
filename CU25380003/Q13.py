#Q13-  Write a program to find the difference of two sets.


# 1. Create two initial sets
set_a = {"apple", "banana", "cherry", "date"}
set_b = {"cherry", "date", "elderberry", "fig"}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 2. Find the difference A - B using the '-' operator (Operator Method)
# Result: Elements in A that are not in B (apple, banana)
difference_a_minus_b_operator = set_a - set_b
print(f"\nDifference A - B using '-' operator: {difference_a_minus_b_operator}")

# 3. Find the difference B - A using the .difference() method (Method Method)
# Result: Elements in B that are not in A (elderberry, fig)
difference_b_minus_a_method = set_b.difference(set_a)
print(f"Difference B - A using .difference() method: {difference_b_minus_a_method}")

# Note: The difference is NOT commutative (A - B is not the same as B - A)
print(f"\nIs A - B equal to B - A? {difference_a_minus_b_operator == difference_b_minus_a_method}")