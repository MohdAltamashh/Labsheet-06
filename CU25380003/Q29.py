#Q29-  Write a program to find maximum and minimum values in a set.


# Define a set of numeric data
data_set = {45, 12, 99, 3, 58, 21, 75}

print(f"Original Set: {data_set}")
print("-" * 40)

# 1. Finding the Maximum Value
# The max() function returns the largest item in an iterable.
maximum_value = max(data_set)

# 2. Finding the Minimum Value
# The min() function returns the smallest item in an iterable.
minimum_value = min(data_set)

# --- Output the result ---
print(f"Maximum Value in the set: {maximum_value}")
print(f"Minimum Value in the set: {minimum_value}")

# --- Example with Non-Numeric Data (Strings) ---
# max() and min() also work with strings, comparing them lexicographically.
string_set = {"apple", "zebra", "banana", "cat"}

max_string = max(string_set)
min_string = min(string_set)

print("-" * 40)
print(f"String Set: {string_set}")
print(f"Lexicographically Largest (Max): {max_string}")
print(f"Lexicographically Smallest (Min): {min_string}")