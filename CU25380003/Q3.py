#Q3- Write a program to add a single element to a set.


print("--- 1. Initial Set Creation ---")

# Create a set of integer elements
my_shopping_list = {"milk", "bread", "eggs"}

print(f"The initial set: {my_shopping_list}")
print(f"Number of elements: {len(my_shopping_list)}")


print("\n--- 2. Adding a Single Element (using .add()) ---")

# The .add() method is used to insert one single element into the set.
# If the element is already present, the set remains unchanged.
new_item = "cheese"
my_shopping_list.add(new_item)

print(f"Set after adding '{new_item}': {my_shopping_list}")
print(f"New number of elements: {len(my_shopping_list)}")


print("\n--- 3. Attempting to Add a Duplicate Element ---")

# Attempt to add 'milk' again (it will be ignored because sets only store unique elements)
duplicate_item = "milk"
my_shopping_list.add(duplicate_item)

print(f"Set after attempting to add '{duplicate_item}': {my_shopping_list}")
print(f"Number of elements remains the same (4): {len(my_shopping_list)}")