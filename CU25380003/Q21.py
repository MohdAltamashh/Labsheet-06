#21. Write a program to count distinct elements from a list using a set.


# Input list with duplicate elements
data_list = [10, 20, 30, 10, 40, 50, 20, 60, 10, 70]

print(f"Original List: {data_list}")
print(f"Total elements in list: {len(data_list)}")

# 1. Convert the list to a set. This automatically handles and removes duplicates.
#    Example: {10, 20, 30, 40, 50, 60, 70}
unique_set = set(data_list)

# 2. Find the length of the resulting set.
distinct_count = len(unique_set)

print(f"\nSet of distinct elements: {unique_set}")
print(f"Number of distinct elements: {distinct_count}")