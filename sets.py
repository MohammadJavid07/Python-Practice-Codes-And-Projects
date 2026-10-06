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

#Removing all elements from a set using clear
set_a.clear()
print(set_a)

#Creating a set from a list (removes duplicates)
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set_from_list = set(my_list) 
print(my_set_from_list)

#Creating a set from a string (removes duplicates)
my_string = "hello"
my_set_from_string = set(my_string)
print(my_set_from_string)

#Creating a set from a tuple (removes duplicates)
my_tuple = (1, 2, 2, 3, 4,  4, 5)
my_set_from_tuple = set(my_tuple)
print(my_set_from_tuple)

#Creating a set from a dictionary (removes duplicates and only keeps keys)
my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
my_set_from_dict = set(my_dict)     
print(my_set_from_dict)

#Creating a set from a range (removes duplicates)
my_range = range(1, 10)
my_set_from_range = set(my_range)
print(my_set_from_range)

#Creating a set from a generator expression (removes duplicates)
my_generator = (x for x in range(1, 10))
my_set_from_generator = set(my_generator)
print(my_set_from_generator)

#Creating a set from a list comprehension (removes duplicates)
my_list_comprehension = [x for x in range(1, 10)]   
my_set_from_list_comprehension = set(my_list_comprehension)
print(my_set_from_list_comprehension)


#Creating a set from a set comprehension (removes duplicates)
my_set_comprehension = {x for x in range(1, 10)}
print(my_set_comprehension) 

#Creating a set from a frozenset (removes duplicates)
my_frozenset = frozenset([1, 2, 3, 4, 5])
my_set_from_frozenset = set(my_frozenset)   
print(my_set_from_frozenset)

#Creating a set from a list of sets (removes duplicates)
list_of_sets = [{1, 2}, {2, 3}, {3, 4}]
my_set_from_list_of_sets = set()    
for s in list_of_sets:
    my_set_from_list_of_sets.update(s)
print(my_set_from_list_of_sets)

#Creating a set from a list of frozensets (removes duplicates)
list_of_frozensets = [frozenset({1, 2}), frozenset({2, 3}), frozenset({3, 4})]
my_set_from_list_of_frozensets = set()
for fs in list_of_frozensets:
    my_set_from_list_of_frozensets.update(fs)
print(my_set_from_list_of_frozensets)

#Creating a set from a list of tuples (removes duplicates)
list_of_tuples = [(1, 2), (2, 3), (3, 4)]
my_set_from_list_of_tuples = set()
for t in list_of_tuples:
    my_set_from_list_of_tuples.update(t)
print(my_set_from_list_of_tuples)