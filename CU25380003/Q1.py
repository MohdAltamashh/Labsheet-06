# Q1- Write a Python program to create and display a set.



print("--- Creating and Displaying a Set ---")

# 1. Create a set using curly braces {}
# Note: Sets only store unique elements. Duplicates (like 10 and 'banana') are automatically removed.
simple_set = {10, 20, "apple", 50, "banana", 10, "cherry", "banana"}

print(f"The set has been created: {simple_set}")
print(f"Data type confirmed: {type(simple_set)}")

# 2. Demonstration of adding an element
print("\n--- Adding an element ---")
simple_set.add(99)
print(f"Set after adding 99: {simple_set}")