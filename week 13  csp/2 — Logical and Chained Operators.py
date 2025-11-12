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

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

