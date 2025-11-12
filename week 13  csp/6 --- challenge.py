
# ##Day X Python Challenge — Commission & Bonus Calculator##

##Scenario:##
#You work for a school store that pays sales staff a ##commission## on monthly sales. Your manager wants a program that greets the salesperson by name, calculates their commission, and tells them whether they qualified for a monthly ##bonus##.

##Your program should:##

1. ##Ask for inputs## with `input()` and store them in variables:

   # The salesperson’s ##name## (string).
   # The salesperson’s ##total monthly sales## (float).
2. ##Calculate the commission## based on ##tiered rates##:

   # 13% if sales are ##below $10,000##
   # 15% if sales are ##$10,000 or more##
3. ##Round## the commission to ##two decimals## and ##print## a sentence with the ##name## and the ##commission## using an ##f-string##.
4. ##Use comparison + logical operators## to report a simple status:

   # If sales are ##≥ $8,000## ##and## commission is ##≥ $1,000##, print: `"Bonus unlocked!"`
   # Otherwise print: `"Keep pushing—you're close!"`
5. ##Do a quick identity tag## using ##string slicing## on the name:

   # Create `emp_code` from the ##first 3 letters## of the name (uppercase) + the ##last 2 digits## of the year `"25"`.
   # Example: `"Marvin"` → `"MAR25"`. Include this in your output line.
6. ##(Mini list task)## Ask for ##three product sales## (as three separate `float` inputs). Store them in a ##list##, compute their ##sum##, and print the list and its total.

   # If the ##list total## is within ##$1## of the monthly sales, print: `"Sales breakdown verified."` else `"Sales breakdown does not match."`

---

## ##Guidelines (read before you code)##

# Remember that `input()` returns a ##string##. Convert numeric inputs with `float()` where needed.
# Use ##f-strings## for your final messages.
# Use ##`round(value, 2)`## or formatted f-strings (e.g., `f"{value:.2f}"`) to display money.
# Keep your code clear: name your variables meaningfully and add a couple of comments.

---



* Accept the three product sales in **one line** (comma-separated), then **split → map to float → list**.
* Add input validation: if a user types a negative number or text for sales, print `"Invalid input"`.
* Add a message for **top performers**: if sales `>= 20000 or commission >= 3000` → `"Top Performer!"`.


