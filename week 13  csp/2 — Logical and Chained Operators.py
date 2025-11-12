# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True

# Grade Calculator
score = float(input("Enter your score (0-100): "))
# Use the regular, standard, American grading system!
if score >= 89.5 and score <= 100:
    print("Grade A get!")
elif score >= 79.5 and score < 89.5:
    print("Grade B get!")
elif score >= 69.5 and score < 79.5:
    print("Grade C get!")
elif score >= 59.5 and score < 69.5:
    print("Grade D get!")
elif score >= 0 and score < 59.5:
    print("Grade F get!")
else:
    print("N/A")


# Practice Problems:

# Write an expression that checks if a number is between 50 and 100 (inclusive).
num_expression = float(input("To win, type in a number between 50 and 100: "))
if 50 <= num_expression <= 100:
    print("Yep, that's between the limit!")
else:
    print("You silly goose.")

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.
write_expression = float(input("To win, type in a number that ISN'T 0 and is greater than 10: "))
print(write_expression != 0 and write_expression > 10)

# Use chained comparison to check if 3 < 4 < 5.
print("The Expression '3 < 4 < 5' Is ", str(3 < 4 < 5), ".")

# Challenge: Create a password rule using logical operators:
pass_new = input("Enter your new password. It must be 10 characters long and have at least 2 digits: ")
if len(pass_new) >= 10 and len([x for x in pass_new if x.isdigit()]) >= 2:
    print("Good.")
else:
    print("No.")
# Thank you to random stranger "Andres H." on Stack Overflow for helping (someone else) with the code above. I barely know what it means (yet)!
