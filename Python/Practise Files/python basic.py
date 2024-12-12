print("Hello")
print('hello')
# declaring a vairable  
# print after declaring a variable
age = 30.5
age
print("The age is:" ,age)
# casting to find the data type
print(type(age))
# indentation use
if(age>20):
 print(age)
# Mulitple variable and multiple values
 x,y,z ="student","class","age"
 print(z)
 # Mulitple variable and single values
 
 x=y=z= "student" 
 print(z)
 
 name = "Sumit"
 print(name)
 name ='sumit'
 print(name)
 #Case sensitive-
 age = 5
 AGE = 10
 print(age)
 print(AGE)
 # _ unserscore can be use in a variable declaration
my_school="Vidhya"
print(my_school)
_my_name="Vidhya"
print(_my_name)
# Upper case and lower case
age=5
AGE=20
print(age)
# Camel Case
mySchoolName= "Vidhya"
print(mySchoolName)
#Pascal Case
MySchoolName="Vidhya"
print(MySchoolName)
# Snake Case
My_School_Name = "Vidhya"
print(My_School_Name)
# Concatenation 
name ="Amit"
father = "Mohit"
address = "Delhi"
print(name,father,address)
# using + oprrator
print(name + father + address)
# + operator will not work on different datatypes
a = 5
b = "year"
print(a+b)
# global varibales outside the function

a= 35

def myclass():
    print("My age is" ,a)
myclass()

# global variables inside a function
def myclass():
   
    global a
    a = "Examination"
myclass()

print("I am studying for" ,a)
# Data types

#we are using
a="Python is good"        #Text type -str
ax ='Python is similiar to R Programing'
print(ax)
a=10
print(a)
b = 35.8            # Numeric types int, float,complex
print(b)
a = 3+3j   
print(a)

# Random number
import random
print(random.randrange(20,30))

# Multi line string
rules = '''I am working on python,
python is a parsing language,
it is very easy,
We are taking it'''
print(rules) 

# Python - Slicing Strings
b = "Hello, World!"
print(b[1:4])

# Slice From the Start
b = "Hello, World!"
print(b[1:3])
#Slice To the End
b = "Helloh"
print(b[3:])
#Negative Indexing
b = "Helloh"
print(b[-4:-2])

# Python - Modify Strings
#Upper Case
a = "Hello, World!"
print(a.upper())
#Lower Case
a = "Hello, World!"
print(a.lower())

#Python - Escape Characters

txt = 'It\'s alright.'
print(txt) 
txt = "This will insert one \\ (backslash)."
print(txt) 
# Python Booleans  expression is True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)
# Python Operators
#Arithmetic operators   (+,-,*,&,%)
x = 5
y = 3
print(x / y)

#Assignment operators
x = 5
x -= 3        # x = x-3   .i.e x=5-3=2
print(x)
x*=3
print(x)    # 6
x/=2
print(x)
#Comparison operators
x = 5
y = 3
#print(x == y)
#print(x!=y)
print(x<=y)

#Logical operators
x = 5
#print(x > 3 and x < 10)
print(x > 3 or x > 10)

# list 
mylist = ["Sports","Education","Seminar"]
print(mylist)
# length of a list
print(len(mylist))
mylist = [True,False,True]
print(mylist)
# different type of data 
mylist = ['Apple',23,True]
print(mylist)
# accesing items from the list

mylist = ["Sports","Education","Seminar","School"]
print(mylist[3])         # listname[indexno]

# Negative indexing
mylist = ["Sports","Education","Seminar","School"]
print(mylist[-4])
# access items by using range of index

mylist = ["Sports","Education","Seminar","School","Btech","MCA"]

#print(mylist[2:5])     # listname[startrange:end range]
#print(mylist[:5])
#print(mylist[3:])
#print(mylist[-3:-1])

# to checl any specific items exits in the list using in keyword

if "Seminar" in mylist:
    print("Yes")
# to change the item value 
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist[0]="Timetable"      # listname[indexno]="value"
print(mylist)
# To make chnage by using range value
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist[2:4] = ["Mr.John","Alex"]
print(mylist)
# insert items in a list  insert()
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
#mylist.insert(2,"Practice")   # insert(indexno,"value")
print(mylist)

# appned mehtod to insert   listname.append("value")
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.append("BCA")
print(mylist)

# extend a list from one list to another list
list1 =["BBA","BCA","MCA"]
list2 = ["25K","35K","65K"]
list1.extend(list2)
print(list1)
# Remove the items from a list
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.remove("Sports")
print(mylist)
# remove items by using pop method
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
#mylist.pop(4)
mylist.pop()  # if index not defined
print(mylist)
#sorting a list  listname.sort()  by default ascending order
mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.sort()
print(mylist)
# to sort in decending order

mylist = ["Sports","Education","Seminar","School","Btech","MCA"]
mylist.sort(reverse =True)
print(mylist)

# tuples is list
mytuples = ("Orange","Apple","Banana")
print(mytuples)
# by using single items
mytuples = ("Orange",)
print(mytuples)
# different types of data in tuples
mytuples = ("Orange",25,True)
print(mytuples)
# set
myset = {"Myschool","Books","Books"}
print(myset)
#enth of a set
myset = {"school","class","Exam","Result"}
print(len(myset))

#acees the elements from a set using in keyword
myset = {"school","class","Exam","Result"}
for x in myset:
    print(x)
#add items in the set

myset = {"school","class","Exam","Result"}
myset.add("Test")
print(myset)

# Remove items
myset = {"school","class","Exam","Result"}
myset.remove("class")
print(myset)

# python control statement
math = 45
eng =65
if math > eng:
    print("Student is good in Matchmatics")
else:
    print("Student is good in English")
# if - elseif-else
if math > eng:
    print("He is good in Math")
elif math == eng: 
    print("Student has scored equall marks in boths subject")
else:
    print("He is goog in English")
# while statement
a=5
while a<15:
    print(a)
    a +=2        # a = a+2   = 5+2
# for loops
student = ["Rohit","Tarun","Vikas","Sonia"]
for a in student:
    print(a)
    