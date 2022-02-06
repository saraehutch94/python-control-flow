# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input("Enter letter in the alphabet: ").lower()

vowels = ["a", "e", "i", "o", "u"]

if letter in vowels:
  print(f'The letter {letter} is a vowel')
else:
  print(f'The letter {letter} is a cononant')

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = None

while phrase != "quit":
  phrase = input("Enter a word or a phrase: ")
  print(f'What you entered is {len(phrase)} characters long')

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

human_years = input("Enter a dog's age in human years: ")

entered_age = int(human_years)

dog_years = 0

for number in range(0, entered_age, 1):
  if (number == 1) or (number == 2):
    dog_years += 10
  else:
    dog_years += 7

print(dog_years)

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

value1, value2, value3 = input("Enter the lengths of three sides of a triangle: ").split()

if value1 == value2 == value3:
  print(f'A triangle with sides of {value1}, {value2}, & {value3} is a equalateral triangle')
elif (value1 == value2) or (value2 == value3) or (value1 == value3):
  print(f'A triangle with sides of {value1}, {value2}, & {value3} is a isosceles triangle')
else:
  print(f'A triangle with sides of {value1}, {value2}, & {value3} is a scalene triangle')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

term = 0
number1 = 0
number2 = 0
count = 0

while term <= 50:
  print(f'term: {term} / number: {count}')
  if (term == 0):
    count += 1
    term += 1
  else:
    number1 = number2 + count
    number2 = count
    count = number1
    term += 1

# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
