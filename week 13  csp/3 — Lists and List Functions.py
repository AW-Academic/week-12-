# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# Creating a list

# Collections are used to store multiple items in a single variable
# Lists are ordered collections of items
# Lists are mutable, meaning you can change their content
# Lists are created using square brackets []
my_list = [1, 2, 3, 4, 5]
# Instead of creating separate variables
# for each item, i.e....
# var1 = 1
# var2 = 2
# var3 = 3...
# ...we can store them in a list.
# This makes our job easier when we
# need to store multiple items.
# Performance task answer lol


print(my_list) # [1, 2, 3, 4, 5]
print(type(my_list)) # <class 'list'>
# Accessing elements
print(my_list[0]) # 1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[0:]) # [1, 2, 3, 4, 5]
print(my_list[-1]) # 5
# Modifying lists
# Adding an item to the end of the list
my_list.append(6)
print(my_list) # [1, 2, 3, 4, 5, 6]
my_list.append(7)
my_list.append(8)
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]
# We can use the extent method for appending multiple items
my_list.extend([9,10,11,12,13,14])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# What if we wanted to print up to 500? (Range method)
# The below won't givee you what you want, so...
my_list.extend(range(15, 500))
print(my_list)
# ...let's make it a list!
my_list.extend(list(range(15, 500)))
print(my_list)
# 600 more.
my_list.extend(range(500, 1100))
print(my_list)

# Examples:

#my_list = ['apple', 'banana', 'cherry']
#print(my_list[0])         # apple
#print(my_list[1:])        # ['banana', 'cherry']

#my_list.append('grape')
#print(my_list)

#my_list.pop(1)
#print(my_list)

#numbers = [3, 1, 4, 2]
#numbers.sort()
#print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.