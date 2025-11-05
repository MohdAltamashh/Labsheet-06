#Q20-  Write a program to find the Cartesian product of two sets.



import itertools

# --- Define the input sets ---
set_X = {1, 2}
set_Y = {'a', 'b', 'c'}

print(f"Set X: {set_X}")
print(f"Set Y: {set_Y}")
print("-" * 40)

# --- Cartesian Product (X x Y) Logic ---

# 1. Use itertools.product to generate all ordered pairs (tuples)
#    where the first element comes from set_X and the second from set_Y.
product_iterator = itertools.product(set_X, set_Y)

# 2. Convert the resulting iterator into a list for display.
cartesian_product_xy = list(product_iterator)

# --- Output the result ---

# X x Y = {(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')}
print(f"Cartesian Product (X x Y): {cartesian_product_xy}")

print("-" * 40)

# --- Cartesian Product (Y x X) Example ---

# Calculate Y x X 
cartesian_product_yx = list(itertools.product(set_Y, set_X))

# Y x X = {('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)}
print(f"Cartesian Product (Y x X): {cartesian_product_yx}")