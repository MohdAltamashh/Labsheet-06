#Q5.  Write a program to remove an element from a set using remove().


# 1. Create the set
items = {"book", "pen", "pencil", "eraser"}
print(f"Initial set: {items}")

# 2. Use .remove() to delete an existing element
try:
    items.remove("pen")
    print(f"Set after removing 'pen': {items}")

    # 3. Demonstrate the KeyError for a non-existent element
    items.remove("marker")
except KeyError:
    print("\nError: The element you tried to remove was not found in the set.")
    print(f"Final set state: {items}")