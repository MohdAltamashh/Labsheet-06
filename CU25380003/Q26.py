#Q26-  Write a program to find unique words in a sentence using a set.


# Input sentence
sentence = "The quick brown fox jumps over the lazy dog dog dog"

print(f"Original Sentence: '{sentence}'")
print("-" * 40)

# 1. Convert the sentence to lowercase to ensure case-insensitive matching
#    (e.g., "The" and "the" are treated as the same word).
normalized_sentence = sentence.lower()

# 2. Split the sentence into a list of words.
#    The split() method, without arguments, splits by whitespace.
word_list = normalized_sentence.split()

print(f"List of all words (with duplicates): {word_list}")

# 3. Convert the list of words into a set.
#    The set constructor automatically removes all duplicate words.
unique_words_set = set(word_list)

# 4. Convert back to a list (optional) if you want a list output, 
#    but the set itself holds the unique words.
unique_words_list = list(unique_words_set)

# --- Output the result ---
print("-" * 40)
print(f"Unique words found (Set): {unique_words_set}")
print(f"Total number of unique words: {len(unique_words_set)}")
