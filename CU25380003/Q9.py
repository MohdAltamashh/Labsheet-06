#Q9-  Write a program to find the length of a set.


# 1. Create the initial set
countries = {"USA", "Canada", "Mexico", "Brazil", "UK"}
print(f"Set of countries: {countries}")

# 2. Use len() to find the initial number of elements
initial_length = len(countries)
print(f"\nInitial length of the set: {initial_length}")

# 3. Add a new element to demonstrate length change
countries.add("Germany")
print(f"Set after adding 'Germany': {countries}")

# 4. Use len() again to find the updated number of elements
updated_length = len(countries)
print(f"Updated length of the set: {updated_length}")