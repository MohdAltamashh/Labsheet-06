#Q22-  Write a program to find duplicate elements in a list using a set.


# Input list containing duplicates
data_list = [5, 12, 8, 12, 15, 5, 20, 8, 30, 45, 12]

# Initialize two sets:
# 1. 'seen': to track every unique element encountered.
# 2. 'duplicates': to store elements that appear more than once.
seen = set()
duplicates = set()

print(f"Original List: {data_list}")
print("-" * 30)

# Iterate through the list
for element in data_list:
    # Check if the element is already in the 'seen' set
    if element in seen:
        # If it is, it's a duplicate. Add it to the 'duplicates' set.
        # Adding to a set ensures we only record each duplicate once.
        duplicates.add(element)
    else:
        # If it's the first time seeing this element, add it to the 'seen' set.
        seen.add(element)

# --- Output the result ---
# The result is automatically a set of unique duplicate values: {5, 8, 12}
print(f"Found Duplicate Elements: {duplicates}")
print(f"Total number of distinct duplicates found: {len(duplicates)}")