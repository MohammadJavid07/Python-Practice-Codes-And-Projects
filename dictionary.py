#How to create a dictionary in Python
employee = {'name': 'John Doe', 'age': 30, 'position': 'Software Engineer', 'department': 'IT', 'salary': 75000}
print(employee)

#Creating a dictionary using the dict() constructor
employee_dict = dict(name='Jane Smith', age=28, position='Data Analyst', department='Marketing', salary=65000)
print(employee_dict)

#Creating a dictionary from a list of tuples
employee_list_of_tuples = [('name', 'Alice Johnson'), ('age', 35), ('position', 'Project Manager'), ('department', 'Operations'), ('salary', 85000)]
employee_dict_from_tuples = dict(employee_list_of_tuples)
print(employee_dict_from_tuples)

#Creating a dictionary from two lists using the zip() function
keys = ['name', 'age', 'position', 'department', 'salary']
values = ['Bob Wilson', 40, 'HR Specialist', 'Human Resources', 70000]
employee_dict_from_lists = dict(zip(keys, values))
print(employee_dict_from_lists)

#Creating a dictionary from a list of keys and a single value using the fromkeys() method
keys = ['name', 'age', 'position', 'department', 'salary']
value = 'N/A'
employee_dict_from_keys = dict.fromkeys(keys, value)
print(employee_dict_from_keys)

#adding a new key-value pair to an existing dictionary
employee['email'] = 'john.doe@example.com'
print(employee) 

#updating an existing key-value pair in a dictionary
employee['salary'] = 80000
print(employee)

#removing a key-value pair from a dictionary using the del statement
del employee['department']
print(employee)

#removing a key-value pair from a dictionary using the pop() method
removed_value = employee.pop('age')
print(f"Removed value: {removed_value}")
print(employee) 

#removing a key-value pair from a dictionary using the popitem() method
removed_item = employee.popitem()
print(f"Removed item: {removed_item}")
print(employee) 

#removing all key-value pairs from a dictionary using the clear() method
employee.clear()    
print(employee)

#Creating a dictionary from a list of dictionaries using the update() method
employee1 = {'name': 'John Doe', 'age': 30, 'position': 'Software Engineer', 'department': 'IT', 'salary': 75000}
employee2 = {'name': 'Jane Smith', 'age': 28, 'position': 'Data Analyst', 'department': 'Marketing', 'salary': 65000}
employee1.update(employee2) 
print(employee1)

#Creating a dictionary from a list of dictionaries using the update() method with a loop
employee_list = [{'name': 'Alice Johnson', 'age': 35, 'position': 'Project Manager', 'department': 'Operations', 'salary': 85000},
                 {'name': 'Bob Wilson', 'age': 40, 'position': 'HR Specialist', 'department': 'Human Resources', 'salary': 70000}]
employee_dict = {}
for employee in employee_list:
    employee_dict.update(employee)
print(employee_dict)

#Creating a dictionary from a list of dictionaries using the update() method with a dictionary comprehension
employee_list = [{'name': 'Alice Johnson', 'age': 35, 'position': 'Project Manager', 'department': 'Operations', 'salary': 85000},
                 {'name': 'Bob Wilson', 'age': 40, 'position': 'HR Specialist', 'department': 'Human Resources', 'salary': 70000}]
employee_dict = {k: v for d in employee_list for k, v in d.items()}
print(employee_dict)

