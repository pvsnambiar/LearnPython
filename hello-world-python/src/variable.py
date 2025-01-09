myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 
x = 5 # assign a integer to a variable
y = "John" # assign a string to a variable
a, b ,c = "Orange", "Banana", "Cherry";# assign multiple values to multiple variables
d= e = f = "Orange" # assign the same value to multiple variables
fruits = ["apple", "banana", "cherry"] # assign multiple values to multiple variables
x1, y1, z1 = fruits # assign the values of an array to multiple variables
s = 5
t = 10


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print(x)
print(y)  
print(a)
print(b)
print(c)
print(d)
print(e)    
print(f)    
print(x1)
print(y1)
print(z1) 
print(a, b, c, d, e, f, x1, y1, z1) # print multiple variables   
print(s + t) # print the sum of two variables
print (x + s) # print the sum of two variables
print (x + t) # print the sum of two variables
print (x + s + t) # print the sum of two variables
print (x + s + t + s)
print (x-t)
print (x , y) 

#--------------------------------
print("-----------------")
#Global Variables
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("You are " + x)

myfunc()

print("-----------------")

#Create a variable inside a function, with the same name as the global variable

aw = "awesome"

def myfunc():
  aw = "fantastic"
  print("Python is " + aw)

myfunc()

print("Tanmay is " + aw)

print("-----------------")

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Advaith is " + x)

print("-----------------")

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Manju is " + x)