"""
Created on Thu Oct 17 14:24:49 2024

@author: mr-arthor
"""
# =============================================================================
# 
# 6.Write a function filter_long_words() that takes a list of words and an integer n and
# returns the list of words that are longer than n
# =============================================================================


def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

words_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(filter_long_words(words_list, 5))
