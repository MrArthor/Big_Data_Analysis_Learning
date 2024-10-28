#R Basic
myString <- "Hello, Delhi!"
print ( myString)

# comments
if(FALSE) {
  "This is a demo for multi-line comments and it should be put inside either a 
      single OR double quote"
}
myString <- "Hello, World!"
print ( myString)

# Variable declaration and value assignment

name <- "John"
age <- 40

name   # output "John"
age    # output 40

# concatenating the variable
text <- "awesome"

paste("R is", text)

#adding two variables
text1 = "Bigdata"
text2 = "Technology"
paste(text1,text2)

#adding two variables different datatypes
text1 = "Bigdata"
text2 = "24"
paste(text1+text2) # will generate error

# Assigining one values to multiples variables
Height<-age<-weight<-40
Height
my_var <- 30 # my_var is type of numeric
my_var <- "Sally" # my_var is now of type character (aka string)
# to find the class of data
x <- 10.5
class(x)

# integer
x <- 1000L
class(x)

# complex
x <- 9i + 3
class(x)

# character/string
x <- "R is exciting"
class(x)

# logical/boolean
x <- TRUE
class(x)

#Type Conversion

x <- 1L # integer
y <- 2 # numeric

# convert from integer to numeric:
a <- as.numeric(x)
a

# convert from numeric to integer:
b <- as.integer(y)
b

# print values of x and y
x
y

# print the class name of a and b
class(a)
class(b)

# Built-in Math Functions
max(10,15,20)
min(10,15,20)
abs(-5.9)
ceiling(3.2)
floor(2.4)

# Assign a String to a Variable
str <- "CDAC"
str
# Assign a multiline String to a Variable
str <- "Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."
cat(str)
#  check if a character or a sequence of characters are present in a string

str <- "Hello World!"

grepl("H", str)
grepl("Hello", str)
grepl("X", str)

# booleans operations 
10 > 9 
