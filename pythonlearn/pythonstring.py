#Python strings

#concatenation or joing of strings we use '+' in python

str1="hi"

str2=" man"

print(str1+str2)

#To find length of string in python we use len()

print(float(len(str1+str2)))

#To retrieve a part of a string we use the concept of slicing

str3=str1+str2

#To access character of a string

print(str3[1])

print(str3[0:2]) #Fetch hi

print(str3[3:]) #Fetch man 

print(str3[3:6])#Fetch man. we dont have to mention the last index of the string

#Slicing concept using negative indexes

print(str3[-6:-4]) #Fetch hi

print(str3[-3:]) #Fetch man

#Misc functions in python

#1) endswith() :- check if a given string ends with a given substring

print(str3.endswith("man"))

#2) capitalize() :- capitalize the first letter of a sentence

print(str3.capitalize())

#3) find() :- to find the index of the first letter of first occurence of string

str3=str3+" yo"

print(str3.find("man"))

#4) replace() :- replace character or substring with new in the string

print(str3.replace("yo", "ye"))

#5) count() :- to count the occurences of a character or a string

print(str3.count("hi"))




