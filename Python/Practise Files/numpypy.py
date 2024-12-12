# =============================================================================
# """
# Created on Fri Oct 18 11:17:13 2024
# 
# @author: mr-arthor
# """
# import numpy \
# # =============================================================================
# #     =============================================================================
# # =============================================================================
# # print (my_arr) 
# # =============================================================================
# 
# # =============================================================================
# # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# # print (arr)
# # =============================================================================
# 
# # =============================================================================
# # arr = np.array([1, 2, 3, 4], ndmin=5)
# # print(arr)
# # print('number of dimensions :', arr.ndim)
# # =============================================================================
# x = numpy.array([[6, 12], [8, 13]]) # initializing matrices
# y = numpy.array([[7, 14], [9, 15]])
# print ("The element wise addition of matrix is : ")
# print (numpy.add(x,y)) # using add() to add matrices
# print ("The element wise subtraction of matrix is : ")
# print (numpy.subtract(x,y)) # using subtract() to subtract matrices
# print ("The element wise division of matrix is : ")
# print (numpy.divide(x,y)) # using divide() to divide matrices
# print ("The element wise multiplication of matrix is : ")
# print (numpy.multiply(x,y)) # using multiply() to multiply matrices element wise
# print ("The product of matrices is : ")
# print (numpy.dot(x,y)) # using dot() to multiply matrices
# print ("The element wise square root is : ")
# print (numpy.sqrt(x)) #
# print ("The summation of all matrix element is : ")
# print (numpy.sum(y)) #using sum() to print summation of all elements of matrix
# print ("The column wise summation of all matrix is : ")
# print (numpy.sum(y,axis=0)) # using sum(axis=0) Sum of all columns of matrix
# print ("The row wise summation of all matrix is : ")
# print (numpy.sum(y,axis=1)) # using sum(axis=1) Sum of all columns of matrix
# print ("The transpose of given matrix is : ")
# print (y.T) # using "T" to transpose the matrix
# =============================================================================


import numpy as np

# 1. Creating a 2D array
arr = np.array([[1, 2, 3], ["jk", 5, 6], [7, 8, 9]])

# 1. Ndim – Get the number of dimensions of the array
print("Dimensions of array:", arr.ndim)

# 2. Itemsize – Get the size of each element in bytes
print("Item size of array elements (in bytes):", arr.itemsize)

# 3. Dtype – Get the data type of elements
print("Data type of array:", arr.dtype)

# 4. Reshape – Reshape the array
reshaped_arr = arr.reshape(1, 9)  # Convert to a 1x9 array
print("Reshaped array:\n", reshaped_arr)

# 5. Slicing – Extract specific elements
slice_arr = arr[0:2, 1:3]  # Extracts first two rows and last two columns
print("Sliced array:\n", slice_arr)

# 6. Linspace – Generate evenly spaced numbers
linspace_arr = np.linspace(0, 1, 5)  # Generates 5 numbers between 0 and 1
print("Linspace array:", linspace_arr)

# 7. Max/Min, Sum, Sqrt
print("Max value in array:", arr.max())
print("Min value in array:", arr.min())
print("Sum of array elements:", arr.sum())
print("Square root of array elements:\n", np.sqrt(arr))

# 8. Ravel – Flatten the array
ravel_arr = arr.ravel()
print("Flattened array:", ravel_arr)
