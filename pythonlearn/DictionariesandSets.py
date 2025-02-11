#Dictionaries are like objects in Python where datas are stored in key value pairs

#Dictionaries are mutable their values can be changed where usually overwritting happens

karan={
"age":21,
"skills":["Python", "Javascript", "Java"],
"role":{
"software":["programming languages", "React", "Express"],
"Hardware":["Arduino uno", "Electronics"]
}

}


print(karan["age"])

print(len(karan["role"]["software"]))


#Dictionaries functions

#1) key() :-retrieve all keys

print(karan.keys())

#2) value() :- retrieve all the values

print(karan.values())

#3) item() :- retrieve all key value pair

print(karan.items())

#4) get("") :- get value on the basis of key


print(karan.get(21))

#5) update() :- add new key value data in the dictionary

karan.update({"hobby":"video games"})

print(karan)


#Sets

#Sets are collections which stores unique datas and are immutable

#creating a set

collection={1,2,3,2}

print(collection)

#Set methods

#1) add(element) :- add an element

collection.add(4)

print(collection)

#2) collection.remove(element) :- removes a specified element

collection.remove(1)

print(collection)

#3) pop() :- removes a random element

collection.pop()

print(collection)

#4) clear() :- clears the entire set

collection.clear()

print(collection)

#creating empty set

newSet=set()

print(type(newSet))


#Set misc functions

#1) union :- add to sets and return a new

set1={1,2,3}

set2={3,4,5,6}

print(set1.union(set2))


#2) intersection :- return common set

print(set1.intersection(set2))


