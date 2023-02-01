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

letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
vowels = 'aeiou'
consonants = 'bcdfghjklmpqrstvwxyz'

if letter in vowels:
    print(f'{letter} is a vowel')
elif letter in consonants:
    print(f'{letter} is a consonant')
else:
    print("Enter a letter")

print('------------------------------------------------')

# exercise-02 Length of Phrase
# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
prompt = input("Please enter a word or phrase: ")
if prompt != 'quit':   
    print(f"What you entered is", len(prompt), "characters long")
else:
    print('see ya!')

print('------------------------------------------------')

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
prompt_three = int(input("Input a dog's age in human years: "))

if prompt_three < 0:
    print("You need to enter a number.")
elif prompt_three == 1:
    print("The dog's age in dog years is 10 years old")
elif prompt_three == 2:
    print("The dog's age in dog years is 20 years old")
elif prompt_three >= 3:
    print(f"The dog's age in dog years is", (prompt_three * 7), "years old")

print('------------------------------------------------')

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

prompt_four = "Enter the lengths of three side of a triangle:"
prompt_a = int(input("Enter the length of side a: "))
prompt_b = int(input("Enter the length of side b: "))
prompt_c = int(input("Enter the length of side c: "))

if prompt_a == prompt_b == prompt_c:
    print(f"A triangle with sides of {prompt_a}, {prompt_b} & {prompt_c} is an equilateral triangle.")
elif prompt_a == prompt_b:
    print(f"A triangle with sides of {prompt_a}, {prompt_b} & {prompt_c} is an isosceles triangle.")
else: 
    print(f"A triangle with sides of {prompt_a}, {prompt_b} & {prompt_c} is a scalene triangle.")

print('------------------------------------------------')
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
def fibonacci(t):

    term1 = 0
    term2 = 1  
    if t == 1:
        print(term1)
    
    else:
        for term in range(0, t):   
            next_term = term1 + term2              
            term1 = term2
            term2 = next_term
            print(f"term: {term} / number: {next_term}")

fibonacci(51)
print('------------------------------------------------')

# exercise-06 What's the  Season?
# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then promptshtt the user to enter the day of the month:
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
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of the season as three characters (Jan - Dec): ")
day = input("Enter the day of the month (1-31): ")

if (month == "dec", "jan", "feb", "mar"):
    season = 'winter'
elif (month ==  "mar", "apr", "may", "jun"):
    season = 'spring'
elif (month == "jun", "jul", "aug", "sep"):
    season = 'summer'
else:
    season = 'fall'

if (month == 'Mar') and (day > 19):
    season = 'spring'
elif (month == 'Jun') and (day > 20):
    season = 'summer'
elif (month == 'Sep') and (day > 21):
    season = 'fall'
elif (month == 'Dec') and (day > 20):
    season = 'winter'
print(f"{month} {day} is in {season}.")

