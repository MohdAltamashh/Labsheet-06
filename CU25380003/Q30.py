#Q30- Write a program to perform all basic set operations (union, intersection, difference,
symmetric difference) in one program.



set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print("--- Basic Set Operations (Short Code) ---")
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print("-" * 40)

# 1. Union (Elements in A OR B): The | (pipe) operator
union_set = set_A | set_B
print(f"1. Union (A | B)        : {union_set}")

# 2. Intersection (Elements in A AND B): The & (ampersand) operator
intersection_set = set_A & set_B
print(f"2. Intersection (A & B) : {intersection_set}")

# 3. Difference (Elements in A BUT NOT B): The - (minus) operator
difference_set = set_A - set_B
print(f"3. Difference (A - B)   : {difference_set}")

# 4. Symmetric Difference (Elements in A OR B, but NOT both): The ^ (caret) operator
symmetric_difference_set = set_A ^ set_B
print(f"4. Symmetric Difference (A ^ B): {symmetric_difference_set}")
print("-" * 40)