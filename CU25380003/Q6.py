#Q6-  Write a program to remove an element from a set using discard().


# 1. Create the set
items = {"book", "pen", "pencil", "eraser"}
print(f"Initial set: {items}")

# 2. Use .discard() to delete an existing element
items.discard("pen")
print(f"Set after discarding 'pen': {items}")

# 3. Demonstrate safe handling of a non-existent element
# 'marker' is not in the set, but discard() does nothing and raises no error.
items.discard("marker")
print(f"Set after attempting to discard 'marker' (no change, no error): {items}")