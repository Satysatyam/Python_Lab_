# Create a dictionary
my_dict = {'apple': 3, 'banana': 2, 'orange': 1}

# Access a value by its key
print(my_dict['apple'])  # Output: 3

# Add a new key-value pair
my_dict['pear'] = 4

# Modify a value by its key
my_dict['banana'] = 5

# Delete a key-value pair
del my_dict['orange']

# Check if a key is in the dictionary
print('apple' in my_dict)  # Output: True

# Get a list of all the keys
print(list(my_dict.keys()))  # Output: ['apple', 'banana', 'pear']

# Get a list of all the values
print(list(my_dict.values()))  # Output: [3, 5, 4]

# Get a list of all the key-value pairs
print(list(my_dict.items()))  # Output: [('apple', 3), ('banana', 5), ('pear', 4)]
