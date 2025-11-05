# Q2- Write a program to create a set with different data types.


print("--- Creating and Displaying a Set with Mixed Data Types ---")
simple_set = {10, 20, "apple", 50, "banana", 10, "cherry", "banana", 3.14, True}

print(f"The set has been created: {simple_set}")
print(f"Data type confirmed: {type(simple_set)}")

# 2. Demonstration of adding an element
print("\n--- Adding a new data type (tuple) ---")
# Tuples are immutable and can be added to a set
immutable_tuple = ("red", "green", "blue")
simple_set.add(immutable_tuple)
print(f"Set after adding a tuple ({immutable_tuple}): {simple_set}")

# 3. Removing a float element
print("\n--- Removing a float element ---")
simple_set.discard(3.14)
print(f"Set after removing 3.14: {simple_set}")