#Q7-  Write a program to clear all elements from a set.


# 1. Create the initial set
countries = {"USA", "Canada", "Mexico", "Brazil", "UK"}
print(f"Initial set of countries: {countries}")
print(f"Set size: {len(countries)}")

# 2. Use .clear() to remove all elements
print("\n--- Clearing the set ---")
countries.clear()

# 3. Display the cleared set
print(f"Set after using .clear(): {countries}")
print(f"Set size: {len(countries)}")