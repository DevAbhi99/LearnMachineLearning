#Lists

#These are like arrays in other programming languages

#Unlike strings lists are mutable which means the datas can be changed

#Lists store different kinds of datas

arr=[10,10.0, True, "Hi"]

#Accessing list datas

print(arr[1])

#changing datas in lists

arr[1]=20.0

print(arr)

#finding length of list

print(len(arr))

#Slicing a list (We use the same concept we use in slicing string)

print(arr[1:3])





#Lists misc methods

arr1=[2,3,1,4,6,5]

#1) append() :- add a data or an element at the end

arr1.append(7)

print(arr1)

#2) sort() :- sort the list in ascending order

arr1.sort()

print(arr1)

#3) sort(reverse=True) :- sort the list in descending order

arr1.sort(reverse=True)

print(arr1)

#4) reverse() :- reverse a list

arr1.reverse()

print(arr1)

#5) insert(index, element) :- insert a data or an element in any index value of a list

arr1.insert(1,99)

print(arr1)

#6) pop(index) :- in python when we use pop we can specify the index we want to delete where in other programming languages pop() deletes the last element

arr1.pop(1)

print(arr1)


#Tuples

#These are data structures like lists which are immutable as the datas cannot be changes

tup=(1,2,3,4,5,6,2)

print(type(tup))

#Tuple functions

#1) index() :- helps us to find index of a data 

print(tup.index(1))

#2) count() :- helps us to find count

print(tup.count(2))



