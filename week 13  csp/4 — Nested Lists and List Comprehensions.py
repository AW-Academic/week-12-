
# Let's make nested lists!
print()
print("___NESTED STUFF___")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [list1, list2]
print(nested_list) # Output: [[1, 2, 3], [4, 5, 6]]
print(nested_list[1][2]) # Output: 6

fruits = ["apple", "orange", "banana", "coconut"] # 1D List
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats] # 2D List
print(groceries[1][2]) # Output: "potatoes"
print(groceries[0][2]) # Output: "banana"
print(groceries[2][2]) # Output: "turkey"

for collection in groceries:
    print(collection)

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()

# The numpad example (kids don't use these anymore)

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for char in row:
        print(char, end = " ")
    print()

# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:
print("___MATRIX STUFF___")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2])    # 3

# List comprehension (IMPORTANT ! ! !)
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]


# Practice Problems:
print("___PRACTICE STUFF___")

# Build a matrix variable containing 3 lists of 3 numbers each.
new_matrix = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]]

# Print the first list.
print(new_matrix[0])

# Print the second item from the third list.
print(new_matrix[2][1])

# Use a list comprehension to extract the last item from each sub-list.
list_comp = [row[2] for row in new_matrix]
print(list_comp)

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squared_numbers = [x**2 for x in range(1, 11)]
# for x in range(1, 11):
#   squared = x**2
#   print(squared)
print(squared_numbers)