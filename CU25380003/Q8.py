# Q8-  Write a program to check if an element exists in a set.


# 1. Create the initial set
countries = {"USA", "Canada", "Mexico", "Brazil", "UK"}
print(f"Set of countries: {countries}")

# Define elements to check
check_country_1 = "Canada"
check_country_2 = "Japan"

# 2. Check for the existence of the first element using 'in'
print(f"\nChecking for '{check_country_1}':")
if check_country_1 in countries:
    print(f"'{check_country_1}' is a member of the set.")
else:
    print(f"'{check_country_1}' is NOT a member of the set.")

# 3. Check for the existence of the second element using 'in'
print(f"\nChecking for '{check_country_2}':")
if check_country_2 in countries:
    print(f"'{check_country_2}' is a member of the set.")
else:
    print(f"'{check_country_2}' is NOT a member of the set.")