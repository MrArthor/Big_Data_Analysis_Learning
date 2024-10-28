str1 = 'Cdacdelhi'
upper = lambda string: string.upper()        # upper is the lambda function
print(upper(str1))


x = lambda a : a + 10
print(x(5))                                # here X is the function
 
x = lambda a, b : a * b
print(x(5, 6))                             # here x is the function taking two arguments

x = lambda a, b, c : a + b * c
print(x(5, 6, 2))

Max = lambda a, b : a if(a > b) else b  # use of lambda function with if -else 
print("The Result is:",Max(55, 34))

age = [35, 12, 69, 55, 75, 14, 73]      # list is created for age 
detail = list(filter( lambda num: (num % 2 == 0) , age ))      
print('The list of age  is:',detail)    


# to find the sqaure of each item using lambda function
numbers = [22, 24, 25, 21, 23, 37, 28, 29, 40]      
new_list = list(map( lambda num: num ** 2 , numbers))      
print( 'Square of number in the given list:' ,new_list )    

# to find the odd number and even number from a list
seq = [0, 1, 2, 3, 5, 8, 13,17,20,36,46,49,53]
result = filter(lambda x: x % 2 != 0, seq)
print("The odd numbers are:", list(result))

numbers = [22, 24, 25, 21, 23, 37, 28, 29, 40]      
new_list = list(filter(lambda num:num**2,numbers))      
print('Square of number in the given list:',new_list)    


# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print("The Even Number are :" ,list(result))
horsemen = ['war', 'pestilence', 'famine']
str(horsemen) 

lang = ("C","C++","Java","Python")  
# Calling function  
att = dir(lang)  
# Displaying result  
print(att)  

pi = 34
formatted = format(pi, 'e')
print(formatted)

# input function
name = input("What is your name? ")
print(f"My Name is: {name}")

# create list by using user input


# creating an empty list
test = []
n = int(input("Enter number of elements : ")) # number of elements as input
# iterating till the range
for i in range(0, n):
	item = int(input())
	test.append(item)  # adding the element
print("The user input List is: ",test)

#list as input from user in Python Using map()  

n = int(input("Enter number of elements : "))  # number of elements

# Below line read inputs from user using map() function
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", a)


# zip () function
animal = ['cat', 'dog', 'bird', 'great white shark']
weight = [9, 50, 0.33,65]
food =('Bread','Grass','Wheat','fish')
country={'India',"Srilanka",'Africa','USA'}
disct={'leg':4, 'color': 'Black' , 'Nature': 'Runn'}
detail = zip(animal, weight,food,country,disct)
print(list(detail))

# Module in python 
# importing built-in module math
import math

# using square root(sqrt) function contained 

print(math.sqrt(25)) 

# using pi function contained in math module
print(math.pi) 

# 2 radians = 114.59 degrees
print(math.degrees(2)) 

# 60 degrees = 1.04 radians
print(math.radians(60)) 

# Sine of 2 radians
print(math.sin(80)) 

# Cosine of 0.5 radians
print(math.cos(45)) 

# Tangent of 0.23 radians
print(math.tan(56)) 

print(math.factorial(4)) 

