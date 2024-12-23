"""
Created on Fri Oct 18 14:23:41 2024

@author: mr-arthor
"""

import pandas as pd


df = pd.DataFrame() # Calling DataFrame constructor
print (df)
data = ['BCA', 'MCA', 'BTech', 'MTech', 'MBA', 'PHD', 'Bsc'] # list of strings
df = pd.DataFrame(data) # Calling DataFrame constructor on list
print (df)
