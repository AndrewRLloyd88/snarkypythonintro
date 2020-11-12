b = input('Enter a number between(0, 10)')

print("The Entered Number was " + b)

# Strings are a sequence of symbols in quotes
# Without the quotes, Python tries to interpret text as variable names!
a = 'imagination is more important than knowledge'

# Strings can contain any symbols, not just letters
b = 'The meaning of life is 42.'

# Concatenation (i.e. combining)
b = a + ', but not as important as learning to code'

# Functions on strings 
# Note: these functions don't change the original variables. They spit out copies with the function applied
b = a.capitalize()
b = a.upper()
b = b.lower()
b = a.replace('more', 'less')    # Replace all instances of 'more' with 'less'

# Input/output
print(a)                                           # Display a value on the screen
b = input('Enter a number between (0, 10)')        # Get a value from the user
print(a + ' ' + b)

# Conversion between strings and numbers
c = int(b)    # Useful for converting user inputs to numbers
c = float(b)
d = str(c)    # Useful for combining a number with a string before printing it
print('The entered number was ' + d)

# Let's improve out bill splitter so that it takes in input from the user
# and prints out the result

#input function always returns a string so you have to do (float(input))