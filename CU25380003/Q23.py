#Q23-  Write a program to remove duplicates from a list using a set.


# Input list with duplicate values
data_list = [4, 10, 2, 4, 8, 10, 2, 1, 6, 8]

print(f"Original List (with duplicates): {data_list}")
print(f"Original Length: {len(data_list)}")
print("-" * 40)

# --- Steps to Remove Duplicates ---

# 1. Convert the list to a set. This retains only unique elements.
unique_set = set(data_list)
# Note: The order of elements is lost here.

# 2. Convert the set back to a list if a list structure is required for the output.
list_without_duplicates = list(unique_set)

# --- Output the result ---
print(f"Set of Unique Elements: {unique_set}")
print(f"List without Duplicates: {list_without_duplicates}")
print(f"New Length: {len(list_without_duplicates)}")