"""
Created on Thu Oct 17 14:27:59 2024

@author: mr-arthor
"""

def correct(text):
    # Replace multiple spaces with a single space
    text = ' '.join(text.split())
    # Add a space after periods if followed by a letter
    text = text.replace('. ', '.').replace('.', '. ')
    return text.strip()

print(correct("This is very  funny and  cool.Indeed!"))
