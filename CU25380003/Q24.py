#Q24-  Write a program to convert a string into a set of characters.


# Input string
input_string = "programming in python"

print(f"Original String: '{input_string}'")

# Use the set() constructor on the string.
# The set constructor automatically iterates through the string (treating it 
# as an iterable of characters) and keeps only the unique characters.
character_set = set(input_string)

print("-" * 30)
# The resulting set will not retain the original order and will only contain
# the distinct characters, including spaces.
print(f"Set of Unique Characters: {character_set}")
print(f"Total distinct characters (including space): {len(character_set)}")

# Example 2
input_string_2 = "apple pie"
character_set_2 = set(input_string_2)
print(f"\nString 2: '{input_string_2}' -> Set: {character_set_2}")