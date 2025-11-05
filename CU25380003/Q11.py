#Q11.  Write a program to find the union of two sets.


# 1. Create two initial sets
set_a = {"apple", "banana", "cherry", "date"}
set_b = {"cherry", "date", "elderberry", "fig"}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 2. Find the union using the '|' operator (Operator Method)
# Elements 'cherry' and 'date' are common, so they appear only once in the result.
union_set_operator = set_a | set_b
print(f"\nUnion using '|' operator: {union_set_operator}")

# 3. Find the union using the .union() method (Method Method)
union_set_method = set_a.union(set_b)
print(f"Union using .union() method: {union_set_method}")

# Verify that both methods produce the same result
print(f"Are the results identical? {union_set_operator == union_set_method}")