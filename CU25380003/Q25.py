#Q25-   Write a program to find common letters in two strings using sets.


# Input strings
string_1 = "programming"
string_2 = "python is fun"

print(f"String 1: '{string_1}'")
print(f"String 2: '{string_2}'")
print("-" * 40)

set_1 = set(string_1)
set_2 = set(string_2)

print(f"Set 1 (Unique chars in String 1): {set_1}")
print(f"Set 2 (Unique chars in String 2): {set_2}")

# 2. Find the intersection of the two sets.
#    The intersection operator (&) returns a new set containing only 
#    elements that are present in BOTH set_1 and set_2.
common_characters = set_1 & set_2

print("-" * 40)
print(f"Common Letters (Intersection): {common_characters}")
print(f"Total number of common distinct letters: {len(common_characters)}")