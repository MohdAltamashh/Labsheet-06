#Q4-  Write a program to add multiple elements to a set.


# Create a set of initial elements
my_products = {"keyboard", "mouse", "monitor"}

print(f"The initial set: {my_products}")
print(f"Number of elements: {len(my_products)}")


print("\n 2. Adding Multiple Elements (using .update()) ")

# New elements to add:
new_accessories = ["webcam", "headset", "mouse", "speaker"]

print(f"Elements to add: {new_accessories}")

# Add the new elements to the set
my_products.update(new_accessories)

print(f"Set after adding multiple elements: {my_products}")
print(f"New number of elements: {len(my_products)}")
# Note: 'mouse' was a duplicate, so it was added only once, and 'mouse' was not a new element

print("\n--- 3. Showing Duplicates are Handled ---")

# Demonstrate that 'mouse' was only counted once, even though it was in both the initial set and the update list.
print(f"Final set (guaranteed to contain only unique items): {my_products}")