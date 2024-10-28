"""
Created on Thu Oct 17 12:17:10 2024

@author: mr-arthor
"""

# =============================================================================
# Write a function find_longest_word() that takes a list of words and returns the
# length of the longest one.
# =============================================================================

def find_longest_word(words):
    return max(len(word) for word in words)

words_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(find_longest_word(words_list))

