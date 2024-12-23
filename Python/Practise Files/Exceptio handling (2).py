# initialize the amount variable 
amount = 10000
  
# perform division with 0 
amount = amount/ 0
print(amount)

##############
x = 50
y = "hello"
z = x + y 
############
x = 5
y = "hello"
try: 
    z = x + y 
except TypeError: 
    print("Error: cannot add an int and a str") 
    
    
## Try Expepct
item = [15, 17, 30] 
try:  
  print ("Secod element = %d" %(item[1])) 
  
  # Throws error since there are only 3 elements in array 
  print ("Fourth element = %d" %(item[2])) 
  
except: 
    print ("An error occurred") 
###############
def divide(p , q): 
   try: 
        c = ((p+q) / (p-q)) 
   except ZeroDivisionError: 
        print ("p/q result in 0") 
   else: 
        print (c) 
  
divide(6.0, 6.0) 

#############
try: 
    k = 5//0  # raises divide by zero exception. 
    print(k) 
  
# handles zerodivision exception 
except ZeroDivisionError: 
    print("Can't divide by zero") 
  
finally: 
    # this block is always executed 
    # regardless of exception generation. 
    print('This is always executed') 

