#Q14-  Write a program to find the symmetric difference of two sets.


# 1. Create two initial sets
set_a = {"apple", "banana", "cherry", "date"}
set_b = {"cherry", "date", "elderberry", "fig"}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# The common elements (intersection) are 'cherry' and 'date'.
# The unique elements are 'apple', 'banana' (from A) and 'elderberry', 'fig' (from B).

# 2. Find the symmetric difference using the '^' operator (Operator Method)
symmetric_difference_operator = set_a ^ set_b
print(f"\nSymmetric Difference using '^' operator: {symmetric_difference_operator}")

# 3. Find the symmetric difference using the .symmetric_difference() method (Method Method)
symmetric_difference_method = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference using .symmetric_difference() method: {symmetric_difference_method}")

# 4. Verify that both methods produce the same result and that order doesn't matter
print(f"\nAre the results identical? {symmetric_difference_operator == symmetric_difference_method}")
print(f"Is A ^ B equal to B ^ A? {symmetric_difference_operator == set_b ^ set_a}")