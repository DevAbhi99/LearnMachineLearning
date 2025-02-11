
#Printing hello world
print("Hello World!")

#variables :- variables are the memory blocks created in the program to store datas

#Identifier is a name provided to the memory blocks or variables following certain naming convention

a=10

print(a)

a=20

print(a)


#Data Types

a=30

b=30.5

c=True

d="Hello"

print(a," ",b," ",c," ",d)


#Finding datatypes of variables using type keyword

print(type(a)," ",type(b)," ",type(c)," ",type(d))


#Operators

#There are 3 types of operators namely:- arithmetic, relational and logical

a=5
b=2

#1) Arithmetic operator :- +, -, *, /, %, **

#a) Addition +

print(a+b)

#b) Subtraction - 

print(a-b)

#c) Multiplication *

print(a*b)

#d) Division /

print(a/b)

#e) Remainder %

print(a%b)

#f) Power of **

print(a**b)


#Relational Operators :- >, <, >=, <=, ==, !=. These operators give boolean output

print(a>b)  #if condition is satisfied then will give true as output otherwise false

print(a!=b)

print(a>=b) #Any one condition is fulfilled the output will be true or otherwise false

#Logical operators :- or, and, not

print(a==b and a>b)

print(a==b or a>b)

print(not True)


#Type conversion and type casting

#The basic difference between the two is in type conversion the interpreter automatically converts the data type while type casting is forceful conversion and is done manually

#a) Type conversion (Automatic conversion by python interpretor)

a=10 #int value

b=20.5  #float value

print(a+b) #int value which is a will be converted to float and then added to b because float is superior in terms of storing data

#b) Type casting (Manual or forceful conversion)

a=10

b=int(20.5)

print(a+b) #output will be in int

#Input in python

a=float(input("Enter first number"))

b=float(input("Enter second number"))

print(a+b)
