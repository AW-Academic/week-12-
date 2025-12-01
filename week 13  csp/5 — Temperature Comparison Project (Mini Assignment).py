# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Simple, but functional code:
print("Hello, user! Let's track the temperature today!")
temp = float(input("What's the temperature today? "))

if (temp < -10) or (temp > 110):
    print("Extreme temperature warning!")

elif (temp > 75):
    print("Oh! A nice, hot day today! Make sure to wear sunscreen before going outside!")

elif (temp < 40):
    print("Ah! A pretty cool day today! Wear your jacket and mittens for the outdoors!")

else:
    print("Nice! Today looks to have swell weather!")