#Q27-  Write a program to check if two strings are anagrams using sets.


# Program to check if two strings are anagrams.

string_1 = "Debit Card"
string_2 = "Bad Credit"

# 1. Normalize (lowercase, remove spaces).
s1_normalized = string_1.lower().replace(" ", "")
s2_normalized = string_2.lower().replace(" ", "")

# 2. Sort the characters of both strings.
# This creates a list of characters where frequency is preserved.
s1_sorted = sorted(s1_normalized)
s2_sorted = sorted(s2_normalized)

# 3. Check if the sorted lists are identical.
is_anagram = s1_sorted == s2_sorted

print(f"String 1: '{string_1}'")
print(f"String 2: '{string_2}'")
print(f"Are they anagrams? -> {is_anagram}")