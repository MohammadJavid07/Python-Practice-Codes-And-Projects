my_set = {1, 2, 3, 4, 5}
print(type(my_set))

#Creating an empty set
empty_set = set()

#Adding elements to a set
my_set.add(6)
print(my_set)

#Removing elements from a set
my_set.remove(3)
print(my_set)

#Checking if an element is in a set
print(4 in my_set)
print(7 in my_set)

#Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#Union
print(set_a | set_b)

#Intersection
print(set_a & set_b)

#Difference
print(set_a - set_b)

#Symmetric Difference
print(set_a ^ set_b)    

#Subset and Superset
print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))

#Clearing a set
my_set.clear()
print(my_set)

#Copying a set
set_copy = set_a.copy()
print(set_copy)

#Updating a set with another set
set_a.update(set_b)
print(set_a)

#Removing an element from a set using discard (does not raise an error if the element is not found)
set_a.discard(5)
print(set_a)

#Removing an element from a set using pop (removes and returns an arbitrary element)
popped_element = set_a.pop()
print(popped_element)
print(set_a)