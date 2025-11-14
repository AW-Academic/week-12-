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
#my_list.extend(range(15, 500))
#print(my_list)
# ...let's make it a list!
#my_list.extend(list(range(15, 500)))
#print(my_list)
# 600 more.
#my_list.extend(range(500, 1100))
#print(my_list)

new_list = ['a', 'b', 'c']
print(new_list) # ['a', 'b', 'c']
new_list.append('d')
print(new_list) # ['a', 'b', 'c', 'd']
# Removing an item from the list
removed_item = new_list.pop()
# Removes the last item by default
print(removed_item) # d
print(new_list) # ['a', 'b', 'c']
remove_second_item = new_list.pop(1)
# Removes the item at index 1
print(remove_second_item) # b
print(new_list) # ['a', 'c']

# Sorting the list
numbers = [4, 2, 5, 1, 3]
print(numbers)
numbers.sort()
print(numbers) # [1, 2, 3, 4, 5]
# Reversing the list
numbers.reverse()
print(numbers) # [5, 4, 3, 2, 1]
# Inserting an item at a specific position
# The code below inserts 10 at index 2, and
# moves everything after that over.
numbers.insert(2, 10)
print(numbers) # [5, 4, 10, 3, 2, 1]
numbers.insert(6, 64)
print(numbers) # [5, 4, 10, 3, 2, 1, 64]
# Replacing items
# Different from inserting, remember!
third_list = [7, 8, 9]
third_list[0] = 6
print(third_list) # [6, 8, 9]

import random
random_list = random.sample(range(1, 100), 10)
# This will create a list of 10 unique random
# numbers between 1 and 99.
print(random_list)
# Sorting them!
random_list.sort()
print(random_list)
# ...or you can do this:
print(sorted(random_list))
sorted_list = sorted(random_list)
print(sorted_list)
# Reverse the list, then
# remove every 3rd item from the list.
sorted_list.pop(2)
sorted_list.pop(4)
sorted_list.pop(6)
print(sorted_list)



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