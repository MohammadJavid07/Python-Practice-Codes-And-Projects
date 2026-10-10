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