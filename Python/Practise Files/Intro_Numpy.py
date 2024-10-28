""" 
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra,
 fourier transform, and matrices.
 
In Python we have lists that serve the purpose of arrays, but they are slow to
 process.

NumPy aims to provide an array object that is up to 50x faster than traditional
 Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting 
functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are 
very important.
"""

import numpy as np
print(np.__version__)

a = np.array([1,2,3])
print(a)
type(a)
a[0]
a[1]

# 2-D array 

#np.array( [ [] , [] ])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
arr
print('2nd element on 1st dim: ', arr[0, 1])
print('5th element on 2nd dim: ', arr[1, 4])
print('6th element on 2nd dim: ', arr[1, 5]) # will show error
print('Last element from 2nd dim: ', arr[1, -1])


# 3-D array

#arr - np.array([ [ [],[] ] , [ [],[] ] , [ [],[] ] ])


arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr1
print(arr1[0, 1, 2])

"""
The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6

"""



"""----------------SLICING-------------------
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end-1].
We can also define the step, like this: [start:end-1:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr2[::2])

print(arr2[1:5:2])

arr3= np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr3
print(arr3[1, 1:4])

"""-------------------Datatype of Array-----------------------
i - integer
b - boolean
f - float
c - complex float 
{  x = 1 + 2j
  print(x)
  print(type(x)) } 

M - datetime
O - object
S - string
"""

arr5 = np.array([1, 2, 3, 5])
print(arr5.dtype)
arr6= np.array(["apple", "banana", "cherry"])

print(type(arr6))

print(arr6.dtype)

arr7= np.array([1, 2, 3, 4], dtype='f')

print(arr7)
print(arr7.dtype)

arr8= np.array([1, 2, 3, 4], dtype='i')

print(arr8)
print(arr8.dtype)

arr9 = np.array([1.1, 2.1, 3.1])
print(arr9.dtype)
newarr = arr9.astype(int)

print(newarr)
print(newarr.dtype)


"""----------------Numpy Random number------------------


"""
from numpy import random

x = random.randint(1000)
print(x)

# Generate random float between 0 to 1
x1 = random.rand()
print(x1)

# Generate a 1-D array containing 5 random integers from 0 to 100:
x2=random.randint(100, size=(5))
print(x2)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x3= random.randint(100, size=(3, 5))
print(x3)

# Generaten a 1-D and 2-D array containing random float
x4 = random.rand(5)
print(x4)
x5 = random.rand(3, 5)
print(x5)
x6 = random.uniform(10.5, 75.5, size=(2,3))
print(x6)

"""------------- Numpy Arithematic operation-----------
"""
a = np.arange(9).reshape(3,3)
a
b = np.array([10,10,10])
b
addition = np.add(a,b)
addition
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)
