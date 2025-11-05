#Q28-  Write a program to create a frozen set and demonstrate its properties.



# 1. Standard (Mutable) Set
mutable_set = {10, 20}

# 2. FrozenSet (Immutable)
frozen_set = frozenset({30, 40})

print("--- FrozenSet Hashability ---")
print(f"Mutable Set: {mutable_set}")
print(f"FrozenSet:   {frozen_set}")
print("-" * 40)

# Property Demonstration: Standard sets are NOT hashable
try:
    # This will fail because mutable_set can change and therefore cannot be hashed.
    container_set = {mutable_set} 
except TypeError as e:
    print(f"Error when nesting mutable_set: {e}")
    print("-> RESULT: Mutable sets cannot be elements of other sets.")

# Property Demonstration: FrozenSets ARE hashable
try:
    # This succeeds because frozen_set cannot change and is hashable.
    container_set = {frozen_set} 
    print(f"\nSet containing frozen_set: {container_set}")
    print("-> RESULT: FrozenSets can be elements of other sets.")
except Exception as e:
    print(f"Unexpected error: {e}")